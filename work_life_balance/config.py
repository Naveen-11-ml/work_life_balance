from pathlib import Path


# File Path
BASE_PATH = Path(__file__).parent.parent

DATA_PATH = BASE_PATH / "data"
MODEL_PATH = BASE_PATH / "models"
TRANSFORMER_PATH = BASE_PATH / "work_life_balance/transformers"


# Data URLs
BUCKET_URL = "s3://remote-storage-lifenotes-gtr/work_life_balance/"
BUCKET_NAME = "remote-storage-lifenotes-gtr"
BUCKET_KEY = "work_life_balance/lifestyle_data.csv"
