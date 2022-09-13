#ʀᴏʙɪɴ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴠᴄ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ ɴᴏ ʟᴀɢ

#ᴅᴇᴠᴇʟᴏᴘᴇʀs :- @SIXTH_H0KAGE & @GodlyDemxn
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Mikasa Ackerman ♡ 振")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "𝓚𝒶кคѕⒽᎥ ђ𝔞𝓉ᗩЌ𝒆")
OWNER_USERNAME = getenv("OWNER_USERNAME", "SIXTH_H0KAGE")
ALIVE_NAME = getenv("ALIVE_NAME", "Mikasa Ackerman ♡ 振")
BOT_USERNAME = getenv("BOT_USERNAME","MisakaXmanagementBot")
OWNER_ID = getenv("OWNER_ID","1937701729")
ASSISTANT_NAME = getenv("ASSISTANT_NAME","eren yeager")
GROUP_SUPPORT = getenv("GROUP_SUPPORT","kakashi_bots_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","kakashi_bots_updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1937701729").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/db09d094f55e3508bc172.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/db09d094f55e3508bc172.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/otakubinge/Robin-Music-Robot")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/880f7e9706591af8d0bfa.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/324399325cf48ff25a494.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
