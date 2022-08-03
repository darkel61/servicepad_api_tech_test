from flask_restful import Api
from resources import UserCreate, Login, Logout
from models import User as UserModel, db
from flask_migrate import Migrate
from app import create_app

app = create_app()
migrate = Migrate(app, db)


# API
api = Api(app)
api.add_resource(UserCreate, '/api/user')
api.add_resource(Login, '/api/user/login')
api.add_resource(Logout, '/api/user/logout')

# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=UserModel)