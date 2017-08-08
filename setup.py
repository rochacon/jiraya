# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='jiraya',
    description='Simple Jira Command Line Interface.',
    version='0.1.1',
    install_require=open('requirements.txt').readlines(),
    scripts=['jiraya'],
)
