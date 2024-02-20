#!/usr/bin/env zsh
source ${HOME}/.zshrc

__dir="$(cd "$(dirname "${(%):-%x}")" && pwd -P)"
__root="$(cd "$(dirname "${__dir}")" && pwd -P)"
__backend="$(cd "${__root}/backend" && pwd -P)"

cd ${__backend}

# Nuke migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Nuke db
rm -f db.sqlite3

# Recreate
micromamba activate ovs
python manage.py makemigrations app
python manage.py migrate

DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_EMAIL=dh749@cornell.edu python manage.py createsuperuser --noinput