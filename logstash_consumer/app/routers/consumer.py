from fastapi import APIRouter, Request

from logstash_consumer.app.controllers import event_hub
from logstash_consumer.app.utils.log import LogApplication


router = APIRouter()


@router.post("", status_code=200)
async def consumer_log_stash(
    request: Request,
    payload: dict
):
    log_user = LogApplication(request, await request.body())

    data = await event_hub.send(payload, log_user)

    return data
