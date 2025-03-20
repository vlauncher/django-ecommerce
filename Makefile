.PHONY: build up down migrate createsuperuser shell test logs

# Build the Docker images.
build:
	docker-compose build

# Start the containers in detached mode.
up:
	docker-compose up -d

# Stop and remove containers, networks, etc.
down:
	docker-compose down

# Run Django migrations.
migrate:
	docker-compose run --rm web python manage.py migrate

#  Run makemigrations.
makemigrations:
	docker-compose run --rm web python manage.py makemigrations

# Create a new superuser.
createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser

# Open a Django shell.
shell:
	docker-compose run --rm web python manage.py shell

# Run Django tests.
test:
	docker-compose run --rm web python manage.py test

# Stream logs from containers.
logs:
	docker-compose logs -f
