#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['djangorestframework>=3.10']

setup_requirements = ['pytest-runner', 'djangorestframework>=3.10']

test_requirements = ['pytest>=3', 'djangorestframework>=3.10']

setup(
    author="Denis Ivlev",
    author_email='me@dierz.pro',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Django Rest Framework pretty exception handler",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='drf_pretty_exception_handler',
    name='drf_pretty_exception_handler',
    packages=find_packages(include=['drf_pretty_exception_handler', 'drf_pretty_exception_handler.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ivlevdenis/drf_pretty_exception_handler',
    version='0.1.1',
    zip_safe=False,
)
