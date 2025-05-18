import re
from os import environ

id_pattern = re.compile(r'^.\d+$') def is_enabled(value, default): if value.lower() in ["true", "yes", "1", "enable", "y"]: return True elif value.lower() in ["false", "no", "0", "disable", "n"]: return False else: return default

Bot information

SESSION = environ.get('SESSION', 'Media_search') API_ID = int(environ.get('API_ID', '')) API_HASH = environ.get('API_HASH', '') BOT_TOKEN = environ.get('BOT_TOKEN', '')

Log channel (supports both ID and username)

log_channel_env = environ.get('LOG_CHANNEL', '-1002483241672') LOG_CHANNEL = int(log_channel_env) if log_channel_env.startswith('-100') else log_channel_env

Bot settings

CACHE_TIME = int(environ.get('CACHE_TIME', 300)) USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False)) PICS = (environ.get('PICS', '')).split()

Admins, Channels & Users

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()] CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()] auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()] AUTH_USERS = (auth_users + ADMINS) if auth_users else [] auth_channel = environ.get('AUTH_CHANNEL') auth_grp = environ.get('AUTH_GROUP') AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

MongoDB information

DATABASE_URI = environ.get('DATABASE_URI', "") DATABASE_NAME = environ.get('DATABASE_NAME', "Anurag") COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Anurag_files')

Others

SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'sources_cods') P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True) IMDB = is_enabled((environ.get('IMDB', "True")), True) SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False) CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b><i>{file_name} » {file_size} › MOVIES</i></b>") BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b><i>{file_name} » {file_size} › MOVIES</i></b>") IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "\ud83c\udfe7 Title: <a href={url}>{title}</a> \n\ud83d\udd2e Year: {year} \n\u2b50\ufe0f Ratings: {rating}/10 \n\ud83c\udfad Genres: {genres}") LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False) SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True) MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None) INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', str(LOG_CHANNEL))) FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()] MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True) PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False) PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True) PORT = environ.get("PORT", "8080")

LOG_STR = "Current Configurations:\n" LOG_STR += ("IMDB enabled\n" if IMDB else "IMDB disabled\n") LOG_STR += ("P_TTI_SHOW_OFF enabled\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF disabled\n") LOG_STR += ("Single button mode ON\n" if SINGLE_BUTTON else "Single button mode OFF\n") LOG_STR += (f"Custom caption: {CUSTOM_FILE_CAPTION}\n" if CUSTOM_FILE_CAPTION else "Default caption\n") LOG_STR += ("Long IMDB enabled\n" if LONG_IMDB_DESCRIPTION else "Short IMDB\n") LOG_STR += ("Spell check enabled\n" if SPELL_CHECK_REPLY else "Spell check disabled\n") LOG_STR += (f"Max cast limit: {MAX_LIST_ELM}\n" if MAX_LIST_ELM else "All casts listed\n") LOG_STR += f"IMDB template: {IMDB_TEMPLATE}"

Extra features

USE_SHORTLINK = is_enabled(environ.get("USE_SHORTLINK", "False"), False) SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 40)) SELF_DELETE = is_enabled(environ.get('SELF_DELETE', 'True'), True)

DOWNLOAD_TEXT_NAME = "\ud83d\udce5 HOW TO DOWNLOAD \ud83d\udce5" DOWNLOAD_TEXT_URL = "https://t.me/sources_cods/55"

CAPTION_BUTTON = "Subscribe" CAPTION_BUTTON_URL = "https://youtube.com/channel/UCqts9WhhlioK3RB9XQQzoAg"

