from pyrogram.types import Message


def human_readable_size(size, decimal_places=2):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024.0:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024.0
    return f"{size:.{decimal_places}f} PB"


async def edit_progress(message: Message, downloaded, total):
    if total:
        percent = downloaded * 100 / total
        text = f"Downloading... {percent:.2f}% — {human_readable_size(downloaded)} / {human_readable_size(total)}"
    else:
        text = f"Downloading... {human_readable_size(downloaded)}"
    try:
        await message.edit_text(text)
    except Exception:
        pass
