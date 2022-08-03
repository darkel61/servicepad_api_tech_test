from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .abc import BaseModel
from .user import User

__all__ = ['BaseModel', 'User']