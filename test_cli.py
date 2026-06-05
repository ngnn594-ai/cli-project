import subprocess
import sys


def test_add_valid():
    result = subprocess.run(
        [sys.executable, "zabis.py", "add", "--amount", "10", "--category", "food"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0


def test_add_invalid_amount():
    result = subprocess.run(
        [sys.executable, "zabis.py", "add", "--amount", "0", "--category", "food"],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0
    assert "Ошибка: сумма должна быть больше 0" in result.stdout


def test_add_empty_category():
    result = subprocess.run(
        [sys.executable, "zabis.py", "add", "--amount", "10", "--category", "   "],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0
    assert "категория не должна быть пустой" in result.stdout


def test_stats():
    subprocess.run(
        [sys.executable, "zabis.py", "add", "--amount", "10", "--category", "food"],
        capture_output=True,
        text=True
    )

    result = subprocess.run(
        [sys.executable, "zabis.py", "stats"],
        capture_output=True,
        text=True
    )

    assert "Всего:" in result.stdout
    assert "Операций:" in result.stdout


def test_list():
    result = subprocess.run(
        [sys.executable, "zabis.py", "list"],
        capture_output=True,
        text=True
    )

    assert isinstance(result.stdout, str)

def test_import_csv(tmp_path):
    # 1. создаём временный csv файл
    file = tmp_path / "data.csv"
    file.write_text("10,food\n20,transport")

    # 2. запускаем программу
    result = subprocess.run(
        [sys.executable, "zabis.py", "import_csv", "--path", str(file)],
        capture_output=True,
        text=True
    )

    # 3. проверяем успех
    assert result.returncode == 0

def test_export_csv():
    # 1. сначала добавляем данные
    subprocess.run(
        [sys.executable, "zabis.py", "add", "--amount", "10", "--category", "food"],
        capture_output=True,
        text=True
    )

    # 2. экспортируем в CSV
    result = subprocess.run(
        [sys.executable, "zabis.py", "export_csv"],
        capture_output=True,
        text=True
    )

    # 3. проверяем что команда успешна
    assert result.returncode == 0