from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from init import main_config, log
from vkbottle import API
from vkbottle.tools import PhotoWallUploader


async def tg_bot():
    # vk bot conf
    log().debug('Loading vk')
    vktoken = main_config()['VK']['token']
    api = API(vktoken)
    vk_wallposter = PhotoWallUploader(api)
    # Start Telegram bot
    log().debug('Starting Telegram bot')
    tgtoken = main_config()['TG_BOT']['token']
    router = Router()
    dp = Dispatcher()
    bot = Bot(token=tgtoken, parse_mode='HTML')

    @router.channel_post()
    async def channel_post_handler(channel_post: Message):
        log().debug('Getting file')
        upload_url = await api.photos.get_upload_server(group_id=-220955688)
        file = await bot.get_file(channel_post.document.file_id)
        photo = await vk_wallposter.upload(file_source=file.file_path)
        # await api.wall.post(attachments={'photo'}_{-220955688}_{file})

    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)

