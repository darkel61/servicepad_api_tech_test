from sqlalchemy.exc import IntegrityError
from models import Publication

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