import os
from pyrogram import Client
from config import BOT_TOKEN
from helpers.logger import logger

if not BOT_TOKEN:
    raise RuntimeError('Please set BOT_TOKEN in the environment or .env file')

app = Client('terabox_bot', bot_token=BOT_TOKEN)

# Import plugins so handlers register
from plugins import start, terabox, progress  # noqa: F401


if __name__ == '__main__':
    logger.info('Starting TeraBox Downloader Bot')
    app.run()
