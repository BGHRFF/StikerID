import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

Bot = Client(
    "StickerIdBot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
 
   
START_TEXT = """
Salam {},
Mən Stiker Paketlərin ID-sin tapan botam. 
Mən stikerdən onun id-sin tapa bilərəm. Sadəcə mənə bir stiker göndərin, mən sizə onun id-sin deyim. 
"""
    
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Sahibim 📕', url='t.me/TheBaghirov'), 
        InlineKeyboardButton('Yeniliklər Kanalımız📕', url=f"https://telegram.me/{Config.CHANNEL}")
        ]]
    )

@Bot.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"İstədiyiniz Stikerin ID-si    * `{message.sticker.file_id}` *", quote=True)
   
Bot.run()
