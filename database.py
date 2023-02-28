from typing import Any
from pymongo import MongoClient
import datetime as dt


class DatabaseWrapper:
    def __init__(
        self,
        username,
        password,
        host="localhost",
        port=27017,
    ):
        self._client = MongoClient(
            host=host, port=port, username=username, password=password
        )
        self._db = self._client.backupgram

    def save_personal_info(
        self,
        id: int,
        first_name: str,
        last_name: str,
        phone_number: str,
        username: str,
        bio: str,
    ):
        collection = self._db["personal_information"]
        user: dict[str, Any] = {
            "user_id": id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "username": username,
            "bio": bio,
        }

        if not collection.find_one(
            user
        ):  # NOTE: was probably right to update and/or insert anyway
            user["created_at"] = dt.datetime.now()
            result = collection.insert_one(user)
            return result.inserted_id

        return True

    def save_profile_picture(self):
        pass

    def save_contact(self, first_name: str, last_name: str, phone_number: str):
        collection = self._db["contacts"]
        contact: dict[str, Any] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
        }

        if not collection.find_one(contact):
            contact["created_at"] = dt.datetime.now()
            result = collection.insert_one(contact)
            return result.inserted_id

        return True

    def save_frequent_contact(self):
        pass

    def save_chat(self):
        pass

    def save_left_chat(self):
        pass
