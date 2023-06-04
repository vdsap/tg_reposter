from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from init import main_config, log
from posters.vkposter import vk


async def tg_bot():
    # Start Telegram bot
    log().debug('Starting Telegram bot')
    tgtoken = main_config()['TG_BOT']['token']
    router = Router()
    dp = Dispatcher()
    bot = Bot(token=tgtoken, parse_mode='HTML')

    @router.channel_post()
    async def channel_post_handler(channel_post: Message):
        log().debug('Getting tg file')
        file = await bot.get_file(channel_post.document.file_id)
        # vk poster
        await vk(file.file_path)
        # await api.wall.post(attachments={'photo'}_{-220955688}_{file})

    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)

