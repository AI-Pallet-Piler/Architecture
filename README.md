# AI-Pallet-Piler Architecture Usage Guide

This guide will help you set up and run the AI-Pallet-Piler project using Docker Compose. It covers prerequisites, environment setup, running all services, and starting specific services.

In this repo is a script to pull all repos needed for the project and a docker compose to run the services needen for the project

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system
- [Docker Compose](https://docs.docker.com/compose/install/) (Docker Desktop includes Compose)
- (Optional) [Git](https://git-scm.com/) for cloning the repository

## 1. Clone the Repository

create a folder for the project and clone the project to your local machine:

```sh
mkdir project-name
cd project-name
git clone https://github.com/AI-Pallet-Piler/Architecture.git
cd Architecture
```

## 2. Configure Environment Variables

Edit the `.env` file to set your database credentials and other environment variables as needed. Example:

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_DB=architecture_db
```

## 3. Project Structure

- `API-gateway/` – API Gateway service (Repo)(Dockerized)
- `Backend/` – Backend service (Repo)(Dockerized)
- `Frontend/` – Frontend service (Repo)(Dockerized)
- `Architecture/` – Contains `compose.yaml` and project documentation

## 4. Build and Run All Services

From the `Architecture` directory, run:

```sh
docker compose up -d
```

This will build and start all services defined in `compose.yaml` in detached mode.

## 5. Running a Specific Service

If you want to start only a specific service (e.g., just the database), use:

```sh
docker compose up -d database
```

Replace `database` with the name of the service you want to start (e.g., `backend`, `frontend`, `api-gateway`).

## 6. Stopping Services

To stop all running services:

```sh
docker compose down
```

To stop a specific service:

```sh
docker compose stop <service-name>
```

## 7. Troubleshooting

- Ensure all required folders (with Dockerfiles) exist for services you want to build.
- If you only want to run the database, make sure to specify it explicitly as shown above.
- Check logs with:
	```sh
	docker compose logs <service-name>
	```

## 8. Additional Notes

- Service names in `compose.yaml` must be lowercase.
- Port mappings and environment variables can be adjusted in `compose.yaml` and `.env` as needed.

---
For more details, see the documentation in each service's folder or contact the project maintainers.

## 9. References used
- [python os module](https://docs.python.org/3/library/os.html)
- [Docker compose file example](https://docs.docker.com/compose/gettingstarted/)
- [Postgres compose file example](https://github.com/docker/awesome-compose/tree/master/postgresql-pgadmin)
# Architecture
Repository with docker to run the whole stack

