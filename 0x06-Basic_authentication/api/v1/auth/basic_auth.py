#!/usr/bin/env python3
"""Basic auth"""

from api.v1.basic_auth import BasicAuth
import base64


class BasicAuth(Auth):
    """Basic_Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Base64"""
    if (
        not authorization_header or type(authorization_header) != str
        or "Basic " not in authorization_header
    ):
        return None
    return authorization_header.split()[1]
