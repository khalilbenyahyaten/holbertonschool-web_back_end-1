#!/usr/bin/env python3
"""
a Unit test
"""
import unittest
from utils import access_nested_map, memoize, get_json
from parameterized import parameterized

import sys, types, os


class TestAccessNestedMap(unittest.TestCase):
    """testing test_utils from utils"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map, path, expected):
        """"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
