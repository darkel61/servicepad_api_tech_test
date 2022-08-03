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
            }
        except IntegrityError:
            Publication.rollback()
            # raise ResourceExists('user already exists')

        return result