pep8:
	flake8 sluggable --ignore=E501,E127,E128,E124

test:
	coverage run --branch --source=pure_pagination manage.py test pure_pagination
	coverage report --omit=pure_pagination/test*
