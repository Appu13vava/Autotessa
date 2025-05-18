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

    if LOG_CHANNEL:
        try:
            await self.send_message(LOG_CHANNEL, LOG_STR)
        except Exception as e:
            print(f"Failed to send startup log to log channel: {e}")

        # Attach the Telegram log handler only if LOG_CHANNEL set
        telegram_handler = TelegramLogHandler(self, LOG_CHANNEL, self.loop)
        telegram_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        telegram_handler.setFormatter(formatter)
        logging.getLogger().addHandler(telegram_handler)
    else:
        print("LOG_CHANNEL is not set or zero; skipping Telegram logging setup.")

    logging.info(f"{me.first_name} for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info("Telegram logging enabled.")
