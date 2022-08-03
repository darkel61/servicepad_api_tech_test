from lib2to3.pgen2 import token
from flask import request
from flask_restful import Resource

from repositories import PublicationRepository, SessionRepository

class CreatePublication(Resource):
    def post(self):
        request_json = request.get_json(silent=True)
        title = request_json.get('title', '')
        description = request_json.get('description', '')
        priority = request_json.get('priority', '')
        token = request_json.get('token', '')
        
        user = SessionRepository.token_check(token)

        if not user:
            return {"message": "Unauthorized"}, 403

        try:
            publication = PublicationRepository.create(title, description, priority, user.id)
            return publication, 200
        except Exception as e:
            print(e)
            return {"message": "Something went wrong"}, 400


# UpdatePublication
# DeletePublication
# GetPublications