from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectMultipleField, SubmitField, DateField, IntegerField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from datetime import datetime

class OrderForm(FlaskForm):
    created_by = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    phone = StringField('Phone Number', [DataRequired()])
    pickup_or_delivery = RadioField('Pickup or Delivery?', [DataRequired()], choices=[('pickup', 'Pickup'), ('delivery', 'Delivery')], default='pickup')
    date = StringField('Date', [DataRequired()])
    item = SelectMultipleField('What would you like to order?', [DataRequired()], choices=[('wedding', 'Wedding Cake'), ('tasting', 'Wedding Cake Tasting'), ('bento', 'Bento Cake'), ('carved', 'Carved Cake'), ('6cake', '6" Cake'), ('8cake', '8" Cake'), ('1/4sheet', '1/4 Sheet Cake'), ('1/2sheet', '1/2 Sheet Cake'), ('cookieCake', 'Cookie Cake'), ('cupcakes', 'cupcakes'), ('cookies', 'cookies'), ('decCookies', 'Decorated Sugar Cookies'), ('cheesecake', 'Cheesecake'), ('cinn rolls', 'Cinnamon Rolls'), ('pie', 'Pie'), ('miniPie', 'Mini Pie'), ('pops', 'Cake Pops'), ('brownies', 'Brownies'), ('cookieKit', 'Cookie Decorating Kit'), ('bunt', 'Bunt Cake'), ('chocStraw', 'Chocolate Strawberries')])
    quantity = IntegerField('Quantity', [DataRequired()])
    description = StringField('Description', [DataRequired()])
    submit = SubmitField()


class SignupForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    birthday = DateField(label='Date', validators=[DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField("Confirm your Password", [DataRequired(), EqualTo('password')])
   
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Sign In')

class ReviewForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    rating = StringField('rating', [DataRequired()])
    comments = StringField('comments', [DataRequired()])
    date = DateField('date', [DataRequired()], default=datetime.utcnow)
    submit = SubmitField('post review')
   