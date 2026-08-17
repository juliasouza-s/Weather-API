import json
import redis

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
)

def get_cache(city):
    data = redis_client.get(city)
    if data:
        return json.loads(data)
    return None

def set_cache(city, data):
    redis_client.set(
        city,
        json.dumps(data),
        ex=3600
    )