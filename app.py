from flask import Flask, request, redirect, url_for, render_template, jsonify, session, flash
from models import *
from database import db_session
import re
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)
app.secret_key = 'secret'
# app.config['SECRET_KEY'] = 'secret'

# functions


def getCategories():
    listCategories = []
    temp = db_session.query(Category).all()
    for category in temp:
        listCategories.append(category)
    return listCategories

# public routes


@app.route('/')
def index():
    newlyAdded = (
        db_session.query(Vehicle)
        .filter_by(is_available=True)
        .order_by(desc(Vehicle.id))
        .limit(3)
        .all()
    )
    return render_template('public/index.html', newlyAdded=newlyAdded)


@app.route('/about')
def about():
    return render_template('public/about.html')


@app.get('/listing')
def listing():
    vehicles = db_session.query(Vehicle).filter(
        Vehicle.is_available == True).all()

    return render_template('public/listing.html', vehicles=vehicles, categories=getCategories())


@app.post('/listing')
def listingPost():
    category_id = request.form['category']
    available_for_rent = request.form['available_for_rent']
    location = request.form['location'].lower()
    listVehicles = []

    vehicles = db_session.query(Vehicle).filter(
        Vehicle.is_available == True).all()

    for vehicle in vehicles:
        listVehicles.append(vehicle)

    if category_id:
        listVehicles = [
            vehicle for vehicle in listVehicles if vehicle.category_id == int(category_id)]

    if available_for_rent == 'True':
        listVehicles = [
            vehicle for vehicle in listVehicles if vehicle.available_for_rent]
    elif available_for_rent == 'False':
        listVehicles = [
            vehicle for vehicle in listVehicles if not vehicle.available_for_rent]

    if location and location.strip():
        listVehicles = [
            vehicle for vehicle in listVehicles if vehicle.location.lower() == location]

    return render_template('public/listing.html', vehicles=listVehicles, categories=getCategories())


@app.route('/details/<int:id>')
def details(id):
    vehicle = db_session.query(Vehicle).filter_by(id=id).first()
    if not vehicle:
        return "Vehicle not found"

    return render_template('public/vehicle-details.html', vehicle=vehicle)


@app.route('/contact')
def contact():
    return render_template('public/contact.html')

# admin routes


@app.get('/signup')
def signup():
    return render_template('admin/signup.html')


@app.post('/signup')
def signupPost():
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Check if the user already exists in the database
    user = db_session.query(User).filter(User.email == email).first()
    if user:
        flash('Email already exists. Please sign in.', 'success')
        return redirect(url_for('signin'))

    # Create a new user
    new_user = User(email=email, password=password)
    db_session.add(new_user)
    db_session.commit()

    flash('Account created successfully. Please sign in.', 'success')
    return redirect(url_for('signin'))


@app.get('/signin')
def signin():
    return render_template('admin/signin.html')


@app.post('/signin')
def signinPost():
    email = request.form['email']
    password = request.form['password']

    # Check if the user exists in the database
    user = db_session.query(User).filter(User.email == email).first()
    if not user:
        return "user_not_exists"

    # Check if the entered password matches the one in the database
    if user.password == password:
        # Store user data in the session
        session['user_id'] = user.id
        session['user_email'] = user.email

        return "success"
    else:
        return "invalid_password"


@app.route('/signout')
def signout():
    # Clear user data from the session to sign out
    session.pop('user_id', None)
    session.pop('user_email', None)
    return redirect(url_for('signin'))


@app.route('/admin')
def indexAdmin():
    # Check if the user is logged in by verifying session data
    if 'user_id' in session and 'user_email' in session:
        # Get the top 3 rented vehicles with the highest total earnings
        top_vehicles = db_session.query(
            Vehicle.year,
            Vehicle.make,
            Vehicle.model,
            Vehicle.image_url,
            Category.name.label('category_name'),
            Vehicle.rental_price_per_day,
            func.sum(Rental.total_price).label('total_earnings')
        ).join(Rental).join(Category).group_by(Vehicle.id).order_by(desc('total_earnings')).limit(3).all()

        # Get total value of rentals received in 2023
        total_rentals = db_session.query(func.sum(Rental.total_price)).filter(
            Rental.rental_start_date >= '2023-01-01',
            Rental.rental_start_date < '2024-01-01'
        ).scalar() or 0.0

        # Get total value of purchases received in 2023
        total_purchases = db_session.query(func.sum(Purchase.total_price)).filter(
            Purchase.purchase_date >= '2023-01-01',
            Purchase.purchase_date < '2024-01-01'
        ).scalar() or 0.0

        # Get total number of clients
        total_clients = db_session.query(func.count(Client.id)).scalar() or 0

        # Get total number of vehicles available (inventory count)
        total_vehicles_available = db_session.query(func.count(Vehicle.id)).filter(
            Vehicle.is_available == True
        ).scalar() or 0

        return render_template('admin/index.html', top_vehicles=top_vehicles,
                               total_rentals=total_rentals,
                               total_purchases=total_purchases,
                               total_clients=total_clients,
                               total_vehicles_available=total_vehicles_available)

    else:
        flash('You need to sign in to access the admin panel.', 'error')
        return redirect(url_for('signin'))

@app.get('/add-vehicle')
def addVehicle():
    return render_template('admin/add-vehicle.html', categories=getCategories())

@app.post('/add-vehicle')
def addVehiclePost():
    category_id = request.form.get('category', type=int)
    make = request.form['make']
    model = request.form['model']
    year = request.form.get('year', type=int)
    fuel_type = request.form['fuel_type']
    horsepower = request.form.get('horsepower', type=int)
    kilometers = request.form.get('kilometers', type=float)
    transmission = request.form['transmission']
    image_url = request.form['image_url']
    location = request.form['location'].lower()
    available_for_rent = request.form.get('available_for', type=str) == 'Rent'
    available_for_purchase = request.form.get('available_for', type=str) == 'Purchase'
    rental_price_per_day = request.form.get('rental_price', type=float)
    purchase_price = request.form.get('purchase_price', type=float)

    new_vehicle = Vehicle(
        category_id=category_id,
        make=make,
        model=model,
        year=year,
        fuel_type=fuel_type,
        horsepower=horsepower,
        kilometers=kilometers,
        transmission=transmission,
        image_url=image_url,
        location=location,
        available_for_rent=available_for_rent,
        available_for_purchase=available_for_purchase,
        rental_price_per_day=rental_price_per_day if available_for_rent else None,
        purchase_price=purchase_price if available_for_purchase else None,
        is_available=True
    )
    db_session.add(new_vehicle)
    db_session.commit()

    return redirect(url_for('indexAdmin'))

if __name__ == '__main__':
    app.run(debug=True)
