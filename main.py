from vkbottle.bot import Bot, Message

from lib import JsonConfig
from middlewares import FirstMessageMiddleware
from utils import get_image_url, search

config = JsonConfig("./config.json")
bot = Bot(config.token, task_each_event=True)
bot.labeler.message_view.register_middleware(FirstMessageMiddleware())


@bot.on.message(regexp=r".*(?i)(anime|аниме).*")
async def handler(ans: Message, _) -> str:
    url = get_image_url(ans)
    if not url:
        return "Не удалось найти картинку для поиска в Вашем сообщении!"
    try:
        text = await search(url)
    except Exception:
        return "Ой, произошла ошибка, попробуйте еще раз."
    return text


bot.run_forever()
