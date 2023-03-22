from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os

CHANNEL = os.environ.get('CHANNEL', "")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", 1484670284))
bot_username = os.environ.get("BOT_USERNAME","GangsterBaby_renamer_BOT")
log_channel = int(os.environ.get("LOG_CHANNEL", ""))
token = os.environ.get('TOKEN', '')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "🤙"
elif 12 <= currentTime.hour < 12:
    wish = '👋'
else:
    wish = '✌️'

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""ʜᴇʟʟᴏ{wish} {message.from_user.first_name } \n
	ᴛʜɪs  ɪs  ᴀ  ғᴀsᴛ⚡  4ɢʙ  ʀᴇɴᴀᴍᴇʀ  ʙᴏᴛ🤖  ᴡɪᴛʜ  ᴍᴜʟᴛɪ  ғᴇᴀᴛᴜʀᴇs . ʏᴏᴜ  ᴄᴀɴ  ᴇᴅɪᴛ🖌️  10  ғɪʟᴇs  sɪᴍᴜʟᴛᴀɴᴏᴜsʟʏ💡 .\n\nsᴇɴᴅ  ғɪʟᴇ  ᴏʀ ᴠɪᴅᴇᴏ  ᴛᴏ  ᴇᴅɪᴛ \n\nᴜsᴇ /FEATURES ᴄᴏᴍᴍᴀɴᴅ  ᴛᴏ  ᴄʜᴇᴄᴋ  ᴛʜɪs  ʙᴏᴛs  ғᴇᴀᴛᴜʀᴇs"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("🖌️HOW TO EDIT", url="https://t.me/LazyDeveloper")],
                                      [InlineKeyboardButton("DEVELOPER🛸", url="https://t.me/F9Devs"),
                                       InlineKeyboardButton("GET PREMIUM👑", url='https://cosmofeed.com/vig/6410a3933702d700208ace5b')],
                                      [InlineKeyboardButton("WATCH MOVIES🍿", url='https://t.me/MOVIEBEEZ'),
                                       InlineKeyboardButton("HELP🥲", url='https://t.me/CALLADMIN_beebot')]
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "Your Friend is Already Using Our Bot")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("🖌️HOW TO EDIT", url="https://t.me/LazyDeveloper")],
                                              [InlineKeyboardButton("DEVELOPER🛸", url="https://t.me/F9Devs"),
                                               InlineKeyboardButton("GET PREMIUM👑", url='https://cosmofeed.com/vig/6410a3933702d700208ace5b')],
                                             [InlineKeyboardButton("WATCH MOVIES🍿", url='https://t.me/MOVIEBEEZ'),
                                              InlineKeyboardButton("HELP🥲", url='https://t.me/CALLADMIN_beebot')]
                                          ]))
            except:
                return
        else:
            await client.send_message(id, "🎉ᴄᴏɴɢʀᴀᴛᴇs ! ʏᴏᴜ ᴡᴏɴ 500 ᴍʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ ғʀᴏᴍ ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ \n\nʀᴇғᴇʀ🎟️  ᴀɢᴀɪɴ  ᴛᴏ  ᴡɪɴ😀")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 536870912
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	ʜᴇʟʟᴏ{wish} {message.from_user.first_name }\n\n
	ᴛʜɪs  ɪs  ᴀ  ғᴀsᴛ⚡  4ɢʙ  ʀᴇɴᴀᴍᴇʀ  ʙᴏᴛ🤖  ᴡɪᴛʜ  ᴍᴜʟᴛɪ  ғᴇᴀᴛᴜʀᴇs . ʏᴏᴜ  ᴄᴀɴ  ᴇᴅɪᴛ🖌️  10  ғɪʟᴇs  sɪᴍᴜʟᴛᴀɴᴏᴜsʟʏ💡 .\n\nsᴇɴᴅ  ғɪʟᴇ  ᴏʀ ᴠɪᴅᴇᴏ  ᴛᴏ  ᴇᴅɪᴛ \n\nᴜsᴇ /FEATURES ᴄᴏᴍᴍᴀɴᴅ  ᴛᴏ  ᴄʜᴇᴄᴋ  ᴛʜɪs  ʙᴏᴛs  ғᴇᴀᴛᴜʀᴇs
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🖌️HOW TO EDIT", url="https://t.me/LazyDeveloper")],
                                          [InlineKeyboardButton("DEVELOPER🛸", url="https://youtube.com/F9Devs"),
                                           InlineKeyboardButton("GET PREMIUM👑", url='https://cosmofeed.com/vig/6410a3933702d700208ace5b')],
                                          [InlineKeyboardButton("WATCH MOVIES🍿", url='https://t.me/MOVIEBEEZ'),
                                           InlineKeyboardButton("HELP🥲", url='https://t.me/CALLADMIN_beebot')]
                                          ]))
    


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**__YOU ARE NOT SUBSCRIBE MY UPDATE CHANNEL \n\nJOIN👇🏻 AND SEND ME FILE AGAIN😊__** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🛸UPDATE CHANNEL🛸", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"🦋 #F9 RENAMER BOTS LOG 🦋,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Restrict User ( **pm** ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("Use About cmd first /about")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"𝙷𝙴𝙻𝙻𝙾 {message.from_user.first_name} 𝙳𝚄𝙴  𝚃𝙾  𝙾𝚅𝙴𝚁𝙻𝙾𝙰𝙳 . 𝙾𝙽𝙻𝚈  𝙾𝚄𝚁  𝚅𝙴𝚁𝙸𝙵𝙸𝙴𝙳  𝚄𝚂𝙴𝚁  𝙲𝙰𝙽  𝚄𝚂𝙴  𝚃𝙷𝙸𝚂  𝙱𝙾𝚃 . \n\n𝙸𝙵  𝚈𝙾𝚄  𝚆𝙰𝙽𝚃  𝚃𝙾  𝚄𝚂𝙴  𝚃𝙷𝙸𝚂  𝙱𝙾𝚃  𝙾𝙽  𝙳𝙰𝙸𝙻𝚈  𝙱𝙰𝚂𝙸𝚂  𝚃𝙷𝙴𝙽  𝚂𝙴𝙽𝙳 **/UPGRADE** 𝙲𝙾𝙼𝙼𝙰𝙽𝙳  𝙰𝙽𝙳  𝙲𝙷𝙾𝙾𝚂𝙴  𝙿𝚁𝙴𝙵𝙴𝚁𝙴𝙳  𝙿𝙻𝙰𝙽 .\n\n𝗱𝗼𝗻'𝘁 𝘄𝗼𝗿𝗿𝘆 𝘄𝗲 𝗵𝗮𝘃𝗲 𝗮 𝗳𝗿𝗲𝗲 𝗽𝗹𝗮𝗻 𝗮𝗹𝘀𝗼🤠",
                                  reply_markup=InlineKeyboardMarkup([
                                                                     [InlineKeyboardButton("DEVELOPER🛸", url='https://telegram.me/F9Devs')],
                                                                     [InlineKeyboardButton("ANY HELP🥲", url='https://t.me/CALLADMIN_beebot')]
                                                                    ]))
        await message.reply_text(text=f"🚀")
        return 

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 60
    else:
        LIMIT = 5
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"**100% of daily {humanbytes(limit)} data quota exhausted.\n\n  File size detected {humanbytes(file.file_size)}\n  Used Daily Limit {humanbytes(used)}\n\nYou have only **{humanbytes(remain)}** left on your Account.\nIf U Want to Rename Large File Upgrade Your Plan👇🏻 \n\nYou can refer this bot and earn upto 5gb upload limit . use /REFER command to refer** ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daily Limit {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rename", callback_data="rename"), InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 1610612736)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Your Plan Expired On {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Can't upload files bigger than 2GB ")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 1610612736)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rename", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))

