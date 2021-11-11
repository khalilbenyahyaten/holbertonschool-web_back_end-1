#!/usr/bin/env python3
"""Basic auth"""

import base64
import typing
from api.v1.auth.auth import Auth
from typing import TypeVar, Iterable


class BasicAuth(Auth):
    """ Defines the BasicAuth class that inherits from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts Base64 Authorization Header """
        if (
            not authorization_header
            or not isinstance(authorization_header, str)
            or "Basic " not in authorization_header
        ):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decode Base64 Authorization Header """
        if (
            not base64_authorization_header
            or not isinstance(base64_authorization_header, str)
        ):
            return None
        try:
            b64_bytes = base64_authorization_header.encode('utf-8')
            string_bytes = base64.b64decode(b64_bytes)
            return string_bytes.decode('utf-8')
        except Exception:
            return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decode Base64 Authorization Header """
        if (
            not base64_authorization_header
            or not not not isinstance(base64_authorization_header, str)
        ):
            return None
        try:
            b64_bytes = base64_authorization_header.encode('utf-8')
            string_bytes = base64.b64decode(b64_bytes)
            return string_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Extract User Credentials """
        if (
            not decoded_base64_authorization_header
            or not isinstance(decoded_base64_authorization_header, str)
            or ':' not in decoded_base64_authorization_header
        ):
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))
