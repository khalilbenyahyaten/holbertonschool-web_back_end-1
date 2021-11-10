#!/usr/bin/env python3
"""Basic auth"""

import base64
from api.v1.auth.auth import Auth


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
