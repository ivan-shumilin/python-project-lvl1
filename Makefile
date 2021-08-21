install:
		poetry install

brain-games:
		poetry run brain-games

brain-even:
		poetry run brain-even	

brain-calc:
		poetry run brain-calc		

build:
		poetry build

lint:
		poetry run flake8 brain_games	

publish:
		poetry publish --dry-run	

package-install:
		python3.7 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build