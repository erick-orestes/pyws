from functools import wraps
from six import PY2

try:
    from cgi import parse_qs
except ImportError:
    from urllib.parse import parse_qs

try:
    import json
except ImportError:
    import simplejson as json


ENCODING = 'utf-8'


def cache_method_result(attr):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, attr_name):
                setattr(self, attr_name, func(self, *args, **kwargs))
            return getattr(self, attr_name)
        return wrapper
    if callable(attr):
        attr_name = '_cached_' + attr.__name__
        return decorator(attr)
    attr_name = attr
    return decorator


def cached_property(func):
    return property(cache_method_result(func))


class DefaultStrImplemntationMixin(object):

    def __str__(self):
        if PY2:
            return self.__unicode__().encode('utf-8')
        else:
            return self.__unicode__()
