from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    ugis = IntegerField('Ugis', [DataRequired()])
    svoris = IntegerField('Svoris', [DataRequired()])
    amzius = IntegerField('Amzius', [DataRequired()])
    submit = SubmitField('Submit')