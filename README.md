
# Assignment

This is a project for joining ..., utilizing FastAPI as the web framework and Tortoise ORM for database management.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Tortoise ORM**: An easy-to-use async ORM built with relations in mind.
- **Poetry [Optional]**: A dependency management tool for Python.

## Installation

To get started with the project, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone git@github.com:krypton-byte/Assignment.git
   cd Assignment
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   #or
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, you need to migrate the database schema:

```bash
poetry run migrate
#or
python -m app migrate
```

## Running the Application

To start the application, use the following command:

```bash
poetry run app
#or
python -m app serve
```

## Proper Example HTTP Request to webhook
```bash
> curl -X POST http://127.0.0.1:8000/webhook \
-H "Content-Type: application/json" \
-d '{"task_id":1, "task_name": "new task name", "action_type": "test action", "dummy": "hello world"}'

```
## Additional Information

- Make sure to configure your database settings appropriately in the project before running migrations.
- The application should be accessible at `http://localhost:8000` by default.

---
