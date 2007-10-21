# -*- coding: utf-8 -*-
import werkzeug
import os
import ez_setup
from inspect import getdoc
ez_setup.use_setuptools()

from setuptools import setup, Extension, Feature

setup(
    name = 'Werkzeug',
    version = '0.1',
    url = 'http://werkzeug.pocoo.org/',
    download_url = 'http://trac.pocoo.org/repos/werkzeug/trunk',
    license = 'BSD',
    author = 'Armin Ronacher',
    author_email = 'armin.ronacher@active-4.com',
    description = 'WSGI Utility Collection -- formal successor of Colubrid',
    long_description = getdoc(werkzeug),
    zip_safe = False,
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    scripts = ['werkzeug-bootstrap'],
    packages = ['werkzeug', 'werkzeug.debug'],
    platforms = 'any',
    include_package_data = True,
    extras_require = {
        'plugin': ['setuptools>=0.6a2'],
        'wsgiref': ['wsgiref']
    }
)