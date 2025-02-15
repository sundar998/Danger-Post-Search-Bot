# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import traceback
from pyrogram.types import Message
from pyrogram import Client, filters
from info import API_ID, API_HASH, DATABASE_URI, ADMIN
from pymongo import MongoClient

mongo_client = MongoClient(DATABASE_URI)
database = mongo_client.userdb.sessions

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot: Client, message: Message):
    await message.reply_text("**Bot is active!**\n\nSubscribe: [YouTube](https://youtube.com/@Tech_VJ)")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
