FROM python:3.12.11-slim

WORKDIR /app

RUN apt update -y && \
    apt install -y libpq-dev libssl-dev libcurl4-openssl-dev gcc pkg-config && \
    rm -rf /var/cache/apt/lists

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv gunicorn && pipenv install --deploy --system

COPY src/ /app/

ENV PORT=8080
ENV WEB_CONCURRENCY=1

EXPOSE ${PORT}
CMD ["gunicorn", "django_project.wsgi:application", "--timeout", "30", "--max-requests", "65536", "--max-requests-jitter", "200", "--access-logfile", "-", "--capture-output"]
