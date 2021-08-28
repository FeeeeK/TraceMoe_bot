from vkbottle.bot import Bot
from config import api, labeler
from src.middlewares import SubscriptionMiddleware
from src.handlers import *  # noqa


def main():
    labeler.message_view.register_middleware(SubscriptionMiddleware())
    bot = Bot(api=api, labeler=labeler)
    bot.run_forever()
