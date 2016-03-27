#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

PACKAGES = find_packages()


setup(
    name='letsencrypt-appengine',
    version='1.0',
    description=(
        "A Django app to make letsencrypt SSL certificates easier to create/renew on Google App Engine."
    ),
    author='Adam Alton',
    author_email='adamalton@gmail.com',
    url='https://github.com/adamalton/letsencrypt-appengine',
    packages=PACKAGES,
    include_package_data=True,
    # dependencies
    )
