"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	**VIP3**
	Daily Upload limit 100GB
	Price Rs 150  🇮🇳/🌎 1.81$  per Month
	
	
	Pay Using Upi I'd ```lokamandc1224@oksbi```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrlokaman")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/lokamanchendekar"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/los89jy0")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """<b>**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	**VIP3**
	Daily Upload limit 100GB
	Price Rs 150  🇮🇳/🌎 1.81$  per Month
	
	
	Pay Using Upi I'd ```655365838@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🙋",url = "https://t.me/haashim_999")], 
        			[InlineKeyboardButton("Paytm💰",url = "https://p.paytm.me/xCTH/dtvlquzy")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
