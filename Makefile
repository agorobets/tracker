all: activate install run

.PHONY: install
install:
	. venv/bin/activate && \
	pip install -r requirements.txt

.PHONY: run
run:
	PYTHONPATH=$(shell pwd)/src gunicorn --workers 3 -b 0.0.0.0:80 wsgi:app

.PHONY: rundev
rundev:
	PYTHONPATH=$(shell pwd)/src flask --app main run

