build:
	make build-docker
	make manage-migrate
	make manage-createsuperuser
	make manage-filldb
	
build-docker:
	docker-compose build

run:
	docker-compose up

manage-python:
	docker-compose run --rm web python manage.py $(command)

manage-migrate: command=migrate
manage-migrate: manage-python

manage-createsuperuser: command=makesuperuser
manage-createsuperuser: manage-python

manage-filldb: command=fill_db
manage-filldb: manage-python

