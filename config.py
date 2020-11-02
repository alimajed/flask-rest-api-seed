from os import getenv

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv(), verbose=True)


class ConfigFactory:
    def factory():
        env = getenv("FLASK_ENV", "development")

        if env in ["development"]:
            return Development()

    factory = staticmethod(factory)


class Config:
    """base config class contains same configurations in all environments"""
    pass


class Development(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')