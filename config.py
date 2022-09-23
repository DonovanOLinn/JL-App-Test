import os 
#os.chdir('<path URL>')
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))

# Give access to the project in any OS we find ourselves in
# Allow outside files or folders to be added to the project from
# the base directory
load_dotenv(os.path.join(basedir, '.env'))


class Config():

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False