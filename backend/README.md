# fastapi-template
This Repository is based on python FastAPI that can be used as kickstarter for all your webapi operations.
### Open in dev containers mode

- venv interpertor located in `/app/.venv/bin/python`. this is useful to select python interceptor for debugging.
- for debugging , run the following command 
```sh
python -m debugpy --listen 5678 main.py
```
- later, click on debug tab and choose `Python: localhost` from dropdown and run it. it attaches to the running solution.

- navigate to `http://localhost:8070/docs`


### Run Application in docker and Debug

- Run the following command

```sh
docker compose -f compose.debug.yml up --build
```
- Go to debug take, select `Python: Debugger:FastAPI` from dropdown and hit play.
- navigate to `localhost:8000/docs`

### Run Application in PRD

- Run the following command

```sh
docker compose -f compose.yml up --build
```
- navigate to `localhost:8000/docs`


### When host doesnt have python and poetry

- To use `Poetry`, please change the `ENV_MODE=local` in `.env.local` 
- Later, Run the following command

```sh
docker compose -f compose.yml up --build
```

### Access Poetry
- In order to initiate a terminal, use this
```sh
docker exec -it multi-agent /bin/bash
```
- Add / Remove libraries
```sh
poetry add/remove <lib>
```

### Run Ruff Formatting
- Run `Ruff` commands for linting

```sh
ruff check /app --fix --exit-zero
ruff format /app
```
