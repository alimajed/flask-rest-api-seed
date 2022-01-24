from os import getenv

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv(), verbose=True)


class ConfigFactory:
    def factory():
        env = getenv("FLASK_ENV", "development")

        if env in ["development"]:
            return Development()
        elif env in ["testing"]:
            return Testing()

    factory = staticmethod(factory)


class Config:
    """base config class contains same configurations in all environments"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")


class Development(Config):
    DEBUG = True
    TESTING = False
    POSTGRES_USER = getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = getenv('POSTGRES_DB')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db/{POSTGRES_DB}"



class Testing(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_TESTING_URI')