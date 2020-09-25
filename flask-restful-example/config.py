"""Flask configuration variables."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')


    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = True # When set to 'True', Flask-SQLAlchemy will log all database activity to Python's stderr for debugging purposes
    SQLALCHEMY_TRACK_MODIFICATIONS = False # remove annoying notification
