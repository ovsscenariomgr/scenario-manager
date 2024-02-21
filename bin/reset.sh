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
python manage.py makemigrations app --noinput
python manage.py migrate --noinput
python manage.py loaddata app/fixtures/users.json
python manage.py collectstatic --noinput