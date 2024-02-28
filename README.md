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