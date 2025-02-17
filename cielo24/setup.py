#!/usr/bin/env python

from setuptools import setup
# Script for PyPI

setup(name='cielo24',
      version='1.0.16',
      description='Package for interacting with the cielo24 public REST API',
      author='cielo24',
      author_email='support@cielo24.com',
      url='http://www.cielo24.com',
      packages=['cielo24'],
      install_requires=['enum-compat==0.0.2', 'six==1.10.0'],
      use_2to3=True,
      )
