#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='insights_data',
    version='0.1.0',
    description="Python module to use in querying Insights data from the LMS.",
    long_description=readme + '\n\n' + history,
    author="Julia Eskew",
    author_email='jeskew@edx.org',
    url='https://github.com/doctoryes/insights_data',
    packages=find_packages(),
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='insights_data',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
