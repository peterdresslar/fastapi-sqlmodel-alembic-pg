# FastAPI, SQLAlchemy, Pydantic, and Alembic Example Project

This project demonstrates a minimal working example of a FastAPI application integrated with SQLAlchemy, Pydantic, and Alembic. It uses `uv` for dependency management.

## Project Overview

This sample project showcases:
- FastAPI for building APIs
- SQLAlchemy for ORM
- Pydantic for data validation
- Alembic for database migrations
- uv for dependency management

A key feature of this example is demonstrating that the returned object includes the database-generated ID.

## Motivation

A motivation for this particular example is that the [fastapi](https://github.com/fastapi) major example project at @https://github.com/fastapi/full-stack-fastapi-template uses sqlmodel instead of sqlalchemy. 

## Setup

1. Clone the repository:
   ```
   git clone [your-repo-url]
   cd [your-repo-name]
   ```

2. Install dependencies using uv:
   ```
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

3. Set up your database URL in a `.env` file at the project root:
   ```
   SQLALCHEMY_DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

4. If you need to set up the tables, you can use alembic:

    a. Create the initial revision:
        ```
        alembic revision --autogenerate -m "Initial migration"
        ```

    b. Run database upgrade:
        ```
        alembic upgrade head
        ```

5. Start the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

## Usage

Once the server is running, you can interact with the API:

1. Create a new user:
   ```
   curl -X POST "http://localhost:3000/users/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
   ```

2. Get all users:
   ```
   curl "http://localhost:3000/users/"
   ```

3. Access the interactive API documentation at `http://localhost:8000/docs` ... in fact, this is the easiest way to test out the API in action

