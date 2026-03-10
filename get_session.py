from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 32614157        # <-- ваш api_id
api_hash = "4fcf3660953c536c8506c7896b6575ed"  # <-- ваш api_hash

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Session string:")
    print(client.session.save())