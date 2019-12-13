# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='jiraya',
    description='Simple Jira Command Line Interface.',
    long_description='Simple Jira Command Line Interface.',
    author='Rodrigo Chacon',
    author_email='rochacon@gmail.com',
    url='https://github.com/rochacon/jiraya',
    license='MIT',
    version='0.1.3',
    install_requires=open('requirements.txt').readlines(),
    scripts=['jiraya'],
)
