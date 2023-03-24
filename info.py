import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5759212584:AAHt_BtGwB9xaORga9hX8jb0zUl50xoPAyQ")

API_ID = int(os.environ.get("API_ID", "23223511"))

API_HASH = os.environ.get("API_HASH", "c2207a11155ad050097e981fdd5fd0b1")

STRING = os.environ.get("STRING", "BQCeWP2LGfkD32LcuT0KI2WNiK9mY0S33v85zMiHteXPMq7_E4pNHlASNjJI0vhaWDLOoNhOSSZnRLPrg59EJ2a8NrRj1cCWJp1Gs-_J8xBeh8TXEnHKnJsvfb8a3yn7jC_x_KReL3EaKGgFkRWR9eo3N-bqVi70DkhkDfM0EiXkxoDrnbPaCz_n-LYIZyTZ6733FZhxs0T7f-h27ckmwuewM24ZXM7U-VPz9ZhUGoCB7CxFT5DPEpRQ8ZlMC32YJOJC6GZQL_421p8JZDUcyCO-zOB1ErOC9L_7QgE-ml5aKDW-nWMBzr-8k_A4G-ANWt7z_H2apIbW8UiH-fByZZHcAAAAAWzPgu4A")

