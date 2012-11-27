#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import worklog
from worklog import git_hooks_dir
import sys

if not '--user' in sys.argv:
    raise RuntimeError('Installing without --user is not supported')
    # FIXME: githooks installer needs to know where to take the
    # prepare-commit-msg hook from

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
        "cement",
        "setuptools",
        "sqlalchemy",
        "pyxdg",
        "pysqlite",
        "alembic",
    ],

    entry_points = {
        'console_scripts': ['wl = worklog.core:main']},

    data_files = [
        (git_hooks_dir, ['git-hooks/prepare-commit-msg'])
    ]
)
