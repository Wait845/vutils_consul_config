# vutils 系列 - CONSUL_CONFIG
## 异步读取配置中心配置
- 异步读写

## 使用
```Python3
from vutils_consul_config import ConsulConfig
import asyncio


async def main():
    consul_config = ConsulConfig(
        host="host",
        port=80,
        token="token")

    # 读取配置
    result = await consul_config.get(
        key="folder_name/config_name"
    )
    print(result)
    # config_value

    # 写入配置
    await consul_config.set(
        key="key",
        value="value"
    )


if __name__ == '__main__':
    asyncio.run(main())
```
