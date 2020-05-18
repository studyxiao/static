import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'jdfgjiagergnewgjkrehjgekrglargwarklnggfaga'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

    USERNAME = os.environ.get('USERNAME') or 'username'
    PASSWORD = os.environ.get('PASSWORD') or 'password'
