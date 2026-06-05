import argparse
from services import add_transaction, list_transactions, get_stats, export, import_data
from logger import logger

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add")
add_parser.add_argument("--amount", type=float, required=True)
add_parser.add_argument("--category", type=str, required=True)
add_parser.add_argument("--date", type=str, required=True)
add_parser.add_argument("--description", type=str, required=True)
add_parser.add_argument("--currency", type=str, required=True)
add_parser.add_argument("--type", type=str, required=True)


import_parser = subparsers.add_parser("import_csv")
import_parser.add_argument("--path", type=str, required=True)


subparsers.add_parser("list")


subparsers.add_parser("stats")


subparsers.add_parser("export_csv")

args = parser.parse_args()
logger.info(f"Command: {args.command}")



if args.command == "add":
    add_transaction(args)

elif args.command == "list":
    list_transactions()

elif args.command == "stats":
    get_stats()

elif args.command == "export_csv":
    export()

elif args.command == "import_csv":
    import_data(args.path)