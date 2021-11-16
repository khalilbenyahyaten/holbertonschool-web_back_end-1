#!/usr/bin/env python3
""" session
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """sessionauth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user ID"""
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """cookie value"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        try:
            return User.get(id=user_id)
        except KeyError:
            return None
