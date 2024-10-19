from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from pyrogram import *
from configs.telegram import api_id,api_hash,bot_token,bot_name
from configs.firebase import firebase_config
import uuid
from modules.ftwilio import send_sms
import pyrebase
from templates.start import start_msg

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()
app = Client(bot_name,api_id=api_id,api_hash=api_hash,bot_token=bot_token)

button = InlineKeyboardMarkup(
                             [
            [InlineKeyboardButton(f'Close', callback_data=f'close')],
            [InlineKeyboardButton(f'Confirm', callback_data=f'confirm')],
                   ] 
                             )

@app.on_message(filters.command('start'))
async def start_msg(client,message):
    name=str(message.from_user.first_name)
    try:
        user_id = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        user_name = str(message.from_user.username)
        user_data = {"name":first_name,"username":user_name}
        new_userdb = db.child("users").child(user_id).set(user_data)
        print(new_userdb)
        await message.reply(f"__**Hey {name}👋🏻**\n\nI'm **Twilio Bot**\n\n{start_msg}")
    except:
        pass
    
@app.on_message(filters.command('send'))
async def start_msg(client,message):
    name=str(message.from_user.first_name)
    text = message.text
    text = text.replace("/send", "").strip()
    parts = text.split(" ", 1)
    phone_number = str(parts[0]).replace("+","")
    user_message = parts[1] if len(parts) > 1 else ""
    uidnum = str(uuid.uuid4())
    if not user_message:
            await message.reply("Please provide a message after the phone number❕")
            return
    try:
        user_id = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        user_name = str(message.from_user.username)
        user_data = {"name":first_name,"username":user_name,"phone":phone_number,"message":user_message}
        new_userdb = db.child("logs").child(user_id).child(uidnum).set(user_data)
        await message.reply(f"**Message Confirmation❕**\n\nPhone : {phone_number}\n\nMessage : {user_message}",
                            reply_markup=
                            InlineKeyboardMarkup(
                             [
            [InlineKeyboardButton(f'Close', callback_data=f'close')],
            [InlineKeyboardButton(f'Confirm', callback_data=f'{uidnum}')],
                   ] 
                             ))
    except:
        pass
    
@app.on_callback_query()
async def mailbox(client,message):
    response=message.data
    chat_id = message.message.chat.id
    print(response)
    if response=='close':
        await message.edit_message_text('Session Closed✅')
    else:
        print(chat_id)
        msg_db = db.child("logs").child(chat_id).child(response).get().val()
        phone = msg_db.get("phone")
        texcont = msg_db.get("message")
        send_status = send_sms(phone_number=f"+{phone}",textctn=texcont)
        await message.edit_message_text(f"**Response**\n\n__{send_status}__")
        
app.run()