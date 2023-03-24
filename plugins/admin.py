from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre
ADMIN = int(os.environ.get("ADMIN", 6029941553))
log_channel = int(os.environ.get("LOG_CHANNEL", "1001932495598"))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("💡Select Plan to upgrade...", quote=True, reply_markup=InlineKeyboardMarkup([
		           [
				   InlineKeyboardButton("BASIC🎟️", callback_data="vip1")
				   ], [
					InlineKeyboardButton("SUPER⚡", callback_data="vip2")
				   ], [
					InlineKeyboardButton("DIAMOND💎", callback_data="vip3")
					]]))
        			
@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240
	uploadlimit(int(user_id),10737418240)
	usertype(int(user_id),"**BASIC🎟️**")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 10 GB")
	await bot.send_message(user_id,"👋**THANKS FOR CHOOSING F9 BOTS👾** \n\nYOUR PLAN IS UPGRADED SUCCESSFULLY☑️ TO **BASIC🎟️**.\n**now your😀 daily upload limit is 10GB** \n\nCHECK YOUR PLAN AT /myplan")
	await bot.send_message(log_channel,f"⚡️ Plan Upgraded successfully 💥\n\nHey you are Upgraded To silver. check your plan here /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 53687091200
	uploadlimit(int(user_id), 53687091200)
	usertype(int(user_id),"**SUPER⚡**")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 50 GB")
	await bot.send_message(user_id,"**👋 THANKS FOR SUBSCRIBING F9 BOTS👾** \n\nYOUR PLAN IS UPGRADED SUCCESSFULLY☑️ TO **SUPER⚡** \n**now your😀 daily upload limit is 50GB** \n\nCHECK YOUR PLAN AT /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 107374182400
	uploadlimit(int(user_id), 107374182400)
	usertype(int(user_id),"**DIAMOND💎**")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 100 GB")
	await bot.send_message(user_id,"👋**THANKS FOR SUBSCRIBING F9 BOTS👾** \n\nYOUR PLAN IS UPGRADED SUCCESSFULLY☑️ TO **DIAMOND💎** \n**now your daily upload limit is 100GB \nand you can use premium features** \n\nCHECK YOUR PLAN AT /myplan")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 1610612736
	uploadlimit(int(user_id), 1610612736)
	usertype(int(user_id),"**Free**")
	addpre(int(user_id))
	await update.message.edit("Daily Data limit has been reset successsfully.\nThis account has default 1.2 GB renaming capacity ")
	await bot.send_message(user_id,"Your Daily Data limit has been reset successsfully.\n\nCheck your plan here - /myplan\n- Contact Admin 🦋<a href='https://t.me/F9Devs'>**F9 DEVELOPER🛸**</a>🦋")

