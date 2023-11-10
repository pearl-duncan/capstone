from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    orders= db.relationship('Order', backref='my_orders')
    reviews = db.relationship('Review', backref='my_reviews')

    def __init__(self, name, email, password, birthday):
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    pickup_or_delivery = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    item = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)

    def __init__(self, crated_by, email, phone, pickup_or_delivery, date, item, quantity, description):
        self.crated_by = crated_by
        self.email = email
        self.phone = phone
        self.pickup_or_delivery = pickup_or_delivery
        self.date = date
        self.item = item
        self.quantity = quantity
        self.description = description

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    rating = db.Column(db.String, nullable=False)
    comments = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)

    def __init__(self, name, rating, comments):
        self.name = name
        self.rating = rating
        self.comments = comments

