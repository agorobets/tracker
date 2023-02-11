all: activate install run

.PHONY: install
install:
	. venv/bin/activate && \
	pip install -r requirements.txt

.PHONY: run
run:
	PYTHONPATH=$(shell pwd)/src gunicorn -c src/core/gunicorn.py main:app

.PHONY: rundev
rundev:
	PYTHONPATH=$(shell pwd)/src

