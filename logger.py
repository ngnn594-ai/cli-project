from pathlib import Path
import logging

BASE_DIR = Path("data")
FILE_LOGGING = BASE_DIR / "app.log"
BASE_DIR.mkdir(exist_ok=True)


logging.basicConfig(
    filename=FILE_LOGGING,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)



