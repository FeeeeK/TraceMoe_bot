from typing import TYPE_CHECKING, List, Any
from config import api
from vkbottle import BaseMiddleware
from vkbottle.bot import Message

if TYPE_CHECKING:
    from vkbottle import ABCHandler, ABCView


class SubscriptionMiddleware(BaseMiddleware):
    async def post(
        self,
        message: Message,
        view: "ABCView",
        handle_responses: List[Any],
        handlers: List["ABCHandler"],
    ):
        if message.conversation_message_id > 2 or message.peer_id > 2e9:
            return True
        is_subscribed = await api.groups.is_member(message.group_id, message.from_id)
        if not is_subscribed:
            await message.answer(
                "Пожалуйста, подпишитесь на группу, если бот был вам полезен."
            )
