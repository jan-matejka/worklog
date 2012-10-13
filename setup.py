#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import worklog

import sys
from os.path import expanduser, join

def get_usrdir():
    if '--user' in sys.argv:
        # FIXME
        return expanduser("~/.local")
    return '/usr'

setup(
    name='worklog',
    version=worklog.__version__,
    description='WorkLog',
    author='Jan Matejka',
    author_email='yac@blesmrt.net',
    url='https://github.com/yaccz/worklog',

    packages = find_packages(
        where = '.'
    ),

    install_requires = [
        "cement", # aliases will need probably like >1.9.12 which hasnt been released yet
        "setuptools",
        "sqlalchemy",
        "pyxdg",
        "pysqlite",
    ],

    entry_points = {
        'console_scripts': ['wl = worklog.core:main']},

    data_files = [
        (join(get_usrdir(), 'lib', 'worklog', 'git-hooks'), ['git-hooks/prepare-commit-msg'])
    ]
)
