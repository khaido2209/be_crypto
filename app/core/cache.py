import os
import json
import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

def get_cache(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache(key: str, value, ttl: int = 60):
    redis_client.setex(key, ttl, json.dumps(value))
