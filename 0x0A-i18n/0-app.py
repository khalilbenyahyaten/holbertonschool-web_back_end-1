#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask
from flask.templating import render_template, render_template

app = Flask(__name__)

@app.route("/")
def holby_welcome():
    """renders 0-index"""
    return render_template('0-index.html')

