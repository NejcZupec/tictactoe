# tictactoe #
Another Implementation of Tic Tac Toe in Python.

[![Codacy Badge](https://api.codacy.com/project/badge/grade/cc1640aff75340d89efee0137c1bc0ec)](https://www.codacy.com/app/zupecnejc_3396/tictactoe)
[![Codacy Badge](https://api.codacy.com/project/badge/coverage/cc1640aff75340d89efee0137c1bc0ec)](https://www.codacy.com/app/zupecnejc_3396/tictactoe)

## Requirements

- python 2.7 + dependencies listed in `requirements.txt`
- [pyenv](https://github.com/pyenv/pyenv)
- npm and bower

## Development environment (pyenv and npm) ##

Set up Python environment and install dependencies

    pyenv virtualenv 2.7 tictactoe
    pyenv local tictactoe
    pip install -r requirements.txt

Install frontend dependencies:

    npm install -g bower
    python manage.py bower_install

Run migrations:

    python manage.py migrate
    
Run development server:

    python manage.py runserver


## Development environment (Vagrant) ##
To setup a development environment for the `tictactoe` project, install the following dependencies:

* Ansible (https://www.ansible.com/)
* VirtualBox (https://www.virtualbox.org/)
* Vagrant (https://www.vagrantup.com/)

Clone the project from Github and run the following commands:

    vagrant up
    vagrant provision  # not mandatory
    vagrant ssh
    cd tictactoe
    python manage.py runserver 0.0.0.0:8000

Open a browser on your local machine and go to: http://127.0.0.1:8080/
