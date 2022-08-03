from models import User
import random
class SessionRepository:
    @staticmethod
    def login(email, password):
        user: dict = {}
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            user.token = random.randint(100000000000,999999999999)
            user.commit()
            return {"success": True, "token": user.token}
        else:
            return {"succes": False, "message": "Bad Credentials"}

    @staticmethod
    def logout(email, token):
        user: dict = {}
        user = User.query.filter_by(email=email, token=token).first()
        if user:
            user.token = ''
            user.commit()
            return {"success": True}
        else:
            return {"succes": False, "message": "Bad Credentials"}

    @staticmethod
    def token_check(token):
        user: dict = {}
        user = User.query.filter_by(token=token).first()
        if user:
            return user
        else:
            return False