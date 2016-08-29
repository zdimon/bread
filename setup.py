#!/usr/bin/env python

# ...

from distutils.core import setup


setup(name='grocery',
      version='1.0',
      description='grocery shop`s backend for mobile client',
      author='Zharikov Dmitry',
      author_email='zdimon77@gmail.com',
      url=' http://grocery.pressa.ru/',
      packages=['bread', 'api'],
      license="Public domain",
      install_requires=['django==1.8'],
      platforms=["any"],
     )
