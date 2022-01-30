VERSION := $(shell python -c 'import doomsdaytutor as dt; print(dt.__version__)')

build: cleanup
	python -m build
	python -c 'print("-" * 80)'
	twine check dist/*
test-deploy: pypi-pkg
	twine upload --repository testpypi --skip-existing dist/*
cleanup:
	rm -rf dist
	rm -rf doomsdaytutor.egg-info
test-env: cleanup-test-env
	virtualenv venv
test-install:
	pip install -i https://test.pypi.org/simple/ doomsdaytutor==$(VERSION) --extra-index-url https://pypi.org/simple/
cleanup-test-env:
	rm -rf venv