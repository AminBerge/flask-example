SECRET_KEY = "fdsafasd"
UPLOAD_FOLDER = "image_pool"
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
import os

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class StagingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}