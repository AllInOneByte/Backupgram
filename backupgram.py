from pyrogram.client import Client
import pyrogram.types as ptypes
import asyncio
from database import DatabaseWrapper
import config

db = DatabaseWrapper(config.MONGO_USERNAME, config.MONGO_PASSWORD)


async def main():
    async with Client(
        "Backupgram", config.API_ID, config.API_HASH, takeout=True
    ) as app:
        if config.SAVE_PERSONAL_INFO:
            me = await app.get_me()
            self_chat = await app.get_chat(me.id)
            result = db.save_personal_info(
                id=me.id,
                first_name=me.first_name or "",
                last_name=me.last_name or "",
                phone_number=me.phone_number or "",
                username=me.username or "",
                bio=self_chat.bio or "",  # type: ignore
            )
            if not result:
                print("* Error while saving personal info")

        if config.SAVE_CONTACTS:
            contacts = await app.get_contacts()
            for contact in contacts:
                result = db.save_contact(
                    first_name=contact.first_name or "",
                    last_name=contact.last_name or "",
                    phone_number=contact.phone_number or "",
                )
                if not result:
                    print(
                        f"* Error while saving contact {contact.first_name} {contact.last_name}"
                    )


if __name__ == "__main__":
    asyncio.run(main())
