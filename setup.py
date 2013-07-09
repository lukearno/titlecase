import os
import sys

from setuptools import setup, find_packages

with open('README') as readme:
    README = readme.read()

setup(name='titlecase',
    version='99.9.9',
    description="Python Port of John Gruber's titlecase.pl",
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Text Processing :: Filters",
    ],
    keywords='string formatting',
    author="Stuart Colville",
    author_email="pypi@muffinresearch.co.uk",
    url="http://muffinresearch.co.uk/",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    tests_require=['nose'],
    test_suite="titlecase.tests")

