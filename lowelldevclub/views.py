from lowelldevclub import app
from flask import render_template, request, make_response, redirect

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/partners', methods=['GET'])
def partners():
    return render_template('partners.html')

@app.route('/sponsors', methods=['GET'])
def sponsors():
    return render_template('sponsors.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
