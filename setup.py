#!/usr/bin/env python

from setuptools import setup

import re
import sys

# load our version from our init file
init_data = open('stackstrap/__init__.py').read()
matches = re.search(r"__version__ = '([^']+)'", init_data, re.M)
if matches:
    version = matches.group(1)
else:
    raise RuntimeError("Unable to load version")

requirements=[
    'PyYAML==3.11',
    'Jinja2>=2.7,<2.8',
    'sh>=1.09'
]
if sys.version_info < (2, 7):
    requirements.append('argparse')

setup(
    name='stackstrap',
    packages=['stackstrap'],
    scripts=['scripts/stackstrap', 'scripts/loose_ssh.sh'],
    include_package_data=True,
    version=version,
    license="Apache License, Version 2.0",
    description='A tool that uses vagrant + salt to make development more awesome',
    long_description=open('README.md').read(),
    author='Evan Borgstrom',
    author_email='evan@borgstrom.ca',
    url='https://github.com/stackstrap/stackstrap',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=requirements
)
