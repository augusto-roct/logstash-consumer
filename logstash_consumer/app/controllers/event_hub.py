from logstash_consumer.app.modules.azure.api import send_batch_event_hub
from logstash_consumer.app.utils.log import LogApplication, log_function


@log_function
async def send(data: dict, log_user: LogApplication):
    message = await send_batch_event_hub(data, log_user)
    return {"message": message}
