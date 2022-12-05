clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	rm -rf venv

install:
	sudo apt install python3.10-venv
	python3 -m venv venv
	# source venv/bin/activate
	./venv/bin/pip install -r requirements.txt

makemigrations:
	./venv/bin/python manage.py makemigrations

migrate:
	./venv/bin/python manage.py migrate

run:
	./venv/bin/python manage.py runserver

createsuperuser:
	./venv/bin/python manage.py createsuperuser

all-linux: clean install makemigrations migrate run