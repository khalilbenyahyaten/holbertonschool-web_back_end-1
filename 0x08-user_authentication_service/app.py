#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request, abort, make_response, json, redirect
from auth import Auth

app = Flask(__name__)


@app.route('/', methods=['GET'])
def idex():
    """JSON form"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """users"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": "{}".format(user.email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """sessions"""
    email = request.form.get['email']
    password = request.form.get['password']

    if Auth.valid_login(email, password) is False:
        abort(401)
    session_id = Auth.create_session(email)
    resp = make_response({"email": email, "message": "logged in"})
    resp.set_cookie('session_id', session_id)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
