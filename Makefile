migrate:
	pipenv run python src/manage.py migrate --fake
	pipenv run python src/manage.py makemigrations
	pipenv run python src/manage.py migrate

test:
	pipenv run python src/manage.py test

run:
	pipenv run python src/manage.py runserver

lint:
	pipenv run black src/
	pipenv run isort src/
	pipenv run flake8 src/

shell:
	pipenv run python src/manage.py shell

runserver:
	pipenv run python src/manage.py runserver 0.0.0.0:8000

reinstall:
	pipenv --rm && pipenv sync --dev
