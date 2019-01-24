#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, Extension

setup(
    name='slacktracker',
    packages=['slacktracker'],
    description='A software for sending DL experiment to slack channel.',
    author='Salih Karagoz',
    author_email='msalihkaragoz@yahoo.com',
    package_dir = {'slacktracker': 'slacktracker'},
    install_requires=[
        'slacker'
    ],
    version='1.0'
)
