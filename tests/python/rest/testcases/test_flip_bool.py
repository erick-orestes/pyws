import  unittest

from ..client import make_rest_call


class FlipBoolTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(make_rest_call('flip_boolean', b=False), True)
        self.assertEqual(make_rest_call('flip_boolean', b=True), False)
