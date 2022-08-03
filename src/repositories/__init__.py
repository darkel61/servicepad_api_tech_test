from flask_sqlalchemy import SQLAlchemy
from .user import UserRepository
from .session import SessionRepository
from .publication import PublicationRepository


db = SQLAlchemy()
__all__ = ['UserRepository', 'SessionRepository', 'PublicationRepository']