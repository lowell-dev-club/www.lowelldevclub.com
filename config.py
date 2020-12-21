import os

'''
Config class
'''


class Config(object):

    SECRET_KEY = os.environ.get('devclubkey')

    TESTING = False
    DEBUG = False

    # Using Postgresql
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
