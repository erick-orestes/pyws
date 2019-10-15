from six.moves import filter

WSDL_NS     = 'http://schemas.xmlsoap.org/wsdl/'
SOAP_NS     = 'http://schemas.xmlsoap.org/wsdl/soap/'
SOAP_ENV_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
XSD_NS      = 'http://www.w3.org/2001/XMLSchema'

def qname(name, ns=None, namespaces=None):
    if not ns:
        return name
    if not namespaces:
        return '{%s}%s' % (ns, name)
    for key, value in namespaces.items():
        if value == ns:
            return '%s:%s' % (key, name)
    #FIXME This raise is to be compliant with the old logic.
    # If there is no match the old code raise IndexError so we are doing the same.
    # In future versions this could improve.
    raise IndexError("There is no match of {} in {}".format(ns, namespaces))

def wsdl_name(name):
    return qname(name, WSDL_NS)

def soap_name(name):
    return qname(name, SOAP_NS)

def soap_env_name(name):
    return qname(name, SOAP_ENV_NS)

def xsd_name(name):
    return qname(name, XSD_NS)

def types_ns(prefix):
    return prefix + 'types/'