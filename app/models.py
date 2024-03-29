from datetime import datetime
from app import db
from app import login
import enum
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_visit = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    houses = db.relationship('House', backref='purveyor', lazy='dynamic')

    def __repr__(self):
        return f"<User {self.username}, email {self.email}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"

class MSZoning(enum.Enum):
    A = "Agriculture"
    C = "Commercial"
    FV = "Floating Village Residential"
    I = "Industrial"
    RH = "Residential High Density"
    RL = "Residential Low Density"
    RP = "Residential Low Density Park"
    RM = "Residential Medium Density"

class House(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    SalePrice = db.Column(db.Float, index=True, nullable=True)
    MSZoning = db.Column(db.String(32))
    LotArea = db.Column(db.Float)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<House {self.Id}>"
