from fastapi import APIRouter, Request

from logstash_consumer.app.utils.log import LogApplication


router = APIRouter()


@router.get("/", status_code=200)
async def root(
    request: Request
):
    LogApplication(request, await request.body())
    return {"message": "Logstash Consumer is running"}
