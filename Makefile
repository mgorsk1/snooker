.PHONY: setup_dev
setup_dev:
	pip3 install -r requirements.txt
	pip3 install -r requirements-dev.txt

.PHONY: clean
clean:
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete
	rm -frd .*_cache/
	rm -rf dist/
	rm -rf build/
	rm -frd *.egg-info

.PHONY: test_unit
test_unit:
	python3 -b -m pytest tests

lint:
	python3 -m flake8

.PHONY: mypy
mypy:
	mypy --ignore-missing-imports --follow-imports=skip --strict-optional --warn-no-return .

.PHONY: isort
isort:
	isort .

.PHONY: isort_check
isort_check:
	isort ./ --check --diff

.PHONY: test
test: clean test_unit lint mypy isort_check

.PHONY: build
build:
	python3 -m pip install --upgrade build
	python3 -m build --sdist --wheel --outdir dist/
