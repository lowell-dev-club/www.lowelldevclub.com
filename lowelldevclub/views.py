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

old_workshops = ['workshop1.html']
short_links = ['https://hackclub.com/workshops/personal_website#part-iii-the-css-file','https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules']

@app.route('/workshop/old', methods=['GET'])
def workshop_old():
    return render_template('old_workshop.html', old_workshops=old_workshops)

@app.route('/workshop/old/<workshop_name>', methods=['GET'])
def workshop_old_displaying(num):
    return render_template(file_name)

@app.route('/workshop/hack<int:num>', methods=['GET'])
def hack(num):
    if num - 1 > len(short_links) or num <= 0:
        return 'Short link doesn\'t exsist'
    return redirect(short_links[num - 1])

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
