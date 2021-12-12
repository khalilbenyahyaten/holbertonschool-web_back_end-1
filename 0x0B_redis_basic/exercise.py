#!/usr/bin/env python3
"""
Create Cache
"""
import redis
from uuid import uuid4


class Cache:
    def __init__(self):
        """stores a private instance of redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """returns a string"""
        random_key = uuid4()
        random_key = str(random_key)
        self._redis.mset({random_key: data})
        return random_key
