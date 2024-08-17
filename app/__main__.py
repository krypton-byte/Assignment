import argparse
from .models.db_task import Initialize
from .cli import start

args = argparse.ArgumentParser()
action = args.add_subparsers(title="action", dest="action", required=True)
action.add_parser("serve")
action.add_parser("migrate")
parse = args.parse_args()


if __name__ == "__main__":
    if parse.action == "serve":
        start()
    else:
        Initialize()
