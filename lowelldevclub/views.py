from lowelldevclub import app
from flask import render_template, request, make_response, redirect

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
