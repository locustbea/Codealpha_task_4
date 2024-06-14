from flask import render_template, request, redirect, url_for
from . import db
from .models import URL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['original_url']
    # Logic to create a short URL and store it in the database
    return redirect(url_for('index'))
