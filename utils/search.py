import datetime

from tracemoe import ATraceMoe

tracemoe = ATraceMoe()


async def search(url) -> str:
    data = await tracemoe.search(url, is_url=True)
    title = (
        data["result"][0]["anilist"]["title"]["english"]
        or data["result"][0]["anilist"]["title"]["romanji"]
        or data["result"][0]["anilist"]["synonyms"][0]
    )
    episode = str(data["result"][0]["episode"]) or "1"
    timecode = datetime.timedelta(seconds=data["result"][0]["from"] or 0)
    similarity = round(data["result"][0]["similarity"] * 100)

    text = "Аниме: {}\nЭпизод: {}\nТаймкод: {}\nТочность: {}%".format(
        title,
        episode if isinstance(episode, str) else ", ".join(map(str, episode)),
        timecode,
        similarity,
    )
    return text
