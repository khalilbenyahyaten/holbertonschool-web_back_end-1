#!/usr/bin/env python3
"""
Create Cache
"""
import redis
from uuid import uuid4
from typing import Callable


class Cache:
    """redis cache class"""

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

    def get(self, key: str, fn: callable = None):
        """recovering original type"""
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str, data: bytes) -> str:
        """parametrize Cache.get with the correct conversion function"""
        return self.get(key, str)

    def get_int(self, key: str, data: bytes) -> int:
        """parametrize Cache.get with the correct conversion function"""
        return self.get(key, int)
