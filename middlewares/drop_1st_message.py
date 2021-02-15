from typing import Union

from vkbottle import BaseMiddleware
from vkbottle.bot import Message


class FirstMessageMiddleware(BaseMiddleware):
    async def pre(self, ans: Message) -> Union[bool, None]:
        if ans.conversation_message_id < 2:
            await ans.answer(
                "Чтобы пользоваться ботом, вам необходимо подписаться на группу."
            )
            return False
