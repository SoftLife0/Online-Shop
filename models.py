from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from main import db, login_manager, app
from flask_login import UserMixin

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    price = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), nullable=True)

class Item(db.Model):
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(10), nullable=True)
    description = db.Column(db.String(), nullable = False)
    image =  db.Column (db.String(), default='default.jpg')
    trending = db.Column (db.Boolean, default = False)
    category = db.Column(db.String(), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.username', ondelete="CASCADE"), nullable=False)
    vendor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
def __repr__(self): 
    return f"Item('{self.name}', '{self.category}' )"

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    owner = db.Column(db.String(), nullable=True)
    size = db.Column(db.String())
    crop = db.Column(db.String())
    location = db.Column(db.String())
    phone = db.Column(db.String())
    price = db.Column(db.String())
    link = db.Column(db.String())
    otherPictures = db.Column(db.String())
    description = db.Column(db.String())
    picture =  db.Column (db.String(), default='default.jpg')
    trending = db.Column (db.Boolean, default = False)
    category = db.Column(db.String())

def __repr__(self): 
    return f"Farm('{self.owner}', '{self.phone}' )"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable = False)
    phone = db.Column(db.String(15), nullable=False)
    # Remove password length limit
    password = db.Column(db.String())
    stock = db.relationship('Item', backref='author', lazy=True)

def __repr__(self):
    return '<User %r' % self.username

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

def __repr__(self):
    return '<Category %r' % self.name