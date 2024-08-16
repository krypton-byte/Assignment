
# Unian Assignment

This is a project for joining Unian, utilizing FastAPI as the web framework and Tortoise ORM for database management.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Tortoise ORM**: An easy-to-use async ORM built with relations in mind.
- **Poetry**: A dependency management tool for Python.

## Installation

To get started with the project, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

## Database Migration

Before running the application, you need to migrate the database schema:

```bash
poetry run migrate
```

## Running the Application

To start the application, use the following command:

```bash
poetry run app
```

## Additional Information

- Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed on your system.
- Make sure to configure your database settings appropriately in the project before running migrations.
- The application should be accessible at `http://localhost:8000` by default.

---
