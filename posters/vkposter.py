from vkbottle import API
from vkbottle.tools import PhotoWallUploader
from init import main_config, log


async def vk(file):
    # vk bot conf
    log().debug('Loading vk poster')
    api = API(main_config()['VK']['token'])
    vk_wallposter = PhotoWallUploader(api)
    upload_url = await api.photos.get_upload_server(group_id=-220955688)
    photo = await vk_wallposter.upload(file_source=file.file_path)
