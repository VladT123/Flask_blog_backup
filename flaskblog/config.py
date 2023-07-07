import os


class Config:
    SECRET_KEY = "123412413"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'smithingmidnight@outlook.com'
    MAIL_PASSWORD = '12348765aA'
