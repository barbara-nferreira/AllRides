from flask import Flask, request, redirect, url_for, render_template, jsonify
from models import *
from database import session

app = Flask(__name__)


@app.route('/')
def index():
    newlyAdded = (
        session.query(Vehicle)
        .filter_by(is_available=True)
        .order_by(desc(Vehicle.vehicle_id))
        .limit(3)
        .all()
    )
    return render_template('index.html', newlyAdded=newlyAdded)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/listing')
def listing():
    category = request.args.get('category')
    is_for_rent = request.args.get('is_for_rent')
    location = request.args.get('location')

    query = session.query(Vehicle).filter_by(is_available=True)

    if category:
        query = query.filter(Vehicle.category.has(name=category))

    if is_for_rent is not None:
        if is_for_rent == 'True':
            query = query.filter(Vehicle.available_for_rent == True)
        else:
            query = query.filter(Vehicle.available_for_rent == False)

    if location:
        query = query.filter(Vehicle.location.ilike(f'%{location}%'))

    vehicles = query.all()

    return render_template('listing.html', vehicles=vehicles, category=category, is_for_rent=is_for_rent, location=location)

@app.route('/details/<int:vehicle_id>')
def details(vehicle_id):
    vehicle = session.query(Vehicle).filter_by(vehicle_id=vehicle_id).first()
    if not vehicle:
        return "Vehicle not found"

    return render_template('vehicle-details.html', vehicle=vehicle)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
