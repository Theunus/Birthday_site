from flask import Flask
from flask_bootstrap5 import Bootstrap  
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'Templates')

app = Flask(__name__, template_folder=template_dir)  # Ensure it reflects the Docker container structure

# Updated DATABASE_URL for 'pro-track' database
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '12345')
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "mysql+pymysql://tokelly:theunusok33@localhost/pro_track?charset=utf8mb4")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes
