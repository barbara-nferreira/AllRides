from flask import Flask, request, redirect, url_for, render_template, jsonify
from models import *
from database import session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
