# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='jiraya',
    description='Simple Jira Command Line Interface.',
    version='0.1.0',
    install_requires=open('requirements.txt').readlines(),
    scripts=['jiraya'],
)
