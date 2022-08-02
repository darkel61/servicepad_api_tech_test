from sqlalchemy.exc import IntegrityError
# from exceptions import ResourceExists
from models import User


class UserRepository:

    @staticmethod
    def create(email: str, photo: str = '',password: str = '',fullname: str = '') -> dict:
        """ Create user """
        result: dict = {}
        try:
            user = User(email=email, photo=photo, password=password, fullname=fullname)
            user.save()
            print(user)
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

    @staticmethod
    def get(username: str) -> dict:
        """ Query a user by username """
        user: dict = {}
        user = User.query.filter_by(username=username).first_or_404()
        user = {
          'username': user.username,
          'date_created': str(user.date_created),
        }
        return user