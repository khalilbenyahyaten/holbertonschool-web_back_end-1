#!/usr/bin/env python3

"""encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """return a hashed, salted password"""
    p = password.encode()
    return bcrypt.hashpw(p, bcrypt.gensalt())
