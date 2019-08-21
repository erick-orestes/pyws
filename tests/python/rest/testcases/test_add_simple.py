import unittest

from ..client import make_rest_call


class AddSimpleTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            make_rest_call('add_simple', a='hello', b=' world'), 'hello world')
