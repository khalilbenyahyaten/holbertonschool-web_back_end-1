#!/usr/bin/env python3
"""
takes in a password and returns a hashed password
"""
import hashlib
import bcrypt
import uuid import uuid4
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    hashes a password
    """
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
            return user
        else:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """credentials validation"""
        try:
            user = self._db.find_user_by(email=email)
            result = bcrypt.checkpw(bytes(password, "utf-8"),
                                    user.hashed_password)
            if result is False:
                return False
            return True
        except NoResultFound:
            return False

    def _generate_uuid() -> str:
        """generates uuid"""
        return str(uuid.uuid4())
