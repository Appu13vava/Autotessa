import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value is None:
        return default
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot credentials
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '0') or 0)
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', 'False'), False)
PICS = environ.get('PICS', '').split()

# Admins and channels
ADMINS = [int(a) if id_pattern.search(a) else a for a in environ.get('ADMINS', '').split()]
CHANNELS = [int(c) if id_pattern.search(c) else c for c in environ.get('CHANNELS', '0').split()]
auth_users = [int(u) if id_pattern.search(u) else u for u in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = auth_users + ADMINS if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(g) for g in auth_grp.split()] if auth_grp else []

# MongoDB info
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Anurag")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Anurag_files')

# Other configs
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '0') or 0)
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'sources_cods')

# Construct the LOG_STR used in bot startup logs
LOG_STR = "Current Customized Configurations are:\n"
LOG_STR += f"IMDB Results: {'enabled' if is_enabled(environ.get('IMDB', 'True'), True) else 'disabled'}\n"
LOG_STR += f"Use Caption Filter: {USE_CAPTION_FILTER}\n"
LOG_STR += f"Admins: {ADMINS}\n"
LOG_STR += f"Channels: {CHANNELS}\n"
LOG_STR += f"Auth Users: {AUTH_USERS}\n"
LOG_STR += f"Log Channel: {LOG_CHANNEL}\n"

# You can expand LOG_STR with more config details as you like.
