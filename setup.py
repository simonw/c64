import os

from setuptools import setup

VERSION = "0.1a0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="c64",
    description="Experimental package of ASGI utilities extracted from Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/c64",
    project_urls={
        "Issues": "https://github.com/simonw/c64/issues",
        "CI": "https://github.com/simonw/c64/actions",
        "Changelog": "https://github.com/simonw/c64/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["c64"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-asyncio", "isort", "black"]},
    tests_require=["c64[test]"],
    python_requires=">=3.6",
)
