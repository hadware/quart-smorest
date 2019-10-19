#!/usr/bin/env python3

from setuptools import setup, find_packages

# Get the long description from the README file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='quart-smorest',
    version='0.1.0',
    description='Quart/Marshmallow-based REST API framework',
    long_description=long_description,
    url='https://github.com/hadware/flask-smorest',
    author='Hadrien Titeux',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Environment :: Web Environment',
        'Framework :: Quart',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=[
        'REST',
        'openapi',
        'swagger',
        'quart',
        'marshmallow',
        'apispec'
        'webargs',
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    package_data={
        '': ['spec/templates/*'],
    },
    python_requires='>=3.5',
    install_requires=[
        'quart>=0.6.5',
        'marshmallow>=2.15.2',
        'webargs>=1.5.2',
        'apispec>=3.0.0',
    ],
)
