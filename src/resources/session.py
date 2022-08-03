from flask import request, jsonify
from flask_restful import Resource

from repositories import SessionRepository


class Login(Resource):
    def post(self):
        request_json = request.get_json(silent=True)
        if request_json:
            email: str = request_json.get('email', '')
            password: str = request_json.get('password', '')
            user = SessionRepository.login(email, password)
            return user, 200
        else:
            return {"message": "No email or password provided."}, 400

class Logout(Resource):
    def post(self):
        request_json = request.get_json(silent=True)
        if request_json:
            email: str = request_json.get('email', '')
            token: str = request_json.get('password', '')
            response = SessionRepository.logout(email, token)
            return response
        else:
            return {"success": False, "message": "Something went wrong"}, 400