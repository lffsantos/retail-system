#!/bin/bash
.PHONY: default
.SILENT:

migrate:
	docker-compose run --rm web python manage.py migrate --noinput

start: migrate
	docker-compose up -d

stop:
	docker-compose down

development:
	docker-compose run --rm --service-ports web python manage.py runserver 0:8000

loaddata:
	docker-compose run --rm web python manage.py loaddata user product


# Code quality
# -----------------------------------------------------------------------------
test:
	docker-compose run --rm web pytest
