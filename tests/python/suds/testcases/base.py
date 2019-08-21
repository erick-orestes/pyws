import os
import suds

directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
wsdl_path = directory + '/test.wsdl'

def build_client():
    return suds.client.Client('file://%s' % wsdl_path, cache=None)


class BaseTestCaseMixin(object):

    def setUp(self):
        client = build_client()
        self.client = client
        self.service = client.service
        self.factory = client.factory
