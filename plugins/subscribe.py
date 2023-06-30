from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ChatJoinRequest
from pyrogram import filters, Client, errors, enums
from database.users_chats_db import db
from info import AUTH_CHANNEL

@Client.on_chat_join_request(filters.group | filters.channel)
async def approve(bot: Client, m: Message):
    user_id = m.from_user.id
    first_name = m.from_user.first_name
    username = m.from_user.username
    date = m.date
    btn = [
        [
            InlineKeyboardButton('🎥 𝐆𝐫𝐨𝐮𝐩 🎥', url='https://t.me/MM_Archives'),
            InlineKeyboardButton('🎥 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🎥', url='http://t.me/Movie_Meadia')
        ]]
    try:
        if m.chat.id != AUTH_CHANNEL:
            await bot.approve_chat_join_request(m.chat.id, user_id)
            await bot.send_message(
                chat_id=m.from_user.id,
                text="Hello {}\n\n Your Request to Join{} has been Approved \n\n Send /start to know more".format(m.from_user.mention, m.chat.title)
                reply_markup=InlineKeyboardMarkup(btn),
                parse_mode=enums.ParseMode.HTML
            )
            if not await db.is_user_exist(m.from_user.id):
                await db.add_user(m.from_user.id, m.from_user.first_name)
        await db.add_req(
            user_id=user_id,
            first_name=first_name,
            username=username,
            date=date
            )
    except errors.PeerIdInvalid as e:
        print("User isn't starting the bot")
    except Exception as err:
        print(str(err))
