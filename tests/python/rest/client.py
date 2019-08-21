from pyws.utils import json

from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError


def encode_arg(xxx_todo_changeme):
    (name, value) = xxx_todo_changeme
    if isinstance(value, (list, tuple)):
        return '&'.join(urlencode({name: element}) for element in value)
    return urlencode({name: value})


def encode_args(args):
    return '&'.join(map(encode_arg, iter(args.items())))


def make_rest_call(func, headers=None, **args):
    request = Request(
        'http://127.0.0.1:8000/api/rest/%s?%s' % (func, encode_args(args)),
        headers=headers or {},
    )
    try:
        return json.loads(urlopen(request).read())['result']
    except HTTPError as e:
        raise Exception(json.loads(e.read())['error']['message'])
