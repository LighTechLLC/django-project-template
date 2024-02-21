migrate:
	DJANGO_SETTINGS_MODULE="django_project.settings" pipenv run python manage.py migrate --fake
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate

test:
	pipenv run python manage.py test

run:
	pipenv run python manage.py runserver

lint:
	pipenv run flake8

shell:
	pipenv run python manage.py shell

runserver:
	pipenv run python manage.py runserver 0.0.0.0:8000

reinstall:
	pipenv --rm && pipenv sync --dev
	pipenv shell
