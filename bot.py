import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5759212584:AAHt_BtGwB9xaORga9hX8jb0zUl50xoPAyQ")

API_ID = int(os.environ.get("API_ID", "23223511"))

API_HASH = os.environ.get("API_HASH", "c2207a11155ad050097e981fdd5fd0b1")

STRING = os.environ.get("STRING", "BQCvL9oONeonVdwPOyfuAQSJcrfYg0whrRVpfm8qgIsvFzm124fasi_2Mkh7ul--Gu-RVgqnc9htb7qQfjZ7_OuAZR7cdNPvLYr6nRWSQFu7_paoOhxEOyWE987iBUtegfkAvc4l-yByvOAY4PaF2enmjPNFvW4d55R2nWNbPFHpRt8jneSrKDT_NbmYW1mkEqfNhfk6K8PR6iCCT417JyNb3RHMsGObzMmsCGOXWAtEe16dg4T1TdzXjKfQSrp-aPHoH4BlBCmzG7O_y8UMzeH4QXBoitZUOULs1A46xEhHnjUjdgG3DISgAe3KHOJMeIR9HUKLgWQ3NFNOfMwWhtq-AAAAAS0MIIwA")


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
