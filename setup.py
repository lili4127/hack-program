#!/usr/bin/env python

from setuptools import setup

setup(
    name="mymodule",
    version="0.0.1",
    packages=[],
    entry_points={
        'console_scripts': ['mymodule = mymodule.__main__:main']
    }
)
