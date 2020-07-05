from lowelldevclub import app, login_manager, db, bcrypt
from hashlib import sha256
from lowelldevclub.forms import *
from lowelldevclub.models import *
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup as bs
from flask import render_template, request, make_response, redirect, send_file, url_for, flash, abort


@login_manager.user_loader
def load_user(id):
    try:
        return User.query.get(int(id))
    except BaseException:
        return None

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


@app.route('/donate', methods=['GET'])
def donate():
    return render_template('donate.html')


@app.route('/joinslack', methods=['GET'])
def joinslack():
    return redirect(
        "https://join.slack.com/t/lowelldevclub/shared_invite/enQtNTU4NTA5NTUxMjgxLWZmNjA1MThhMzBkODZjMmUwYzU0OGMxNjE3NTUxNzU5MTQwNjcxYWY4ZmRjN2M0MDU5OWMyNTJmZDEyM2M2MTY",
        code=302)


@app.route('/short<num>', methods=['GET'])
def short(num):

    try:
        shortLink = ShortLink.query.get(int(num))
        if shortLink is None:
            raise BaseException
    except:
        abort(404)

    shortLink.timesused += 1
    db.session.commit()
    return redirect(shortLink.link)


@app.route('/info/short<num>', methods=['GET'])
def shortInfo(num):

    try:
        shortLink = ShortLink.query.get(int(num))
        if shortLink is None:
            raise BaseException
    except:
        abort(404)

    return render_template('shortinfo.html', shortLink=shortLink)


@app.route('/workshop/recent', methods=['GET'])
def workshopRecent():

    workshops = Workshop.query.all()
    workshops.sort(key=lambda workshop: workshop.created, reverse=True)

    return redirect(url_for('workshop', url=workshops[0]))


@app.route('/workshop', methods=['GET'])
def workshopList():

    workshops = Workshop.query.all()
    workshops.sort(key=lambda workshop: workshop.created, reverse=True)

    return render_template('workshopList.html', workshops=workshops)


@app.route('/workshop/<url>', methods=['GET'])
def workshop(url):

    checkWorkshop = Workshop.query.filter_by(url=url).first()

    if checkWorkshop is None:

        flash('Workshop not found')
        abort(404)

    checkWorkshop.timesviewed += 1
    db.session.commit()

    if checkWorkshop.workshopMD is not None:

        r = get('https://github.com/lowell-dev-club/flask-workshop-2.0/blob/master/README.md')
        soup = bs(r.text, 'lxml')
        mdHtml = soup.findAll(attrs={'class':'markdown-body entry-content container-lg'})[0]

        return render_template('workshop.html', workshop=checkWorkshop, mdHtml=mdHtml)

    return render_template('workshop.html', workshop=checkWorkshop, mdHtml=None)


@app.route('/create/workshop', methods=['GET','POST'])
@login_required
def createWorkshop():

    form = CreateWorkshop()

    if form.validate_on_submit():
        if form.repo.data == '':
            repo = None
        else:
            repo = form.repo.data

        if form.markdown.data == '':
            md = None
        else:
            md = form.markdown.data

        newWorkshop = Workshop(name=form.name.data, repoUrl=repo, workshopMD=md, text=form.text.data, url=form.url.data, timesviewed=0, created=datetime.now())
        db.session.add(newWorkshop)
        db.session.commit()

        flash('Workshop created successfully!', 'success')
        return redirect(url_for('workshop', url=form.url.data))

    return render_template('createWorkshop.html', form=form, edit=False)


@app.route('/edit/workshop/<id>', methods=['GET','POST'])
@login_required
def editWorkshop(id):

    try:
        checkWorkshop = Workshop.query.get(int(id))
        if checkWorkshop is None:
            raise BaseException
    except:
        abort(404)

    form = CreateWorkshop()

    if form.validate_on_submit():
        if form.repo.data == '':
            repo = None
        else:
            repo = form.repo.data

        if form.markdown.data == '':
            md = None
        else:
            md = form.markdown.data

        checkWorkshop.repoUrl = repo
        checkWorkshop.workshopMD = md
        checkWorkshop.name = form.name.data
        checkWorkshop.url = form.url.data
        checkWorkshop.text = form.text.data
        db.session.commit()

        flash('Workshop edited successfully!', 'success')
        return redirect(url_for('workshop', url=form.url.data))

    form.name.data = checkWorkshop.name
    form.repo.data = checkWorkshop.repoUrl or ''
    form.markdown.data = checkWorkshop.workshopMD or ''
    form.url.data = checkWorkshop.url
    form.text.data = checkWorkshop.text
    return render_template('createWorkshop.html', form=form, edit=True, workshop=checkWorkshop)


@app.route('/delete/workshop/<id>', methods=['GET','POST'])
@login_required
def deleteWorkshop(id):

    try:
        checkWorkshop = Workshop.query.get(int(id))
        if checkWorkshop is None:
            raise BaseException
    except:
        abort(404)

    form = ConfirmPassword()

    if form.validate_on_submit():
        if bcrypt.check_password_hash(
                current_user.password,
                sha256(
                    (form.password.data +
                     current_user.email).encode('utf-8')).hexdigest()):
            db.session.delete(checkWorkshop)
            db.session.commit()
            flash('Workshop deleted', 'info')
            return redirect(url_for('dashboard'))

        flash('Incorrect Password', 'error')
        form.password.data = ''

    return render_template('passwordConfirm.html', form=form, title='Delete Workshop', message=f'Confirm you want to delete the workshop {checkWorkshop.name}')


@app.route('/create/shortlink', methods=['GET','POST'])
@login_required
def createLink():

    form = CreateShortLink()

    if form.validate_on_submit():

        newShortLink = ShortLink(link=form.longurl.data, timesused=0)
        db.session.add(newShortLink)
        db.session.commit()

        flash('Short link created successfully!', 'success')
        return redirect(url_for('shortInfo', num=newShortLink.id))

    return render_template('createLink.html', form=form, edit=False)


@app.route('/edit/shortlink/<id>', methods=['GET','POST'])
@login_required
def editLink(id):

    try:
        shortLink = ShortLink.query.get(int(id))
        if shortLink is None:
            raise BaseException
    except:
        abort(404)

    form = CreateShortLink()

    if form.validate_on_submit():

        shortLink.link = form.longurl.data
        if form.clearCount.data:
            shortLink.timesused = 0
        db.session.commit()

        flash('Short link edited successfully!', 'success')
        return redirect(url_for('shortInfo', num=shortLink.id))

    form.longurl.data = shortLink.link
    return render_template('createLink.html', form=form, edit=True, link=shortLink)


@app.route('/delete/shortlink/<id>', methods=['GET','POST'])
@login_required
def deleteLink(id):

    try:
        shortLink = ShortLink.query.get(int(id))
        if shortLink is None:
            raise BaseException
    except:
        abort(404)

    form = ConfirmPassword()

    if form.validate_on_submit():
        if bcrypt.check_password_hash(
                current_user.password,
                sha256(
                    (form.password.data +
                     current_user.email).encode('utf-8')).hexdigest()):
            db.session.delete(shortLink)
            db.session.commit()
            flash('Workshop deleted', 'info')
            return redirect(url_for('dashboard'))

        flash('Incorrect Password', 'error')
        form.password.data = ''

    return render_template('passwordConfirm.html', form=form, title='Delete Shortlink', message=f'Confirm you want to delete the shortlink for {shortLink.link}')


@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    users = User.query.all()
    workshops = Workshop.query.all()
    links = ShortLink.query.all()

    return render_template('dashboard.html', users=users, workshops=workshops, links=links)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        flash('You are already logged in', 'warning')
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        user = User.query.filter_by(email=email).first()
        if user is None:
            flash(
                f'Login Unsuccessful. User dosen\'t exsist',
                'error')
        else:
            if bcrypt.check_password_hash(
                user.password,
                sha256(
                    (form.password.data +
                     email).encode('utf-8')).hexdigest()):

                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')

                flash(f'Logged in successfully.', 'success')
                return redirect(next_page) if next_page else redirect(
                    url_for('home'))

            else:
                flash(
                    'Login Unsuccessful. Please check email and password',
                    'error')

    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():

    if current_user.is_authenticated:
        logout_user()
        flash('Logout successful', 'success')

    return redirect(url_for('home'))


@app.route('/create/user', methods=['GET', 'POST'])
@login_required
def userCreation():

    form = CreateUser()

    if form.validate_on_submit():

        try:
            email = form.email.data.lower()

            duplicationCheck = User.query.filter_by(
                email=email).first()

            if duplicationCheck is not None:

                flash(f'Duplicate email found', 'error')

                return render_template('userCreate.html', form=form)

            tempPass = bcrypt.generate_password_hash(sha256((form.password.data + email).encode('utf-8')).hexdigest()).decode('utf-8')

            newUser = User(
                email=email,
                password=tempPass)

            db.session.add(newUser)
            db.session.commit()

            flash(
                f'User created for {form.email.data}',
                'success')

        except BaseException as e:
            flash(f'User couldn\'t be created. Error: {e}', 'error')

        return redirect(url_for('home'))
    return render_template('userCreate.html', form=form)


@app.route('/delete/user/<id>', methods=['GET','POST'])
@login_required
def deleteUser(id):

    try:
        checkUser = User.query.get(int(id))
        if checkUser is None:
            raise BaseException
    except:
        abort(404)

    if current_user.id != checkUser.id:

        flash('You can only delete your own account', 'error')
        return redirect(url_for('dashboard'))

    form = ConfirmPassword()

    if form.validate_on_submit():
        if bcrypt.check_password_hash(
                current_user.password,
                sha256(
                    (form.password.data +
                     current_user.email).encode('utf-8')).hexdigest()):
            logout_user()
            db.session.delete(checkUser)
            db.session.commit()
            flash('Your user has been deleted')
            return redirect(url_for('home'))

        flash('Incorrect Password', 'error')
        form.password.data = ''

    return render_template('passwordConfirm.html', form=form, title='Delete User', message='Confirm you want to delete your account')

short_links = [
    'https://hackclub.com/workshops/personal_website#part-iii-the-css-file',
    'https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules',
    'https://github.com/lowell-dev-club/python-text-game/blob/master/workshop.md',
    'https://github.com/lowell-dev-club/python-emailer/blob/master/workshop.md',
    'https://github.com/lowell-dev-club/youtube-scraper/blob/master/README.md',
    'https://github.com/lowell-dev-club/live-flask-workshop']


@app.route('/latin/', methods=['GET', 'POST'])
def latin():
    form = LatinForm()
    if request.method == 'POST':
        form.link = 'https://en.m.wiktionary.org/wiki/' + \
            str(form.word.data) + '#Latin'
    return render_template('latin.html', form=form)


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
