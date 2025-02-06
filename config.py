"""
This module contains configuration classes for the Flask web application.
Each class defines configuration settings for different environments.
"""

import os


class Config:
    """
    Base configuration class. Contains default configuration settings.
    """

    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_hard_to_guess_string"
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() in [
        "true",
        "on",
        "1",
    ]
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class DevelopmentConfig(Config):
    """
    Development configuration class. Inherits from Config and sets DEBUG to True.
    """

    DEBUG = True


class TestingConfig(Config):
    """
    Testing configuration class. Inherits from Config and sets TESTING to True.
    Also suppresses sending emails.
    """

    TESTING = True
    MAIL_SUPPRESS_SEND = True


class ProductionConfig(Config):
    """
    Production configuration class. Inherits from Config and sets DEBUG and TESTING to False.
    """

    DEBUG = False
    TESTING = False
