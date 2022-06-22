from .base import BaseConfig


class Config(BaseConfig):
    DEBUG = True
    TESTING = False
    JSONIFY_PRETTYPRINT_REGULAR = False

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/video_streaming"
