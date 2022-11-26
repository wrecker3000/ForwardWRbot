#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 2131008
API_HASH = "13d24696f0d535d24ae565f4625d65a2"
BOT_TOKEN = "1826680035:AAEIICer_COLsglV2QOcXWookjpJXrch-6k"
SESSION = "1BVtsOJ4Bu7nOfN9PjGJL2_IqVgTM5hqQ-uJA-XMxosJ5jtjAtSVs9F7XHII_93eZjbzwh3MGdpLE204bGeTBctIJckzdYZ0K3gn0s2LmvfC5Ajl3RbCwcE25uoZa8WZKXwWOkI7pcRNuIg0y3thu7FmynLtB68L2wunMj4D2p_t6uS5rKBnxDzkIdf5msi2YutHwQ6wsTUKWUCkdJ_N9hckuevapNW31J_vl7OgWG-1AL3bSAAsvccDnImh3gUGEr23ow3RNkRiu3x8biGA0HAD94WeB2jRtC6RC0PUd0z9zQb4hobtgxCLGMyS3pdyByYldK8NrSueHdbwcNTHcI1_SrZAo8uo="
FORCESUB = ""
AUTH = ""

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
