
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 24930902 # integer value, dont use ""
    API_HASH = "13ab12fe1f3ecce86ac52b4c6c662f81"
    TOKEN = "6548824436:AAF5QtjsNqiv9OwF6EHotluNmp8XfkMa7Us"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 2006156742 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "-4176933173"  # Your own group for support, do not add the @
    START_IMG = "https://id.pinterest.com/pin/520306563204995674/"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://guimanage14:BnYCaTEcTnkWxEVQ@cluster0.ylagj6l.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://wpmbbjfm:QDiX48aMyWOz0GIUtYzq96IMRiSv3YyC@rain.db.elephantsql.com/wpmbbjfm"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "4SR9UQ224AON4294"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "PEV3WLHPGI2V"
    
    # Get your API key from https://timezonedb.com/api
    API_KEY="2006156742-mukesh-api-|"
    #generate api from telegram using /token command bot username :>> @adventure_robot

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
