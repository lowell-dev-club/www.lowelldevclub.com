import os

'''
Config class
'''


class Config(object):
    # Get the secret key or use the key dev if the devclubkey is not set
    SECRET_KEY = os.environ.get('devclubkey', 'dev')

    TESTING = False
    DEBUG = False

    # Using Postgresql
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
