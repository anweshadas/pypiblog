#!/usr/bin/env python3
"""Test project"""
from setuptools import find_packages, setup



setup(name = 'xyztest',
    version = '0.1',
    description = "Test project for PyPI upload",
    long_description = "Test project for PyPI upload",
    platforms = ["Linux"],
    author="Anwesha Das",
    author_email="anwesha@das.community",
    url="",
    license = "MIT",
    packages=find_packages()
)