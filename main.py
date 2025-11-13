import os
from pyrogram import Client
from helpers.logger import logger

API_ID = int(os.getenv("API_ID", 2040))
API_HASH = os.getenv("API_HASH", "b18441a1ff607e10a989891a4eaaf88f")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "terabox_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workdir=".",
    sleep_threshold=10,      # ⬅ IMPORTANT
    no_updates=False,
    parse_mode="html"
)

if __name__ == "__main__":
    logger.info("Starting TeraBox Downloader Bot...")
    app.run()
