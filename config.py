import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I-like-cookies'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or fr'sqlite:///{os.path.join(basedir, "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    '''
    gmail config:
    export MAIL_SERVER=smtp.googlemail.com
    export MAIL_PORT=587
    export MAIL_USE_TLS=1
    export MAIL_USERNAME=<your-gmail-username>
    export MAIL_PASSWORD=<your-gmail-password>
    local smtpd server:
    python -m smtpd -n -c DebuggingServer localhost:8025
    export MAIL_SERVER=localhost
    export MAIL_PORT=8025
    '''
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['krzysztof.krolikowski92@gmail.com']