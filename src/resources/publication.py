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

class UpdatePublication(Resource):
    def put(self):
        request_json = request.get_json(silent=True)
        id = request_json.get('id', '')
        title = request_json.get('title', '')
        description = request_json.get('description', '')
        priority = request_json.get('priority', '')
        token = request_json.get('token', '')

        user = SessionRepository.token_check(token)

        if not user:
            return {"message": "Unauthorized"}, 403

        try:
            publication = PublicationRepository.update(id, title, description, priority)
            return publication, 200
        except Exception as e:
            print(e)
            return {"message": "Something went wrong"}, 400

class DeletePublication(Resource):
    def delete(self):
        request_json = request.get_json(silent=True)
        id = request_json.get('id', '')
        token = request_json.get('token', '')

        user = SessionRepository.token_check(token)

        if not user:
            return {"message": "Unauthorized"}, 403

        try:
            publication = PublicationRepository.delete(id)
            return publication, 200
        except Exception as e:
            print(e)
            return {"message": "Something went wrong"}, 400


class GetPublication(Resource):
    def get(self):
        request_json = request.get_json(silent=True)
        token = request_json.get('token', '')

        user = SessionRepository.token_check(token)

        if not user:
            return {"message": "Unauthorized"}, 403

        try:
            publications = PublicationRepository.getAll(user.id)
            return publications, 200
        except Exception as e:
            print(e)
            return {"message": "Something went wrong"}, 400


