from lowelldevclub import app
from flask import render_template, request, make_response, redirect

@app.route('/', methods=['GET'])
def hello_world():
    return 'Lowell Dev Club'
