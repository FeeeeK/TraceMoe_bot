import json

import aiofiles


class JsonConfig:
    def __init__(self, path: str):
        self.data: dict = {"token": ""}

        self._path: str = path
        self.token: str = None
        self._read_in()

    async def _write_out(self):
        async with aiofiles.open(self._path, "w", encoding="utf-8") as database:
            await database.write(json.dumps(self.data, ensure_ascii=False))

    def _read_in(self):
        with open(self._path, "r", encoding="utf-8") as database:
            self.data = json.load(database)
            self.token = self.data["token"]

    async def save(self):
        await self._write_out()
