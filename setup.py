#!/usr/bin/env python

# Setup script for the `wsgi-statsd' package.
#
# Author: Wouter Lansu <wouter.lansu@paylogic.eu>
# Last Change: January, 6, 2015
import codecs
import sys
from os.path import abspath, dirname, join

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import wsgi_statsd


class ToxTestCommand(TestCommand):

    """Test command which runs tox under the hood."""

    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        """Initialize options and set their defaults."""
        TestCommand.initialize_options(self)
        self.tox_args = '--recreate'

    def finalize_options(self):
        """Add options to the test runner (tox)."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Invoke the test runner (tox)."""
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

# External dependencies.
install_requires = [
    'statsd >= 3.0.1',

]

long_description = []

for text_file in ['README.rst', 'CHANGES.rst']:
    with codecs.open(join(dirname(abspath(__file__)), text_file), encoding='utf-8') as f:
        long_description.append(f.read())


setup(
    name='wsgi-statsd',
    version=wsgi_statsd.__version__,
    description="WSGI middleware for statsd timing",
    long_description=long_description,
    url='https://github.com/paylogic/wsgi-statsd',
    author='Wouter Lansu, Paylogic International and others',
    author_email='developers@paylogic.com',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
    ],
    cmdclass={"test": ToxTestCommand},
    test_require=["tox"]
),
