install:
	poetry install

reinstall:
	pip install --user --force-reinstall dist/*.whl

gend:
	poetry run gendiff -h

build:
	poetry build

coverage:
	poetry run pytest --cov=project_difference_calculator

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 difference_calculator

test:
	poetry run pytest
