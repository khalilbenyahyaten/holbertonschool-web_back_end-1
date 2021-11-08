#!/usr/bin/env python3
"""
create class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """defines the Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        True if the path is `None`, `excluded_paths` is `None` or if the
        `path` is not in the list of strings `excluded_paths`,
        False otherwise.
        """
        if path and excluded_paths:
            for ex_path in excluded_paths:
                if ex_path.endswith('/') or ex_path.endswith('*'):
                    ex_path = ex_path[:-1]
                if ex_path in path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Flask request object"""
        return None
