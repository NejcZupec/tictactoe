release: python manage.py bower_install && python manage.py collectstatic --noinput
web: gunicorn tictactoe.wsgi:application
