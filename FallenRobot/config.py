class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27655368
    API_HASH = "ae4533a2b07c69c0852e95e5df0f415e"

    CASH_API_KEY = "O7G92QZSX7QTUJS3"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://kwdamrpc:VxhmQ_2qUl97gEEoZJpmRd3EzRmj43XF@cornelius.db.elephantsql.com/kwdamrpc"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001849063346)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://msyariputri:msyariputri@cluster0.uyp1r3a.mongodb.net/test?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "ALXELSUPPORT"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6660003586:AAGxyyLA6dSJxUVBYiRnl0tiUZgp54W-PRw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "7I2L37AC6JUD"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1882202047  # User id of your telegram account (Must be integer)

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
