#!/usr/bin/env python3
"""
takes in a password and returns a hashed password
"""
import hashlib
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    hashes a password
    """
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())
