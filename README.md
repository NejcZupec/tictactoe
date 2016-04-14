# tictactoe #
Another Implementation of Tic Tac Toe in Python.

[![Codacy Badge](https://api.codacy.com/project/badge/grade/cc1640aff75340d89efee0137c1bc0ec)](https://www.codacy.com/app/zupecnejc_3396/tictactoe)
[![Codacy Badge](https://api.codacy.com/project/badge/coverage/cc1640aff75340d89efee0137c1bc0ec)](https://www.codacy.com/app/zupecnejc_3396/tictactoe)


## Development environment ##
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