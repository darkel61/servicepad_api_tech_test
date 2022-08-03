from flask import request
from flask_restful import Resource

from repositories import UserRepository

class UserCreate(Resource):
    def post(self):
        """
        Create user
        """
        request_json = request.get_json(silent=True)
        email: str = request_json.get('email', '')
        password: str = request_json.get('password', '')
        fullname: str = request_json.get('fullname', '')
        photo: str = request_json.get('photo', '')
        
        try:
            user = UserRepository.create(email, fullname, password, photo)
            return user, 200
        except Exception as e:
            print(e)
            return {"message": "Something went wrong"}, 400