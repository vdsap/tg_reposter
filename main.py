import asyncio as aio
from init import main_config, log
from tg import tg_bot


async def main():   # Load config
    main_conf = main_config()
    await tg_bot()


if __name__ == '__main__':
    log().info('Poster start')
    aio.run(main())
