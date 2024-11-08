#!/usr/bin/env python3
from utils import access_nested_map
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Test case 1
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Test case 2
        ({"a": {"b": 2}}, ("a", "b"), 2),  # Test case 3
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",),),  # Test case 4
        ({"a": 1}, ("a", "b"),)  # Test case 5
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

if __name__ == '__main__':
    unittest.main()
