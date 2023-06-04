import asyncio as aio
from init import log
from tg import tg_bot


#
async def main():
    await tg_bot()  # start main loop


if __name__ == '__main__':
    log().info('Poster start')
    aio.run(main())
