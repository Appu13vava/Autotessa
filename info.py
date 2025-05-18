import re
from os import environ

id_pattern = re.compile(r'^-?\d+$')  # accept negative IDs (channels often start with -100)

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

def get_int_env(name, default=None):
    value = environ.get(name, '').strip()
    if value == '':
        return default
    try:
        return int(value)
    except ValueError:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.match(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.match(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.match(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.match(auth_channel) else None
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Anurag")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Anurag_files')

# IMPORTANT FIX: safer int parse for LOG_CHANNEL and INDEX_REQ_CHANNEL
LOG_CHANNEL = get_int_env('LOG_CHANNEL', None)  # None if not set or invalid
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'sources_cods')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "False"), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b><i>{file_name} » {file_size} › [ᎯℕUℛᎯᎶ](https://t.me/MOVIES_ZILAA)</i></b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [ᴀᴍ_ᴛᴇᴄʜ](https://t.me/Am_RoBots)")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Use LOG_CHANNEL as default for INDEX_REQ_CHANNEL, but safely parsed
INDEX_REQ_CHANNEL = get_int_env('INDEX_REQ_CHANNEL', LOG_CHANNEL)

FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split() if id_pattern.match(ch)]

MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# LOG_STR message unchanged ...

# EXTRA FEATURES (your existing code)...

# Usage note:
# In your bot startup, do a check like:
# if LOG_CHANNEL is None:
#     print("LOG_CHANNEL not set or invalid. Skipping telegram log messages.")
