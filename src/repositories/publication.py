from sqlalchemy.exc import IntegrityError
from models import Publication
import json

class PublicationRepository:
    @staticmethod
    def create(title, description, priority, user_id) -> dict:
        """ Create user """
        result: dict = {
            'success': False
        }
        try:
            publication = Publication(title=title, description=description, priority=priority, user_id=user_id)
            publication.save()
            result = {
                'success': True,
                'title': publication.title,
                'publication_id': publication.id
            }
        except IntegrityError:
            Publication.rollback()
            # raise ResourceExists('user already exists')

        return result

    @staticmethod
    def update(id, title, description, priority) -> dict:
        result: dict = {
            'success': False
        }
        try:
            publication = Publication.query.filter_by(id=id).first()

            if title:
                publication.title = title
            if description:
                publication.description = description
            if priority:
                publication.priority = priority
            publication.commit()

            result = {
                'success': True,
                'title': publication.title,
                'publication_id': publication.id
            }
        except IntegrityError:
            Publication.rollback()

        return result

    @staticmethod
    def delete(id) -> dict:
        result: dict = {
            'success': False
        }
        try:
            publication = Publication.query.filter_by(id=id).first()
            publication.delete(publication)
            result = {
                'success': True,
                'message': "Successfully Deleted"
            }
        except IntegrityError:
            Publication.rollback()

        return result

    @staticmethod
    def getAll(user_id) -> dict:
        result: dict = {
            'success': False
        }
        publications_array = []
        try:
            publications = Publication.query.filter_by(user_id=user_id).all()

            for publication in publications:
                publications_array.append({
                    'id': publication.id,
                    'title': publication.title,
                    'description': publication.description,
                    'priority': publication.priority,
                    'status': publication.status,
                    'user_id': publication.user_id,
                    'created_at': str(publication.created_at),
                    'updated_at': str(publication.updated_at),
                    'published_at': str(publication.published_at)
                })

            result = {
                'success': True,
                'publications': publications_array
            }
        except IntegrityError:
            Publication.rollback()

        return result