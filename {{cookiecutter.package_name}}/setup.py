#!/usr/bin/env python

import setuptools

with open('README.rst', 'r') as fh:
    README = fh.read()

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

NAME = '{{ cookiecutter.package_name }}'
DESCRIPTION = '{{ cookiecutter.package_short_description }}'
URL = 'https://github.com/{{ cookiecutter.github_user_name }}/{{ cookiecutter.github_repo_name }}'
AUTHOR = '{{ cookiecutter.author }}'
AUTHOR_EMAIL = '{{ cookiecutter.email }}'
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]
PROJECT_URLS = {
    'Bug Reports': URL + '/issues',
    'Documentation': 'https://{{ cookiecutter.package_name }}.readthedocs.io',
    'Source Code': URL,
}
REQUIRES_PYTHON = '>=3.5, <4'
EXTRAS_REQUIRE = {}
KEYWORDS = '{{ cookiecutter.package_name }}',
LICENSE = '{{ cookiecutter.open_source_license }}'
TEST_SUITE = 'tests'
REQUIREMENTS = []
SETUP_REQUIREMENTS = []
TEST_REQUIREMENTS = ['pytest', 'pytest-cov']
VERSION = '{{ cookiecutter.version }}'


setuptools.setup(
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    classifiers = CLASSIFIERS,
    description = DESCRIPTION,
    extras_require = EXTRAS_REQUIRE,
    include_package_data = False,
    install_requires = REQUIREMENTS,
    keywords = KEYWORDS,
    license = LICENSE,
    long_description = README,
    name = NAME,
    package_data={},
    packages = setuptools.find_packages(),
    project_urls = PROJECT_URLS,
    python_requires = REQUIRES_PYTHON,
    setup_requires = SETUP_REQUIREMENTS,
    test_suite = TEST_SUITE,
    tests_require = TEST_REQUIREMENTS,
    url = URL,
    # version = VERSION,
    zip_safe = False,
)
