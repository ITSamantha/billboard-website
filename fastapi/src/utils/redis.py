import aioredis


class Redis:

    async def init_pool(self):
        # self.pool = await aioredis.ConnectionPool.from_url("redis://otiva_redis", max_connections=10)
        self.pool = await aioredis.create_redis_pool('redis://otiva_redis', max_connections=10)

    async def close_pool(self):
        if not self.pool:
            return
        self.pool.close()
        await self.pool.wait_closed()
        self.pool = None


redis = Redis()
