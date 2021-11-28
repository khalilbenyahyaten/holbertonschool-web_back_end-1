#!/usr/bin/env python3
"""More unittests"""
import unittest
from unittest import mock
from unittest.mock import Mock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """tests class"""
    @parameterized.expand([("google", {"payload": True}),
                           ("abc", {"payload": False})])
    @patch('client.get_json')
    def test_org(self, patch, test, test_payload):
        """tests 'org' class"""
        patch.return_value = test_payload
        client = GithubOrgClient(test)
        self.assertEqual(client.org, test_payload)
        patch.assert_called_once()

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, patch):
        """ Tests '_public_repos_url' class method that
        has been turned into a property by 'memoize' """
        patch.return_value = {"repos_url": "test_value"}
        client = GithubOrgClient('abc')
        result = client._public_repos_url
        self.assertEqual(result, "test_value")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, patch):
        """ Tests '_public_repos_url' class method that
        has been turned into a property by 'memoize' """
        patch.return_value = {"repos_url": "test_value"}
        client = GithubOrgClient('abc')
        result = client._public_repos_url
        self.assertEqual(result, "test_value")

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True),
                           ({"license": {"key": "other_license"}},
                            "my_license", False)])
