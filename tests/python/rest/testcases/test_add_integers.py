import unittest

from ..client import make_rest_call


class AddIntegersTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(make_rest_call('add_integers', a=100, b=50), 150)
