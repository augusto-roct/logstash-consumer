import json
import os

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

from logstash_consumer.app.utils.log import LogApplication


EVENT_HUB_CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")


async def send_batch_event_hub(data: dict, log_user: LogApplication):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR,
        eventhub_name=EVENT_HUB_NAME
    )

    async with producer:
        event_data_batch = await producer.create_batch()

        event_data_batch.add(EventData(json.dumps(data)))

        await producer.send_batch(event_data_batch)

    return "data send to event hub"
