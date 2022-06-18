import logging


class BaseConfig:
    LOGGING_LEVEL = logging.INFO

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/catalog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ITEMS_PER_PAGE = 25
    SECRET_KEY = ""
    ENCRYPT_KEY = b""

    BASIC_AUTH_USERNAME = ""
    BASIC_AUTH_PASSWORD = ""
