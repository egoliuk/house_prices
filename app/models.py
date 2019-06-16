from datetime import datetime
from app import db
import enum

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    houses = db.relationship('House', backref='purveyor', lazy='dynamic')

    def __repr__(self):
        return f"<User {self.username}, email {self.email}>"

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
    MSSubClass = db.Column(db.Enum(MSZoning))
    LotArea = db.Column(db.Float)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<House {self.Id}>"
