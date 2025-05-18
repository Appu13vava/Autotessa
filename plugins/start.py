from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client: Client, message: Message):
    await message.reply_text("Hello! Your bot is running successfully.")
