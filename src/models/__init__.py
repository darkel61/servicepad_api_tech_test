from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .abc import BaseModel
from .user import User
from .publication import Publication

__all__ = ['BaseModel', 'User', 'Publication']