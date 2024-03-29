# Self-Documented Makefile see https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"
PART 	:= minor

# Put it first so that "make" without argument is like "make help".
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-32s-\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

guard-%: ## Checks that env var is set else exits with non 0 mainly used in CI;
	@if [ -z '${${*}}' ]; then echo 'Environment variable $* not set' && exit 1; fi

# --------------------------------------------------------
# ------- Python package (pip) management commands -------
# --------------------------------------------------------

clean: clean-build clean-pyc clean-test  ## remove all build, test, coverage and Python artifacts

clean-build:  ## remove build artifacts
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-pyc:  ## remove Python file artifacts
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:  ## remove test and coverage artifacts
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache

lint:  ## check style with flake8
	@flake8 restricted_fields tests

test:  ## run tests quickly with the default Python
	@pytest

tox: install-test  ## Run tox test
	@tox

coverage:  ## check code coverage quickly with the default Python
	@coverage run --source restricted_fields -m pytest
	@coverage report -m
	@coverage html
	@$(BROWSER) htmlcov/index.html

docs: install-docs  ## generate Sphinx HTML documentation, including API docs
	@rm -f docs/drf_restricted_fields.rst
	@rm -f docs/modules.rst
	@sphinx-apidoc -o docs/ restricted_fields
	@$(MAKE) -C docs clean
	@$(MAKE) -C docs html
	@$(BROWSER) docs/_build/html/index.html

servedocs: docs  ## compile the docs watching for changes
	@watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D restricted_fields docs

release: dist  ## package and upload a release
	@twine upload --verbose dist/*

dist: clean install-deploy  ## builds source and wheel package
	@python setup.py sdist
	@python setup.py bdist_wheel
	@ls -l dist

upload-to-pypi:  ## Builds source and wheel package deploy to PyPi
	@pip install -U twine
	@python setup.py sdist bdist_wheel
	@twine upload dist/*

increase-version: guard-PART  ## Increase project version
	@bump2version $(PART)
	@git push
	@git push --tags

install: clean requirements.txt  ## install the package to the active Python's site-packages
	@pip install -r requirements.txt

install-dev: clean requirements_dev.txt  ## Install local dev packages
	@pip install -e .'[development]' -r requirements_dev.txt

install-docs: clean
	@pip install -e .'[docs]'

install-test: clean
	@pip install -e .'[test]'

install-lint: clean
	@pip install -e .'[lint]'

install-deploy: clean
	@pip install -e .'[deploy]'

.PHONY: clean clean-test clean-pyc clean-build docs help install-docs install-dev install install-lint install-test install-deploy
