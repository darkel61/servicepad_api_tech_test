from . import db
from .abc import BaseModel

import datetime

class Publication(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    published_at = db.Column(db.DateTime)
    

    def __init__(self, title, description, priority, user_id):
        self.title = title
        self.description = description
        self.priority = priority
        self.user_id = user_id