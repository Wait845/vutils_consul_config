import consul.aio


class ConsulConfig:
    _instance = None
    _first_init = True

    def __init__(self,
                host: str,
                port: int,
                token: str = None
        ):
        if not ConsulConfig._first_init:
            return
        ConsulConfig._first_init = False

        self.config = consul.aio.Consul(
                        host=host,
                        port=port,
                        token=token)

    async def get(self, key, default=None):
        index, data = await self.config.kv.get(key)
        if data is None:
            await self.set(key, default)
            return default
        return data['Value'].decode('utf-8')

    async def set(self, key, value):
        await self.config.kv.put(key, value)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
