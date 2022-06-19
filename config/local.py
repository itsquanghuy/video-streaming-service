from .base import BaseConfig


class Config(BaseConfig):
    DEBUG = True
    TESTING = False
    JSONIFY_PRETTYPRINT_REGULAR = False

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/netflix_clone"

    SECRET_KEY = "secret"
    ENCRYPT_KEY = b"aaaaaaaaaaaaaaaa"

    BASIC_AUTH_USERNAME = "admin"
    BASIC_AUTH_PASSWORD = "123456"
