from src.utils.redis import redis
import json
import asyncio


class PubSubMessage:
    def __init__(self, data, pattern, channel, type):
        self.data = data
        self.pattern = pattern
        self.channel = channel
        self.type = type


class PubSub:
    @staticmethod
    async def publish(channel: str, msg):
        if type(msg) is not str:
            try:
                msg = json.dumps(msg)
            except Exception:
                raise Exception('msg must be string or json serializable.')

        pub = redis.get_connection()

        await pub.publish(channel, msg)
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
