#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
  name='todoist-cli',
  version='0.0.2',
  description='A CLI for batch creating Todoist tasks.',
  long_description=open('README').read(),
  author='Christopher Su',
  author_email='gh@christopher.su',
  url='https://github.com/csu/todoist-cli',
  packages=find_packages(),
  install_requires=[
    'certifi==2017.11.5',
    'chardet==3.0.4',
    'click==6.7',
    'idna==2.6',
    'requests==2.20.0',
    'urllib3==1.26.5',
  ],
  entry_points={
    'console_scripts': [
      'todoist=todoist_cli.todoist_cli:main'
    ],
  }
)
