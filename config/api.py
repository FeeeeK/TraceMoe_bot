from vkbottle import API, PhotoMessageUploader
from vkbottle.bot import BotLabeler
import os
from dotenv import load_dotenv

load_dotenv()
api = API(os.getenv("BOT_TOKEN"))
labeler = BotLabeler()
photo_message_uploader = PhotoMessageUploader(api)
