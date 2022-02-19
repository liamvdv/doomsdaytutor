VERSION := $(shell python -c 'import doomsdaytutor as dt; print(dt.__version__)')

build: cleanup
	python -m build
	python -c 'print("-" * 80)'
	twine check dist/*
deploy: 
	twine upload dist/*
test-local-install:
	pip install ./dist/doomsdaytutor-$(VERSION).tar.gz
test-deploy: pypi-pkg
	twine upload --repository testpypi --skip-existing dist/*
test-install:
	pip install -i https://test.pypi.org/simple/ doomsdaytutor==$(VERSION) --extra-index-url https://pypi.org/simple/
cleanup:
	rm -rf dist
	rm -rf doomsdaytutor.egg-info
venv: cleanup-venv
	virtualenv venv
cleanup-venv:
	rm -rf venv