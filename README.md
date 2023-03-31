# README

## branches

### 1. project-init-state

api and web services are setup without dependencies installed. To install dependencies, run following commands:

- for api:

```bash
  docker-compose run --rm api bash
  poetry install
```

- for web:

```bash
  docker-compose run --rm web npm install
```

- then, add
  - `command: ["npm", "run", "dev"]` to web service in docker-compose.yml
  - `command: ["uvicorn", "main:router", "--reload", "--host=0.0.0.0"]` to api servce in docker-compose .yml
  - and, replace `entrypoint: []` with `entrypoint: ['poetry', 'run']`

### 2. api-setup

Install dependencies per section 1. Then setup database with following instructions:

- replace database name
- create database using pgadmin
- setup peewee models
- setup fastapi routers

## TODO

- [ ] add eslint and pylint
- [ ] add pug and sass
