import os
from dotenv import load_dotenv

load_dotenv()

def get_valid_api_keys() -> set[str]:
    keys = os.getenv("VALID_API_KEYS", "")
    return set(k.strip() for k in keys.split(",") if k.strip())
