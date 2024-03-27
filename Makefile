migrate:
	pipenv run python src/manage.py migrate --fake
	pipenv run python src/manage.py makemigrations
	pipenv run python src/manage.py migrate

test:
	pipenv run python src/manage.py test

run:
	pipenv run python src/manage.py runserver 0:8000

lint:
	pipenv run black src/
	pipenv run isort src/
	pipenv run flake8 src/

shell:
	pipenv run python src/manage.py shell

reinstall:
	pipenv --rm && pipenv sync --dev
