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

## Running Backend/Frontend Separately (outside Docker)
Useful for local development/debugging without rebuilding the Docker stack.

### VS Code
`.vscode/launch.json` has run configs for both — open the Run and Debug panel (`Cmd+Shift+D`) and pick one:
* **Python Debugger: Django** — runs `manage.py runserver` with the debugger attached.
* **NPM Run Client DevServer** — runs `npm run dev` in `frontend/`.

Start both to run the full stack locally, or just one to iterate on a single side.

### Command line
* Backend (from `backend/`, with a Python 3.12 virtualenv and `requirements.txt` installed):
    ```shell
    cp example.env .env    # if not already done
    python manage.py migrate
    python manage.py runserver
    ```
* Frontend (from `frontend/`):
    ```shell
    npm install
    npm run dev
    ```
    Reads the `BACKEND_URL` env var for the API base URL (defaults to `http://localhost:8000`).

## Tests
1. From backend dir:
    * coverage run --source='.' manage.py test && coverage html

## Linting
1. `ruff check ./backend`

## Types Generation
1. `cd backend; ./manage.py spectacular --file ./schema.json --format openapi-json --api-version v1`
2. `cd frontend; npx openapi-typescript-codegen --input ~/tmp/schema.json --output ./src/types`

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