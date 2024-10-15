# FastAPI, SQLModel, Pydantic, and Alembic Example Project

This project demonstrates a minimal working example of a FastAPI application integrated with **SQLModel**, Pydantic, and Alembic. It uses `uv` for dependency management.

## Project Overview

This sample project showcases:

- FastAPI for building APIs
- [SQLModel](https://sqlmodel.tiangolo.com/) for ORM (in addition to [SQLAlchemy](https://www.sqlalchemy.org/), which SQLModel extends)
- Pydantic for data validation
- Alembic for database migrations
- `uv` for dependency management (note, install `uv` using `pip` if you do not already have it)

A key feature of this example is demonstrating that the returned, "unified" (schema and db) object includes the database-generated ID.

## Motivation

The motivation for this project is to provide a thinner, end-to-end persistence example than the main FastAPI full-stack example ([fastapi/full-stack-fastapi-postgresql](https://github.com/fastapi/full-stack-fastapi-postgresql)). This example is also specific to postgres, at least in that it handles persisted object identifiers that way.

## Setup

1. **Clone the repository:**

   ```bash
   git clone [your-repo-url]
   cd [your-repo-name]
   ```

2. **Create a virtual environment using `venv` and install dependencies:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   uv venv
   uv pip install -r requirements.txt
   ```

   *Note:* This project uses `uv` for dependency management. If you prefer using `pip` directly, you can install dependencies without `uv`:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up your database URL in a `.env` file at the project root:**

   ```env
   SQLALCHEMY_DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

4. **Set up the database tables using Alembic:**

   a. **Create the initial revision:**

      ```bash
      alembic revision --autogenerate -m "Initial migration"
      ```

   b. **Apply the migration to upgrade the database:**

      ```bash
      alembic upgrade head
      ```

5. **Start the FastAPI server:**

   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

Once the server is running, you can interact with the API:

1. **Create a new user:**

   ```bash
   curl -X POST "http://localhost:8000/users/" \
        -H "Content-Type: application/json" \
        -d '{"name": "John Doe", "email": "john@example.com"}'
   ```

2. **Get all users:**

   ```bash
   curl "http://localhost:8000/users/"
   ```

3. **Access the interactive API documentation at `http://localhost:8000/docs`.**

   This is the easiest way to test out the API in action.

## Notes

- **SQLModel** is a library for interacting with SQL databases using Python type annotations, and it is designed to be fully compatible with Pydantic and SQLAlchemy. It simplifies working with SQL databases in FastAPI applications.

- This project demonstrates how to use **SQLModel** with **Alembic** for database migrations, providing a simple yet complete example for building FastAPI applications with PostgreSQL.

- The use of **Alembic** here shows how to handle database migrations effectively, which is an extension to many example projects that often omit this important aspect.

## Additional Information

- **uv**: A simple tool to manage your virtual environments and dependencies. It ensures that commands like `pip` are run inside your virtual environment without explicitly activating it every time.

- **Virtual Environments**: Using virtual environments is a best practice for Python development. It allows you to manage project-specific dependencies without interfering with your system-wide packages.

## License

This project is open-source and available under the [MIT License](LICENSE).
