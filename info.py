import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '21280367'))
API_HASH = environ.get('API_HASH', 'f6aa508be270f5b53c812fd043a08f7d')
BOT_TOKEN = environ.get('BOT_TOKEN', '8165740581:AAG-kWuF5OEzFwY6mL4OpQFzfCXPGS3VEfw')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6558711318 6398757880').split()]
USERNAME = environ.get('USERNAME', "https://t.me/HatakeKakashi41") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002316391931'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+nLQ95TjVtdpjYjQ9')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002485842996').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv:learningbots.5yddr.mongodb.net/?retryWrites=true&w=majority&appName=learningbots")
DATABASE_NAME = environ.get('DATABASE_NAME', "Best")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '0'))  
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','0'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','0'))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))
auth_channel = environ.get('AUTH_CHANNEL', '-1002411427044')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002296085829')
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '0'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/HatakeKakashi41') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/TNMCartoon")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://envs.sh/sUl.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "7093f846c0cb92afe2a6b65b7581f835f7a39b21")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'modijiurl.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "7093f846c0cb92afe2a6b65b7581f835f7a39b21")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'modijiurl.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "7093f846c0cb92afe2a6b65b7581f835f7a39b21")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'modijiurl.com')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["english", "tamil"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://graph.org/file/2789c7daf8b6a83d6cc03-5c0e6aa2f2084c6bdf.jpg https://envs.sh/sUl.jpg https://graph.org/file/f5926290105be984c2e06-e362ab311534b56ca4.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://envs.sh/sUl.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/sUl.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://envs.sh/sUl.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://envs.sh/sUl.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
