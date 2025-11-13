from pyrogram import filters
from pyrogram.types import Message
from main import app
from config import ADMIN_IDS


@app.on_message(filters.command('start') & filters.private)
async def start_cmd(client, message: Message):
    text = (
        "Hi! I'm your personal TeraBox downloader bot.\n\n"
        "Send me a TeraBox share link and I'll try to download it using the cookies.txt in the project root.\n\n"
        "Commands:\n"
        "/start - this message\n"
        "/status - checks bot status\n"
        "/help - usage\n"
    )
    await message.reply_text(text)


@app.on_message(filters.command('status') & filters.user(ADMIN_IDS))
async def status_cmd(client, message: Message):
    await message.reply_text('Bot is running ✅')
