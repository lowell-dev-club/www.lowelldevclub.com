from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email, Length

'''
Form for lowell student easier latin searching
For emerson lol
'''
class LatinForm(FlaskForm):
    link = None
    word = StringField('Word:')
    submit = SubmitField('Find')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class CreateShortLink(FlaskForm):
    longurl = StringField('Url to shorten', validators=[DataRequired(), Length(max=120)])
    clearCount = BooleanField('Clear url usage count?')
    submit = SubmitField('Shorten')


class ConfirmPassword(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class CreateWorkshop(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    repo = StringField('Repo url', validators=[Length(max=100)])
    markdown = StringField('Markdown url', validators=[Length(max=100)])
    url = StringField('https://www.lowelldev.club/', validators=[DataRequired(), Length(max=50)])
    text = TextAreaField(
        'Description',
        widget=TextArea(),
        validators=[
            DataRequired(),
            Length(
                max=500,
                message='Description must be 500 characters or less')])
    submit = SubmitField('Create')


class CreateUser(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create')