import os
import redis
from dotenv import load_dotenv

load_dotenv()

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_db = os.getenv("REDIS_DB", 0)

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

def cache_get(key):
    return redis_client.get(key)

def cache_set(key, value, ex=3600):
    redis_client.set(key, value, ex)