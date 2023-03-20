install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck #lint

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/