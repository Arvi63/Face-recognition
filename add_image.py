from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField,FileField

from wtforms import validators, ValidationError,DataRequired

class ContactForm(Form):
   name = TextField("Name:",validators=[DataRequired()],[validators.Required("Please enter your name.")])
     
   id = IntegerField("ID:",validators=[DataRequired()],[validators.Required("Please enter ID.")])
   image = FileField('Image:',validators=[DataRequired()],[validators.Required("Please insert image.")])
   submit = SubmitField("Upload")