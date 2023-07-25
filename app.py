from flask import Flask, request, redirect, url_for, render_template, jsonify, session, flash
from models import *
from database import db_session
import re

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
        # Show the admin panel
        return render_template('admin/index.html')
    else:
        flash('You need to sign in to access the admin panel.', 'error')
        return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)
