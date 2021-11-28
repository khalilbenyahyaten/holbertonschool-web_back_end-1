#!/usr/bin/env python3
"""
a Unit test
"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, memoize, get_json
from parameterized import parameterized

import sys
import types
import os


class TestAccessNestedMap(unittest.TestCase):
    """testing test_utils from utils"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map, path, expected):
        """"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self, nested_map, path):
        """tests if a KeyError"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(error.exception, KeyError)


class TestGetJson(unittest.TestCase):
    """class testing utils"""
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})
                           ])
    def test_get_json(self, url, payload):
        """tests"""
        mock = Mock()
        mock.json.return_value = payload
        with patch('requests.get', return_value=mock):
            actual_result = get_json(url)
            self.assertEqual(actual_result, payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """class testing utils"""

    def test_memoize(self):
        """test"""
        class TestClass:
            """test class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as a_method:
            test = TestClass()
            test.a_property
            result = test.a_property
            self.assertEqual(result, test.a_property)
            a_method.assert_called_once()
