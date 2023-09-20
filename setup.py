"""
This module contains the setup script for the Cogniezer-Backend package.

The setup script includes metadata such as the package name, version, author, description, and more.
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Cogniezer-Backend"
AUTHOR_USER_NAME = "InsiderCloud"
SRC_REPO = "Cogniezer"
AUTHOR_EMAIL = "madushakv@live.com"

def setup_package():
    """
    Set up the package with the required metadata.
    """
    setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="A small python package for NLP app",
        long_description=long_description,
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        },
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src")
    )

