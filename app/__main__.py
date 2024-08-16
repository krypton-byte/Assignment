import os
import uvicorn
from pathlib import Path
import argparse
from .models.db_task import Initialize
args = argparse.ArgumentParser()
action = args.add_subparsers(title="action", dest="action", required=True)
action.add_parser("run")
action.add_parser("migrate")
parse = args.parse_args()

def start():
    uvicorn.run(
        "app:app",
        reload=True,
        reload_dirs=Path(__file__).parent.__str__(),
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", 8000)),
    )


if __name__ == "__main__":
    if parse.action == "run":
        start()
    else:
        Initialize()
