#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
  name='todoist-cli',
  version='0.0.1',
  description='A CLI for batch creating Todoist tasks.',
  long_description=open('README').read(),
  author='Christopher Su',
  author_email='gh@christopher.su',
  url='https://github.com/csu/todoist-cli',
  packages=find_packages(),
  install_requires=[
    'click==3.3',
    'requests==2.4.3',
    'wsgiref==0.1.2',
  ],
  entry_points={
    'console_scripts': [
      'todoist=todoist_cli.todoist_cli:main'
    ],
  }
)
