#!/usr/bin/env python3

""" Setup file for pytemplate package.
"""
import sys

from setuptools import setup, find_packages
from pkg_resources import VersionConflict, require

import coffee

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":
    setup(
        name=coffee.__title__,
        version=coffee.__version__,
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        packages=find_packages(exclude=["tests"]),
        install_requires=[
            "certifi==2020.6.20",
            "chardet==3.0.4",
            "click==7.1.2",
            "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "requests==2.24.0",
            "urllib3==1.25.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
        ],
        include_package_data=True,
        zip_safe=False,
        # Uncomment if needed
        # entry_points={"console_scripts": ["pytemplate=pytemplate.__main__:main"]},
        author=coffee.__author__,
        author_email=coffee.__author_email__,
        description=coffee.__description__,
        license=coffee.__license__,
        keywords=coffee.__keywords__,
        url=coffee.__url__,
        project_urls=coffee.__project_urls__,
    )
