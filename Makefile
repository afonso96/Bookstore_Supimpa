install: @pip install -r requirements.txt

test: python ./book/manage.py test
