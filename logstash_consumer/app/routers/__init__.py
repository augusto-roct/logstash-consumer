from logstash_consumer.app.routers.index import router as index
from logstash_consumer.app.routers.health import router as health
from logstash_consumer.app.routers.consumer import router as consumer


__all__ = [
    "index",
    "health",
    "consumer"
]
