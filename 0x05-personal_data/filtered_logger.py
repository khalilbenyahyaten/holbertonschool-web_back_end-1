#!/usr/bin/env python3

"""return the log message obfuscated"""
from typing import List
import re
import logging


REDACTION = "***"
FORMAT = "%(name)s %(levelname)s %(asctime)s %(message)s"
SEPARATOR = ";"


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns a log message obfuscated"""
    lst = message.split(separator)

    for i in fields:
        for j in range(len(lst)):
            if lst[j].startswith(i):
                subst = i + '=' + redaction
                lst[j] = re.sub(lst[j], '', lst[j])
                lst[j] = subst
    return separator.join(lst)
