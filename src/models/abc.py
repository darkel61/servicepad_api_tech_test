from . import db


class BaseModel:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def delete(self):
        db.session.delete(self)
        db.session.commit()