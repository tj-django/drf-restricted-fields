#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

deploy_requires = [
    "bump2version",
    "readme_renderer[md]",
    "changes",
    "git-changelog",
    "twine",
    "wheel",
]

docs_requires = [
    "watchdog[watchmedo]",
    "Sphinx",
]

install_requires = [
    "django",
    "djangorestframework",
]

test_requires = [
    "pytest>=3",
    "tox",
    "tox-gh-actions",
    "coverage",
    "codacy-coverage",
]

lint_requires = [
    "flake8",
    "yamllint",
    "isort",
    "black",
    "mypy",
]

extras_require = {
    "development": [
        install_requires,
        deploy_requires,
        test_requires,
        lint_requires,
    ],
    "test": test_requires,
    "lint": lint_requires,
    "deploy": deploy_requires,
    "docs": docs_requires,
}

setup(
    author="Tonye Jack",
    author_email="jtonye@ymail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Restrict fields returned by DRF serializers",
    install_requires=install_requires,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=False,
    keywords=["drf_restricted_fields", "restricted_fields"],
    name="drf_restricted_fields",
    packages=find_packages(include=["restricted_fields", "restricted_fields.*"]),
    test_suite="tests",
    tests_require=test_requires,
    extras_require=extras_require,
    url="https://github.com/tj-django/drf-restricted-fields",
    version="0.0.1",
    zip_safe=False,
)
