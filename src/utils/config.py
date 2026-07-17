from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data"

RAW_DATA_PATH = DATA_PATH / "raw"

PROCESSED_DATA_PATH = DATA_PATH / "processed"

MODEL_PATH = BASE_DIR / "saved_models"

REPORT_PATH = BASE_DIR / "reports"