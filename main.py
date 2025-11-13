import os
from pyrogram import Client
from config import BOT_TOKEN
from helpers.logger import logger

# Load API ID & API HASH manually
API_ID = int(os.getenv("API_ID", 22107616))
API_HASH = os.getenv("API_HASH", "6629084d27f421f2375a57f233e471e2")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing!")

app = Client(
    "terabox_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Import plugins
from plugins import start, terabox, progress  # noqa

if __name__ == "__main__":
    logger.info("Starting TeraBox Downloader Bot...")
    app.run()
