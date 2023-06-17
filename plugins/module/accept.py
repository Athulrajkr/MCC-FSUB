from pyrogram.types import Message
from pyrogram import filters, Client, errors, enums
from database.users_chats_db import db


@Client.on_chat_join_request(filters.group | filters.channel)
async def approve(bot, m: Message):
    try: 
        if not await db.get_chat(message.chat.id):
            await db.add_chat(m.chat.id, m.chat.title) 
        await bot.approve_chat_join_request(message.chat.id, m.from_user.id)
        await bot.send_message(m.from_user.id, "Hello {}\nWelcome To {}".format(m.from_user.mention, m.chat.title))
        if not await db.is_user_exist(m.from_user.id):
            await db.add_user(m.from_user.id, m.from_user.first_name) 
    except errors.PeerIdInvalid as e:
       print("user isn't start bot")
    except Exception as err:
        print(str(err))    
      
