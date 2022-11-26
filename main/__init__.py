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
SESSION = "BQA3NosoJL8QR-6JkZvuhyJWeZqSKlj0UcWtrQh8PtOVX-ofA3n2kMjAY9crkhXQrLBaTLVaBAUb6jpby6cjUzlFtDHfGGjg4o7ECnoUFYex_N758lpoV5359dHD31Ukuj7FIL1ZVXnZZAegOcKiYnhRjOn8lILWvhfIGGo7dK5K2vxQG0ihp9y0UJSKp_V9ppmxYcftQ1t1qaY0ZGYN8acwZRdh_N6UN-OKPPD_dixqIcyLfUWUfInoQ1ntGVa2-dwTVTuXmgcXCY_Tvh_fRgPlEWwDSaYpc9P_skauWQSjCYlYHOG7Qu64NNI49j3R1Su5FMrf5zNdvxwbPIbx4Sq5Ihfl6AA"
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
