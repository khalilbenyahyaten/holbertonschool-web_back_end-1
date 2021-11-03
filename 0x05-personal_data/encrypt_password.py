#!/usr/bin/env python3

"""encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """return a hashed, salted password"""
    p = password.encode()
    return bcrypt.hashpw(p, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """returns a boolean"""
    return bcrypt.checkpw(password.encode(), hashed_password)
