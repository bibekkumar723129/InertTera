import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')  # Required
ADMIN_IDS = list(map(int, os.getenv('ADMIN_IDS','').split())) if os.getenv('ADMIN_IDS') else []
DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR','downloads')
LOG_FILE = os.getenv('LOG_FILE','logs/bot.log')

# Optional limits
MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 10 * 1024 * 1024 * 1024))  # 10 GB default

# User-agent for requests
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
