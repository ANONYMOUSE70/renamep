import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5945219564:AAHNUQJuBMGsjQgzXg-p_wB-FrHhO9PqfMQ")

API_ID = int(os.environ.get("API_ID", "14505719"))

API_HASH = os.environ.get("API_HASH", "620f0a2aa2cd1474a4953619b3e3643d")

STRING = os.environ.get("STRING", "")

