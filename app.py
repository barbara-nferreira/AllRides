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


if __name__ == '__main__':
    app.run(debug=True)
