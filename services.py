from storage import load_data, save_data, export_to_csv, import_csv
from logger import logger
from pathlib import Path

def add_transaction(args):

    if args.amount <= 0:
        logger.error("Invalid amount")
        print("Ошибка: сумма должна быть больше 0")
        exit(1)

    if not args.category.strip():
        logger.error("Invalid category")
        print("Ошибка: категория не должна быть пустой")
        exit(1)

    if not args.date.strip():
        print("Ошибка: дата не должна быть пустой")
        exit(1)

    if not args.description.strip():
        print("Ошибка: описание не должно быть пустым")
        exit(1)

    if len(args.currency) != 3:
        print("Ошибка: валюта должна быть 3 буквы")
        exit(1)

    if args.type not in ["expense", "income"]:
        print("Ошибка: type должен быть expense или income")
        exit(1)

    data = load_data()

    data.append({
        "amount": args.amount,
        "category": args.category,
        "date": args.date,
        "description": args.description,
        "currency": args.currency,
        "type": args.type
    })

    save_data(data)

    logger.info("Transaction added")


def list_transactions():
    data = load_data()

    for item in data:
        amount = item.get("amount")
        category = item.get("category")

        if amount is None or category is None:
            continue

        print(f"{amount} {category}")




def get_stats():
    data = load_data()

    total = sum(float(t.get("amount", 0)) for t in data)

    print("Всего:", total)
    print("Операций:", len(data))



def export():
    data = load_data()

    logger.info(f"Export started: {len(data)} records")

    export_to_csv(data)

    logger.info("Export finished")


def import_data(path):

    file = Path(path)

    if not file.exists():
        logger.error(f"File not found: {path}")
        print("Ошибка: файл не существует")
        return

    data = load_data()

    logger.info(f"Import started: {path}")

    new_items = list(import_csv(path))

    data.extend(new_items)

    save_data(data)

    logger.info(f"Import finished: {len(new_items)} records")