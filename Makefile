#!/bin/bash
.PHONY: default
.SILENT:

migrate:
	docker-compose run --rm base-service python manage.py migrate --noinput

start: migrate
	docker-compose up -d

build:
	docker-compose up -d --build
	docker-compose run --rm base-service python manage.py migrate --noinput

stop:
	docker-compose down

development:
	docker-compose run --rm --service-ports web python manage.py runserver 0:8000

loaddata:
	docker-compose run --rm base-service python manage.py loaddata user product
