from sqlalchemy.exc import IntegrityError
# from exceptions import ResourceExists
from models import User


class UserRepository:
    @staticmethod
    def create(email, fullname, password, photo) -> dict:
        """ Create user """
        result: dict = {}
        try:
            user = User(email=email, photo=photo, password=password, fullname=fullname)
            user.save()
            result = {
                'email': user.email,
                'password': user.password,
                'fullname': user.fullname,
                'photo': user.photo,
                'date_created': str(user.date_created),
            }
        except IntegrityError:
            User.rollback()
            # raise ResourceExists('user already exists')

        return result