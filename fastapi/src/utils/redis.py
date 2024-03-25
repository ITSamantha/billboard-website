import aioredis


class Redis:
    def __init__(self):
        self.init_pool()

    def init_pool(self):
        self.pool = aioredis.ConnectionPool.from_url("redis://otiva_redis", max_connections=10)

    async def close_pool(self):
        if not self.pool:
            return
        self.pool.close()
        await self.pool.wait_closed()
        self.pool = None


redis = Redis()
