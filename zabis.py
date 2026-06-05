import argparse
from storage import load_data , save_data , export_to_csv ,import_csv
from logger import logger


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")


add_parser = subparsers.add_parser("add")
add_parser.add_argument("--amount", type=float, required=True)
add_parser.add_argument("--category", type=str, required=True)

import_parser = subparsers.add_parser("import_csv")
import_parser.add_argument("--path", type=str ,required=True)


list_parser = subparsers.add_parser("list")
stats_parser = subparsers.add_parser("stats")
export_csv_parser = subparsers.add_parser("export_csv")

args = parser.parse_args()
logger.info(f"Command: {args.command}")

if args.command == "add":

    if args.amount <= 0:
        logger.error(f"Invalid amount: {args.amount}. Must be > 0")
        print("Ошибка: сумма должна быть больше 0")
        exit(1)

    if not args.category.strip():
        logger.error(f"Invalid category: '{args.category}' (empty or whitespace)")
        print("Ошибка: категория не должна быть пустой")
        exit(1)

    logger.info(f"Add command: {args.amount} {args.category}")
    data = load_data()
    data.append({
        "amount": args.amount,
        "category": args.category
    })
    save_data(data)


elif args.command == "list":
    data = load_data()

    for item in data:
        print(f"{item['amount']} {item['category']}")


elif args.command == "stats":
    data = load_data()

    total = sum(float(t.get("amount", 0)) for t in data)

    print("Всего:", total)
    print("Операций:", len(data))

elif args.command == "export_csv":
    data = load_data()

    logger.info(f"Export started: {len(data)} records")

    export_to_csv(data)

    logger.info(f"Export finished: {len(data)} records written to CSV")

elif args.command == "import_csv":
    data = load_data()

    logger.info(f"Import started: {args.path}")

    new_items = list(import_csv(args.path))
    data.extend(new_items)

    save_data(data)

    logger.info(f"Import finished: {len(new_items)} records imported")

else:
    logger.error("No command provided")
    parser.error("Command is required")






