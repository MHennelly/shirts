import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    TESTING = False


class DevelopmentConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")


class ProductionConfig(Config):
    TESTING = False
