#!/usr/bin/env python3
"""
Basic Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """config lang"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config())
Babel.default_locale = "en"
Babel.default_timezone = "UTC"
babel = Babel(app)
