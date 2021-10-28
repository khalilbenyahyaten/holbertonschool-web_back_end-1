#!/usr/bin/env python3

"""index_range"""

from typing import Tuple


def index_range(page, page_size: int) -> tuple:
    """"""
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
