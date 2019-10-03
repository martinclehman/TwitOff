from flask import Flask
from .models import DB

# Unix/Mac
# 'sqlite:////absolute/path/to/db.sqlite3'
# Windows
# 'sqlite:///C:\\Users\\bruno\\OneDrive\\Desktop\\TwitOff\\twitoff\\db.sqlite3'

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/martin/Documents/MyGitHub/DS-Unit-3-Sprint-3-Productization-and-Cloud/TwitOff/twitoff/db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return("Welcome to TwitOff!")

    return app
