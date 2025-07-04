from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from mcp_server.config import get_valid_api_keys

API_KEY_NAME = "X-API-Key"
VALID_KEYS = get_valid_api_keys()

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key in VALID_KEYS:
        return api_key
    raise HTTPException(status_code=403, detail="Unauthorized API key")
