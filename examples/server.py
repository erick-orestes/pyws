from pyws.server import SoapServer

from . import api_settings

# Create a server
server = SoapServer(api_settings, *api_settings.SOAP_PROTOCOL_PARAMS)

# Just import the example module to register all its functions
#noinspection PyUnresolvedReferences
from . import functions
