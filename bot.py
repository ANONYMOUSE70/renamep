import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5945219564:AAHNUQJuBMGsjQgzXg-p_wB-FrHhO9PqfMQ")

API_ID = int(os.environ.get("API_ID", "14505719"))

API_HASH = os.environ.get("API_HASH", "620f0a2aa2cd1474a4953619b3e3643d")

STRING = os.environ.get("STRING", "BQDdVvcAdt14LBDXbPsaSVDzu5ItcZdgQEcbPzDjUx0AsRDTkj5SA25Zr4TpmW_I7y6D1HnfHEU3WBiDEMKINLU1b0E7Sn6q_kjA5DR_CuLv8AhZMktat9VabjT63FDZG2-Lb9IfJ7mV_q8Wn5hm10TvvI6sPbB0CYDagOioSRAZ9P-vUSu6V2l-5rDnfp6wxISJn-U9EpgRt6HED_e7UnlcZXZadLo_h8BFgwzWjDJlW4fYoBgNaF_cwzYNCqbzJgiA-dU3Q-6Su_UZG-50VGelibC8flyIMHvV0mlz_yTDtR4PlBrkj97iqtCQRFwR7JEUC6mmOKShiIqzQaiVRBNYsbNwZQAAAAE7Z4AQAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
