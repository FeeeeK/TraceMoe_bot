from vkbottle.bot import Message
from vkbottle.dispatch.rules.bot import ABCMessageRule

from src.utils.get_image_url import get_image_url


class ImageRule(ABCMessageRule):
    def __init__(self, need_image: bool = True) -> None:
        self.need_image = need_image

    async def check(self, message: Message):
        url = get_image_url(message)

        if not url and self.need_image:
            await message.answer("Вы должны прикрепить изображение")
            return False

        return {"image_url": url}
