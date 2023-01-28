import config
import asyncio
from pyrogram.client import Client


async def main():
    async with Client("Backupgram", config.API_ID, config.API_HASH) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

asyncio.run(main())
