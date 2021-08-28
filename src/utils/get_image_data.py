from vkbottle import AiohttpClient


async def get_image_data(url: str):
    async with AiohttpClient() as http:
        return await http.request_content("GET", url)
