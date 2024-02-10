from logstash_consumer.app.routers.index import router as index
from logstash_consumer.app.routers.health import router as health

__all__ = [
    "index",
    "health"
]
