install:
	poetry install

reinstall:
	pip install --user --force-reinstall dist/*.whl

gendiff:
	poetry run gendiff tests/fixtures/json_file1.json tests/fixtures/json_file2.json

help:
	poetry run gendiff -h

build:
	poetry build

check:
	poetry check

coverage:
	poetry run pytest --cov=difference_calculator

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 difference_calculator

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=difference_calculator --cov-report xml
