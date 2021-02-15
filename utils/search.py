import datetime

from tracemoe import ATraceMoe

tracemoe = ATraceMoe()


async def search(url) -> str:
    data = await tracemoe.search(url, is_url=True)
    title = data["result"][0]["anilist"]["title"]["english"]
    episode = data["result"][0]["episode"]
    start = datetime.timedelta(seconds=round(data["result"][0]["from"]))
    end = datetime.timedelta(seconds=round(data["result"][0]["to"]))
    similarity = round(data["result"][0]["similarity"] * 100)

    text = "Аниме: {}\nЭпизод: {}\nТаймкод: с {} по {}\nТочность: {}%".format(
        title,
        episode if isinstance(episode, str) else ", ".join(map(str, episode)),
        start,
        end,
        similarity,
    )
    return text
