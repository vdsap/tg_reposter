import asyncio as aio
from init import main_config, log
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message


    # Load config
async def main():
    main_conf = main_config()
    # Start Telegram bot
    log().debug('Starting Telegram bot')
    token = main_config()['TG_BOT']['token']
    router = Router()
    dp = Dispatcher()
    bot = Bot(token=token, parse_mode='HTML')

    @router.channel_post()
    async def get_file(channel_post: Message):
        log().debug('Getting file')
        file = channel_post.document

    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    log().info('Script started')
    aio.run(main())
    aio.run(tg_())
