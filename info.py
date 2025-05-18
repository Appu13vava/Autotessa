import re
from os import environ

# Helper function to parse boolean-like strings
def is_enabled(value, default):
    if isinstance(value, bool):
        return value
    if not value:
        return default
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Pattern to check if a string looks like an ID (numbers with optional prefix)
id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '0') or 0)
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', 'False'), False)

# List of picture URLs split by spaces
PICS = environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg').split()

# Admins, Channels & Users — parse IDs or leave as string if not numeric
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = auth_users + ADMINS if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Anurag")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Anurag_files')

# Other settings & flags
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'sources_cods')

P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get('SPELL_CHECK_REPLY', "True"), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split() if ch.strip()]

# Captions
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b><i>{file_name} » {file_size} › [ᎯℕUℛᎯᎶ](https://t.me/MOVIES_ZILAA)</i></b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b><i>{file_name} » {file_size} › [ᎯℕUℛᎯᎶ](https://t.me/MOVIES_ZILAA)</i></b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝖯𝗈𝗐𝖾𝗗 𝖡𝗒 [ᴀᴍ_ᴛᴇᴄʜ](https://t.me/Am_RoBots)")

# Log summary string to verify config loading
LOG_STR = (
    "Current Customized Configurations are:-\n"
    + ("IMDB Results enabled, bot will show IMDB details.\n" if IMDB else "IMDB Results disabled.\n")
    + ("P_TTI_SHOW_OFF enabled: users redirected to /start PM instead of file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF disabled, files sent directly.\n")
    + ("SINGLE_BUTTON enabled: filename and filesize shown as single button.\n" if SINGLE_BUTTON else "SINGLE_BUTTON disabled, filename and filesize shown separately.\n")
    + (f"CUSTOM_FILE_CAPTION enabled with value: {CUSTOM_FILE_CAPTION}\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION found.\n")
    + ("Long IMDB description enabled.\n" if LONG_IMDB_DESCRIPTION else "Long IMDB description disabled.\n")
    + ("Spell check mode enabled: bot suggests related movies if not found.\n" if SPELL_CHECK_REPLY else "Spell check mode disabled.\n")
    + (f"MAX_LIST_ELM set: long lists limited to first {MAX_LIST_ELM} elements.\n" if MAX_LIST_ELM else "No MAX_LIST_ELM set, full lists shown.\n")
    + f"Current IMDB template:\n{IMDB_TEMPLATE}\n"
)

# Extra features and other constants
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 40))
SELF_DELETE = is_enabled(environ.get('SELF_DELETE', "True"), True)

DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/sources_cods/55"

CAPTION_BUTTON = "Subscribe"
CAPTION_BUTTON_URL = "https://youtube.com/channel/UCqts9WhhlioK3RB9XQQzoAg"
