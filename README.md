# README

branch:

- project-init-state:

  - api and web services are setup without dependencies installed.
  - to install dependencies, run following commands:
    - for api:
      ```
        docker-compose run --rm api bash
        poetry install
      ```
    - for web:
      ```
        docker-compose run --rm web npm install
      ```
  - then, add
    - `command: ["npm", "run", "dev"]` to web service in docker-compose.yml
    - `command: ["uvicorn", "main:router", "--reload", "--host=0.0.0.0"]` to api servce in docker-compose .yml
  - and, replace `entrypoint: []` with `entrypoint: ['poetry', 'run']`

- api-setup:
  - api is setup with dependencies, connected to database with a User table, and API connection to the User table.
  - setting up api:
    - replace database name
    - create database using pgadmin
    - setup peewee models
    - setup fastapi routers
