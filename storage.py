import json
import csv
from pathlib import Path



BASE_DIR = Path("data")
BASE_DIR.mkdir(exist_ok=True)


FILE = BASE_DIR / "transactions.json"
FILE_TO_CSV = BASE_DIR / "transactions.csv"
FILE_TO_IMPORT = BASE_DIR / "test.csv"

def load_data():
    if not FILE.exists():
        return []
    with open(FILE, "r", encoding="utf-8")  as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def export_to_csv(data):
    with open(FILE_TO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["amount", "category"])

        for item in data:
            writer.writerow([
                item.get("amount", 0),
                item.get("category", "")
            ])

def import_csv(filename):
    file_path = BASE_DIR / f"{filename}"
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
