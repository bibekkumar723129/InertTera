import os
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from main import app
from helpers.cookies_loader import load_cookies
from helpers.terabox_api import resolve_terabox_link
from helpers.downloader import download_to_file
from plugins.progress import edit_progress
from helpers.logger import logger
from config import MAX_FILE_SIZE


@app.on_message(filters.private & filters.text)
async def handle_link(client, message: Message):
    text = message.text.strip()
    # simple check: must contain terabox or 115.com or share url
    if 'terabox' not in text and '115.com' not in text:
        return

    msg = await message.reply_text('Resolving link...')
    cookies = load_cookies()
    resolved = resolve_terabox_link(text, cookies)
    if not resolved:
        await msg.edit_text('❌ Could not resolve a direct download link. The page may require JS or an unsupported flow.')
        return

    # Try to get content-length
    # We'll download to file then upload
    try:
        async def progress_cb(downloaded, total):
            await edit_progress(msg, downloaded, total)
        # Synchronously call the async download_to_file with a tiny wrapper
        # Because progress_cb is async, adapt to sync callback
        def cb_sync(downloaded, total):
            try:
                asyncio.create_task(progress_cb(downloaded, total))
            except Exception:
                pass

        filename = os.path.basename(resolved.split('?')[0]) or 'downloaded.file'
        tmp_file = await download_to_file(resolved, filename, cookies=cookies, progress_cb=cb_sync)

        # Check size before upload
        size = os.path.getsize(tmp_file)
        if size > MAX_FILE_SIZE:
            await msg.edit_text(f'⚠️ File is too large ({size} bytes). MAX_FILE_SIZE limit reached.')
            return

        await msg.edit_text('Uploading to Telegram...')
        await client.send_document(chat_id=message.chat.id, document=tmp_file, caption=filename)
        await msg.delete()
    except Exception as e:
        logger.exception('Error in handle_link: %s', e)
        await msg.edit_text('❌ Failed: ' + str(e))
