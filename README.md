#Build an analytics API using FastAPI + Time Series Postgres

Own your data pipeline !

Start by building an Analytics API service with Python, FastAPI , and Time-Series Postgres with TimeScaleDB

## Docker 
- `docker build -t analytics-api -f Dockerfile .`
- `docker run -it analytics-api`


## 
- `docker compose up with watch or docker compose down to remove volumes`

##
- `1. Remove stopped containers`
-`docker container prune`

Removes all containers that are not running.

2. Remove unused images
docker image prune

More aggressive (removes dangling images only).

If you want to remove all unused images:

docker image prune -a

3. Remove build cache (this is usually what “stuck builds” are)

Modern Docker uses BuildKit, which stores cache separately.

docker builder prune

Or aggressively:

docker builder prune -a

4. Remove everything unused (full cleanup)

⚠️ This is the “nuclear option”:

docker system prune -a

If you also want to remove volumes (careful: deletes DB data):

docker system prune -a --volumes

5. Docker Compose cleanup (important for your case)

Since you're using docker compose up --watch, you likely have Compose artifacts:

docker compose down

If you also want to remove volumes:

docker compose down -v

6. Why Docker Desktop still shows “inactive builds”
-`Even after deletion, Docker Desktop UI may still show:`

-`A) Build cache not cleared`

-`→ use docker builder prune`

-`B) Old Compose projects cached`

-`→ restart Docker Desktop`

-`C) Images still referenced indirectly`

-`Check:`

-`docker images -a`
-`7. Check what is actually taking space`

-`Run:`

-`docker system df`

-`It will show:`

-`Images`
-`Containers`
-`Volumes`
-`Build cache`

-`This tells you what is actually still there.`

-`8. Safe recommended cleanup sequence (best practice)`

`If you just want a clean dev environment:`

`docker compose down -v`
`docker system prune -a`
`docker builder prune -a`
`9. Important warning (for your DB setup)`

`Since you are using TimescaleDB/Postgres:`

`❌ Do NOT run --volumes unless you want to delete your database`
`because it removes:`

`tables`
`migrations`
`event data`
`everything`
`Summary`

`What you’re seeing is usually not “ghost builds”, but:`

`Docker build cache + unused images + stopped containers not fully cleaned`

`Use:`

`docker builder prune -a → clears build cache (most important for “stuck builds”)`
`docker image prune -a → removes unused images`
`docker system prune -a → full cleanup`