from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics

from logstash_consumer import __version__
from logstash_consumer.app import routers

openapi_tags = [
    {"name": "root", "description": "Endpoint to application Root"},
    {"name": "health", "description": "Endpoints to check health application"}
]

app = FastAPI(
    title="Logstash Consumer",
    version=__version__,
    description="Microsservice to consumer logs in logstash and send for Azure Event Hubs",
    openapi_tags=openapi_tags
)

app.add_middleware(PrometheusMiddleware)

app.add_route("/metrics", handle_metrics)
app.include_router(routers.index, tags=["root"])
app.include_router(routers.health, prefix="/health", tags=["health"])
