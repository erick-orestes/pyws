#!/usr/bin/env python

import sys
import os
sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from setuptools import setup
from setuptools import find_packages

import pyws

short_description = 'Python SOAP server providing WSDL'
long_description = \
    '''
    Pyws is a project, which purpuse is to help developers to expose some
    functions of their systems as public APIs via SOAP with WSDL description.
    The main idea is to let developers completely forget about SOAP itself and
    make creating of APIs fast and painless.
    '''

extra_requires = []
minor_version = sys.version_info[1]
major_version = sys.version_info[0]
if major_version < 3 and minor_version < 7:
    raise Exception('pyws works only on python >= 2.7')
find_pack = find_packages('src')
if 'develop' in sys.argv:
    if major_version < 3:
        extra_requires += ['suds']
        find_pack = find_packages()
    else:
        extra_requires += ['suds-py3']
setup(
    name='pyws',
    version=pyws.VERSION,
    package_dir={'': 'src'},
    packages=find_pack,
    description=short_description,
    long_description=long_description,
    keywords=['soap', 'wsdl', 'server', 'xml', 'json', 'web services'],
    author='Stepan N. Kornyakov',
    author_email='stepankk@gmail.com',
    url='https://github.com/stepank/pyws',
    license='MIT',
    platforms=['Any'],
    install_requires=['lxml', 'six'] + extra_requires,
)
