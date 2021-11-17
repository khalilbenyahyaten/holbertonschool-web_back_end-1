#!/usr/bin/env python3
"""session auth"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.eoute('/auth_session/login', Methods=['POST'], strict_slashes=False)
def login() -> str:
    """"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    user_id_not_found = {"error": "no user found for this email"}
    try:
        users = User.search({'email': email})
    except KeyError:
        return jsonify(user_id_not_found), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user_id=user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
    return jsonify({"error": "wrong password"}), 401
