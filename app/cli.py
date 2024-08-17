import uvicorn
from .const import HOST, PORT
from pathlib import Path


def start():
    """Starts the FastAPI application using Uvicorn.

    This function runs the FastAPI application with auto-reload enabled,
    using environment variables for host and port configuration.

    If HOST and PORT environment variables are not set, defaults to 0.0.0.0:8000.
    """
    uvicorn.run(
        "app:app",
        reload=True,
        reload_dirs=Path(__file__).parent.__str__(),
        host=HOST,
        port=PORT,
    )
