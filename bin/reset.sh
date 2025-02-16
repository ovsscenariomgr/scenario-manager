#!/usr/bin/env zsh
source ${HOME}/.zshrc
source ${HOME}/.zlogin

__dir="$(cd "$(dirname "${(%):-%x}")" && pwd -P)"
__root="$(cd "$(dirname "${__dir}")" && pwd -P)"
__backend="$(cd "${__root}/backend" && pwd -P)"
__frontend="$(cd "${__root}/frontend" && pwd -P)"

cd ${__backend}

# Nuke migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Nuke db.
rm -f ./data/*

# Recreate
micromamba activate ovs
pip install -r requirements.txt
python manage.py makemigrations app --noinput
python manage.py migrate --noinput
python manage.py loaddata users
python manage.py collectstatic --noinput

# Generate schema and types
python manage.py spectacular --file ./openapi-schema.json --format openapi-json --api-version v1

cd ${__frontend}
nvm use
npx openapi-typescript-codegen \
    --input ${__backend}/openapi-schema.json \
    --exportCore false \
    --exportServices false \
    --exportModels true \
    --indent 2 \
    -o ${__frontend}/src/types