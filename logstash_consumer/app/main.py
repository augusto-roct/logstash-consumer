from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

from logstash_consumer import __version__
from logstash_consumer.app import routers

openapi_tags = [
    {"name": "root", "description": "Endpoint to application Root"},
    {"name": "health", "description": "Endpoints to check health application"},
    {"name": "consumer", "description": "Endpoint to send data to the event hub"}
]

app = FastAPI(
    title="Logstash Consumer",
    version=__version__,
    description="Microsservice to consumer logs in logstash and send for Azure Event Hubs",
    openapi_tags=openapi_tags
)

app.add_middleware(PrometheusMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/metrics", handle_metrics)
app.include_router(routers.index, tags=["root"])
app.include_router(routers.health, tags=["health"], prefix="/health")
app.include_router(routers.consumer, tags=["consumer"], prefix="/consumer")
