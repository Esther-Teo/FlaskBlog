#Initialise application and bring tgt various components

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

#importing flask class
app = Flask(__name__)
app.config.from_object(Config)
#__name__ = special variable that is name of module
#below pretend database call
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)


from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)