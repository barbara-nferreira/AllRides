from flask import Flask, request, redirect, url_for, render_template, jsonify
from models import *
from database import session

app = Flask(__name__)

# functions


def getCategories():
    listCategories = []
    temp = session.query(Category).all()
    for category in temp:
        listCategories.append(category)
    return listCategories

# routes


@app.route('/')
def index():
    newlyAdded = (
        session.query(Vehicle)
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
    vehicles = session.query(Vehicle).filter(
        Vehicle.is_available == True).all()

    return render_template('public/listing.html', vehicles=vehicles, categories=getCategories())


@app.post('/listing')
def listingPost():
    category_id = request.form['category']
    available_for_rent = request.form['available_for_rent']
    location = request.form['location'].lower()
    listVehicles = []

    vehicles = session.query(Vehicle).filter(
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
    vehicle = session.query(Vehicle).filter_by(id=id).first()
    if not vehicle:
        return "Vehicle not found"

    return render_template('public/vehicle-details.html', vehicle=vehicle)


@app.route('/contact')
def contact():
    return render_template('public/contact.html')


if __name__ == '__main__':
    app.run(debug=True)
