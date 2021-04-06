# Questboard!

## How to start

```bash
# clone the repository and switch to lab directory
$ git clone https://gitlab.discs.ateneo.edu/miggypinaroc/questboard.git && cd questboard/

# create virtualenv
$ virtualenv env && source env/bin/activate

# install dependencies from requirements.txt
$ pip install -r requirements.txt

# create .env file for postgres credentials (check .sample.env)
$ touch questboard/.env

# make migrations and migrate changes
$ python manage.py makemigrations
$ python manage.py migrate

# start the server
$ python manage.py runserver

```