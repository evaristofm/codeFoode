install:
	pip install -e .['dev']

test:
	FLASK_ENV=test pytest tests -v

run:
	FLASK_APP=delivery/app.py FLASK_ENV=development flask run