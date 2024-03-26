from src.utils.redis import redis
import json
import asyncio
from typing import Union


class PubSubEvents:
    NEW_MESSAGE: str = 'new_message'


class PubSubMessage:
    def __init__(self, data, pattern, channel, type):
        self.data = data
        self.pattern = pattern
        self.channel = channel
        self.type = type


class PubSubEvent:
    def __init__(self, name, data: Union[list, dict]):
        self.name = name
        self.data = data

    def serialize(self) -> str:
        data = {
            'name': self.name,
            'data': self.data,
        }
        return json.dumps(data)


class PubSub:
    @staticmethod
    async def publish(payload: dict[str, PubSubEvent]):
        """Accepts dict {channel_name: data} and publishes data to respective channel names"""
        if not payload:
            return
        pub = redis.get_connection()

        for channel in payload:
            event: PubSubEvent = payload[channel]
            await pub.publish(channel, event.serialize())

        await pub.close()

    @staticmethod
    async def subscribe(channel: str):
        sub = redis.get_connection().pubsub()
        async with sub as conn:
            await conn.subscribe(channel)

            while True:
                try:
                    message = await conn.get_message(ignore_subscribe_messages=True)
                    if message is not None:
                        dto = PubSubMessage(
                            data=message['data'].decode('utf-8'),
                            pattern=message['pattern'].decode('utf-8') if message['pattern'] else None,
                            channel=message['channel'].decode('utf-8') if message['channel'] else None,
                            type=message['type'] if message['type'] else None,
                        )
                        yield dto
                    await asyncio.sleep(1)
                except Exception:
                    break

            await conn.unsubscribe(channel)
        await sub.close()
