#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals

import sys

PY3 = sys.version_info >= (3, 0)

for cmd in ('egg_info', 'develop'):

    if cmd in sys.argv:
        from setuptools import setup

if not PY3:
    reload(sys).setdefaultencoding("UTF-8")


description = 'Приложение для интеграции платежной системы ROBOKASSA в проекты на Django.'
long_description = open('README.rst').read() + "\n\n" + open('CHANGES.rst').read()


setup(
    name='django-robokassa',
    version='1.2',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['robokassa', 'robokassa.migrations'],

    url='https://bitbucket.org/kmike/django-robokassa/',
    license='MIT license',
    description=description if PY3 else description.encode('utf8'),
    long_description=long_description if PY3 else long_description.decode('utf8'),

    install_requires=['Django>=1.7,<1.9'],

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
