from lowelldevclub import app
from flask import render_template, request, make_response, redirect, send_file, url_for

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

old_workshops = ['workshop1','workshop2','workshop3','workshop4']
short_links = ['https://hackclub.com/workshops/personal_website#part-iii-the-css-file',
               'https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules',
               'https://github.com/lowell-dev-club/python-text-game/blob/master/workshop.md',
               'https://github.com/lowell-dev-club/python-emailer/blob/master/workshop.md',
               'https://github.com/lowell-dev-club/youtube-scraper/blob/master/README.md']

@app.route('/workshop/old', methods=['GET'])
def workshop_old():
    return render_template('old_workshop.html', old_workshops=old_workshops)

@app.route('/workshop/old/<workshop_name>', methods=['GET'])
def workshop_old_displaying(workshop_name):
    for items in old_workshops:
        if workshop_name == items:
            return render_template(items + '.html')
    return 'Archived workshop doesn\'t exsist'

@app.route('/workshop', methods=['GET'])
def workshop():
    return redirect(url_for('workshop_old_displaying', workshop_name=old_workshops[len(old_workshops) - 1]))

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
