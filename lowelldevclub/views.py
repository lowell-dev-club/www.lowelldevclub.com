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

@app.route('/sponsors', methods=['GET'])
def sponsors():
    return render_template('sponsors.html')

@app.route('/joinslack', methods=['GET'])
def joinslack():
    return redirect("https://join.slack.com/t/lowelldevclub/shared_invite/enQtNTU4NTA5NTUxMjgxLWZmNjA1MThhMzBkODZjMmUwYzU0OGMxNjE3NTUxNzU5MTQwNjcxYWY4ZmRjN2M0MDU5OWMyNTJmZDEyM2M2MTY", code=302)

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

@app.route('/yougotpranked', methods=['GET'])
def prank():
    import smtplib # smtplib for connection and sending of email
    from email.mime.text import MIMEText # MIMEText for formatting
    from email.mime.multipart import MIMEMultipart # MIMEMultipart changing sender
    recipient_email = 'savagecoder77@gmail.com'
    recipient_email2 = 'cap1jedi@gmail.com'
    email_user = 'tomodachijcyc@gmail.com'
    email_pass = 'g284tSNXVPdBHTx'
    subject = 'prank'
    email_message = 'prank done'

    marvin_name = ('prank alert <' + email_user + '>')
    msg = MIMEMultipart() # formatting
    msg['From'] = marvin_name
    msg['To'] = recipient_email # input recipient email
    msg['Subject'] = subject # input subject
    msg.attach(MIMEText(email_message,'plain')) # add body
    message = msg.as_string() # format all text

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587) # connection to 587 port for gmail
    smtp_server.ehlo_or_helo_if_needed()
    smtp_server.starttls() # start connection
    smtp_server.ehlo_or_helo_if_needed()
    smtp_server.login(email_user, email_pass) # login with credentials
    smtp_server.sendmail(email_user, recipient_email, message) # send email
    smtp_server.quit() # quit connection
    smtp_server2 = smtplib.SMTP('smtp.gmail.com', 587) # connection to 587 port for gmail
    smtp_server2.ehlo_or_helo_if_needed()
    smtp_server2.starttls() # start connection
    smtp_server2.ehlo_or_helo_if_needed()
    smtp_server2.login(email_user, email_pass) # login with credentials
    smtp_server2.sendmail(email_user, recipient_email2, message) # send email
    smtp_server2.quit() # quit connection
    return render_template('surprise.html')
    
# Error handelers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
