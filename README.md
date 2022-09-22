# README

branch:

- project-init-state:
  - api and web services are setup without dependencies installed.
  - to install dependencies, run following commands:
    ```
        docker-compose run --rm web npm install
        docker-compose run --rm api poetry install
    ```
  - then, add
    - `command: ["npm", "run", "dev"]`
      to web service in docker-compose.yml
    - ```
        command: ["uvicorn", "main:router", "--reload", "--host=0.0.0.0"]
        entrypoint: ['poetry', 'run']
      ```
      to api servce in docker-compose .yml
- api-setup:
  - api is setup with dependencies, connected to database with a User table, and API connection to the User table.
