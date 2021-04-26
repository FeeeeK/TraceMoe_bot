import datetime

from tracemoe import ATraceMoe

tracemoe = ATraceMoe()


async def search(url) -> str:
    data = await tracemoe.search(url, is_url=True)
    title = (
        data["docs"][0]["title_english"]
        or data["docs"][0]["title"]
        or data["docs"][0]["synonyms"][0]
    )
    episode = data["docs"][0]["episode"] or "1"
    timecode = datetime.timedelta(seconds=data["docs"][0]["at"] or 0)
    similarity = round(data["docs"][0]["similarity"] * 100)

    text = "Аниме: {}\nЭпизод: {}\nТаймкод: {}\nТочность: {}%".format(
        title,
        episode if isinstance(episode, str) else ", ".join(map(str, episode)),
        timecode,
        similarity,
    )
    return text
