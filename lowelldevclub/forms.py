from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

'''
Form for lowell student easier latin searching
'''


class LatinForm(FlaskForm):
    class Meta:
        csrf = False
    link = None
    word = StringField('Word:')
    submit = SubmitField('Find')
