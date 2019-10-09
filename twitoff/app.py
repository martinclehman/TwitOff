from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_or_update_user

# Unix/Mac
# 'sqlite:////absolute/path/to/db.sqlite3'
# Windows
# 'sqlite:///C:\\Users\\bruno\\OneDrive\\Desktop\\TwitOff\\twitoff\\db.sqlite3'

load_dotenv()

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/martin/Documents/MyGitHub/DS-Unit-3-Sprint-3-Productization-and-Cloud/TwitOff/twitoff/db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='TwitOff!', users=User.query.all())

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['user_name']
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.username==name).one().tweets
        except Exception as e:
            message = 'Error adding {}: {}'.format(name,e)
            tweets = []
        return render_template('user.html', title=name, tweets=tweets,message=message)

    return app


    def compare_users():
        pass