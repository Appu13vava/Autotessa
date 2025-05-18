import logging
import logging.config
import asyncio
import threading
from flask import Flask

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR, LOG_CHANNEL
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types


class TelegramLogHandler(logging.Handler):
    def __init__(self, client, chat_id, loop):
        super().__init__()
        self.client = client
        self.chat_id = chat_id
        self.loop = loop

    def emit(self, record):
        log_entry = self.format(record)
        if self.loop and not self.loop.is_closed():
            asyncio.run_coroutine_threadsafe(self.send_log(log_entry), self.loop)

    async def send_log(self, message):
        try:
            await self.client.send_message(self.chat_id, message)
        except Exception as e:
            print(f"Failed to send log message: {e}")


class Bot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
        self.loop = None

    async def start(self):
        if self.loop is None:
            self.loop = asyncio.get_running_loop()  # Save event loop once
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username

        if LOG_CHANNEL and LOG_CHANNEL != 0:
            try:
                await self.send_message(LOG_CHANNEL, LOG_STR)
            except Exception as e:
                print(f"Failed to send startup log to log channel: {e}")

            # Attach the Telegram log handler only if LOG_CHANNEL is set and valid
            telegram_handler = TelegramLogHandler(self, LOG_CHANNEL, self.loop)
            telegram_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            telegram_handler.setFormatter(formatter)
            logging.getLogger().addHandler(telegram_handler)
        else:
            print("LOG_CHANNEL is not set or zero; skipping Telegram logging setup.")

        logging.info(f"{me.first_name} for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info("Telegram logging enabled.")

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current + new_diff + 1)))
            for message in messages:
                yield message
                current += 1


# --- Flask server to pass Koyeb TCP health check ---
flask_app = Flask(__name__)
bot_app = Bot()


@flask_app.route("/")
def health():
    return "Bot is running", 200


def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(bot_app.start())
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        loop.run_until_complete(bot_app.stop())
        loop.close()


if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    flask_app.run(host="0.0.0.0", port=8080)
