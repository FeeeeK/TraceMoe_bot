import os
import sys

from vkbottle.bot import Bot, Message

from lib import JsonConfig
from middlewares import FirstMessageMiddleware
from utils import get_image_url, search

config = JsonConfig(os.path.realpath(f"{sys.path[0]}/config.json"))
bot = Bot(config.token, task_each_event=True)
bot.labeler.message_view.register_middleware(FirstMessageMiddleware())


@bot.on.message(regexp=r".*(?i)(?:anime|аниме).*")
async def handler(ans: Message, match) -> str:
    url = get_image_url(ans)
    if not url:
        return "Не удалось найти картинку для поиска в Вашем сообщении!"
    try:
        text = await search(url)
    except Exception:
        return "Ой, произошла ошибка, попробуйте еще раз."
    return text


bot.run_forever()
