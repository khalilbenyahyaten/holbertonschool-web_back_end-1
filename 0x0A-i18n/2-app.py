#!/usr/bin/env python3
"""
Basic Flask app
"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel

class Config():
    """ Configuration for babel translation """
    LANGUAGES = ["en", "fr"]

app = Flask(__name__)
app.config.from_object(Config())
Babel.default_locale = "en"
Babel.default_timezone = "UTC"
babel = Babel(app)

@babel.localeselector
def get_locale():
    """local func"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])
