from src.utils import get_image_data
from vkbottle.bot import Message
from config import labeler, photo_message_uploader
from src.rules import ImageRule
from vkbottle.bot import rules
from aiomoe import AioMoe, errors
from datetime import timedelta

tm = AioMoe()
TEMPLATE = """
[Аниме]: {title}
[Тайм-код]: {timecode}
[Совпадение]: {similarity}%
[Эпизод]: {episode}
"""


@labeler.message(rules.RegexRule(r".*(?i)(?:anime|аниме).*"), ImageRule())
async def search(message: Message, image_url: str, match=None):
    try:
        response = await tm.search(image_url, anilist_info=True, cut_borders=True)
    except errors.APIError:
        return "Произошла ошибка, попробуйте еще раз чуть позже."
    if not response.result:
        await message.answer("Мне не удалось ничего найти.")
        return
    result = response.result[0]
    photo = None
    if result.image:
        data = await get_image_data(result.image)
        photo = await photo_message_uploader.upload(data)
    anilist_info = result.anilist
    title = (
        anilist_info.title.english
        or anilist_info.title.romaji
        or anilist_info.title.native
        or " / ".join(anilist_info.synonyms)
    )
    timecode = (
        f"{timedelta(seconds=round(result.from_))}"
        " - "
        f"{timedelta(seconds=round(result.to))}"
    )
    similarity = round(result.similarity * 100)
    text = TEMPLATE.format(
        title=title, timecode=timecode, similarity=similarity, episode=result.episode
    )
    await message.answer(text, photo)
