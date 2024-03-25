import aioredis


class Redis:

    async def init_pool(self):
        self.pool = await aioredis.ConnectionPool.from_url("redis://otiva_redis", max_connections=10)

    async def close_pool(self):
        if not self.pool:
            return
        self.pool.close()
        await self.pool.wait_closed()
        self.pool = None

    def get_connection(self):
        if not self.pool:
            raise Exception('Connection pool is not initialized. Cannot get connection instance.')
        return aioredis.Redis(connection_pool=self.pool)


redis = Redis()
