from lowelldevclub import app
from flask import render_template, request, make_response, redirect, send_file

# User routes
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/partners', methods=['GET'])
def partners():
    return render_template('partners.html')
'''
@app.route('/sponsors', methods=['GET'])
def sponsors():
    return render_template('sponsors.html')
'''
@app.route('/joinslack', methods=['GET'])
def joinslack():
    return redirect("https://join.slack.com/t/lowelldevclub/shared_invite/enQtNTU4NTA5NTUxMjgxLWZmNjA1MThhMzBkODZjMmUwYzU0OGMxNjE3NTUxNzU5MTQwNjcxYWY4ZmRjN2M0MDU5OWMyNTJmZDEyM2M2MTY", code=302)

@app.route('/workshop', methods=['GET'])
def workshop():
    return render_template('workshop1.html')

@app.route('/workshop/hack1', methods=['GET'])
def hack1():
    return redirect('https://hackclub.com/workshops/personal_website#part-iii-the-css-file')

@app.route('/workshop/hack2', methods=['GET'])
def hack2():
    return redirect('https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules')

# SEO
@app.route('/robots.txt', methods=['GET'])
def robots():
    return send_file('templates/seo/robots.txt')

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    sitemap_xml = render_template('seo/sitemap.xml')
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
    
# Error handelers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
