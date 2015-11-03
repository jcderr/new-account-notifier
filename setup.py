#!/usr/bin/env python

from setuptools import setup, find_packages
from acctnotify import version

setup(name='new_account_notifier',
      version=version,
      description='Notify Users of New Accounts',
      author='Jeremy Derr',
      author_email='jeremy@derr.me',
      url='http://github.com/jcderr/new-account-notifier',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'nanotify= acctnotify.cli:notify_user',
          ]
      }
      )
