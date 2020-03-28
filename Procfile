release: python manage.py bower_install && python manage.py collectstatic
web: gunicorn tictactoe.wsgi:application
