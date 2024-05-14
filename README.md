# scenario-manager
Application to manage Open Vet Sim scenario archives.

## Usage
1. Checkout this repo!
    1. git clone https://github.com/ovsscenariomgr/scenario-manager.git
2. Make sure [Docker Desktop](https://docs.docker.com/get-docker/) is installed
3. Copy the [scenario-manager/backend/example.env](/scenario-manager/example.env) file to [scenario-manager/backend/.env](/scenario-manager/.env)
4. Execute the following Docker commands:
    ```shell
    docker compose build
    docker compose up -d --wait
    ```
5. Open http://localhost:8000/admin/ in your browser
    1. login with credentials:
        1. username: test
        2. password: test

## Tests
1. From backend dir:
    * coverage run --source='.' manage.py test && coverage html

## `OvsXMLRenderer` export notes 
1. `<profile>`
    1. `<avatar>`
        1. `filename` property is truncated to file path basename
    2. `<summary>`
        1. `image` property is truncated to file path basename
2. `<vocals>` and `<media>` stored as `<vocalfiles>` and `<mediafiles>` respectively
    1. `<vocalfile>` and `<mediafile>` singular are converted to just `<file>`
    1. `filename` property is truncated to file path basename
3. `<events>`
    1. Stored as `<eventgroups>` in database
    2. `<eventgroup>` is converted to `<category>`
    3. `<eventgroup>/<category>` child `<events>` tag is removed and only `<event>`s rendered
4. `<scenes>` parent tag is removed and only `<scene>`s are rendered.