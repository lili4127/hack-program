
"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="mymodule",
    version="0.0.1",
    author="Lior Tal",
    author_email="ljt2136@columbia.edu",
    license="GPLv3",
    description="A package for playing rock paper scissors",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["mymodule = mypackage.__main__:main"]
    },
)
