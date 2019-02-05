import os
from setuptools import setup

setup(
    name = "chesstester",
    version = "0.0.1",
    author = "Bendik Samseth",
    author_email = "b.samseth@gmail.com",
    description = "A simple interface to play chess engines against each other, including tournaments.",
    license = "MIT",
    keywords = "chess engine testing match tournament",
    url = "https://www.github.com/bsamseth/python-chess-engine-tester",
    packages=['chesstester'],
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
