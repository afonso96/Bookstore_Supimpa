release: python3 manage.py migrate
web: gunicorn BookStore.book.book.wsgi --preload --log-file -