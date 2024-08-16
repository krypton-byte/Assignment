import os
import uvicorn
from pathlib import Path


def start():
    uvicorn.run(
        "app:app",
        reload=True,
        reload_dirs=Path(__file__).parent.__str__(),
        host="127.0.0.1",
        port=int(os.environ.get("PORT", 8000)),
    )


if __name__ == "__main__":
    start()
