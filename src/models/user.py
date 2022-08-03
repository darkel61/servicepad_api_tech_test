from . import db
from .abc import BaseModel

import datetime


class User(db.Model, BaseModel):
    email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    fullname = db.Column(db.String, nullable=False)
    photo = db.Column(db.String, nullable=True)
    token = db.Column(db.String, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, email: str, photo: str = '',password: str = '',fullname: str = ''):
        self.email = email
        self.password = password
        self.fullname = fullname
        self.photo = photo