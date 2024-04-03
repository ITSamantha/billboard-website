import aioredis
from src.config.app.config import settings_app


class Redis:

    async def init_pool(self):
        self.pool = aioredis.ConnectionPool.from_url(
            "redis://" + settings_app.REDIS_HOST,
            password=settings_app.REDIS_PASSWORD,
            max_connections=10
        )

    async def close_pool(self):
        if not self.pool:
            return
        # todo close pool
        # self.pool.close()
        # await self.pool.wait_closed()
        self.pool = None

    def get_connection(self):
        if not self.pool:
            raise Exception('Connection pool is not initialized. Cannot get connection instance.')
        return aioredis.Redis(connection_pool=self.pool)


redis = Redis()
