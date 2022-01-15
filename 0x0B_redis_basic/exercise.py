#!/usr/bin/env python3
""" Basic Redis

"""

from typing import Union, Callable
from uuid import uuid4
from functools import wraps
import redis


def replay(method: Callable):
    """ Display the history of calls of method """
    qualname = method.__qualname__
    nb_calls = method.__self__._redis.llen(qualname + ":inputs")
    inputs = method.__self__._redis.lrange(qualname + ":inputs", 0, -1)
    outputs = method.__self__._redis.lrange(qualname + ":outputs", 0, -1)

    print(f'{qualname} was called {nb_calls} times:')

    for input, output in zip(inputs, outputs):
        print(f'{qualname}(*{input.decode("utf-8")})' +
              f' -> {output.decode("utf-8")}')


def call_history(method: Callable) -> Callable:
    """ Save call history
    """
    @wraps(method)
    def history(*args, **kwds):
        """ Save the input and the output
            of method call history
        """
        args[0]._redis.rpush(method.__qualname__ + ":inputs", str(args))
        output = method(*args, **kwds)
        args[0]._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return history


def count_calls(method: Callable) -> Callable:
    """ Count method calls
    """
    @wraps(method)
    def incr(*args, **kwds):
        """ Increments method call counter """
        args[0]._redis.incr(method.__qualname__)
        return method(*args, **kwds)

    return incr


class Cache:
    """ Caching class
    """
    def __init__(self):
        """ Instantiation """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """ Get data from Redis """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """ Get string data from Redis """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Get int data from Redis """
        return self.get(key, int)
