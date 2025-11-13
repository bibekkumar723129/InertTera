import os
import aiohttp
import asyncio
from pathlib import Path
from helpers.logger import logger
from config import DOWNLOAD_DIR

Path(DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)


async def download_to_file(url: str, dest_filename: str, cookies: dict = None, progress_cb=None):
    """Download a URL to a local file asynchronously with progress callback.

    progress_cb(bytes_downloaded, total_bytes) -> None
    """
    dest = Path(DOWNLOAD_DIR) / dest_filename
    temp = dest.with_suffix('.part')
    headers = {'User-Agent': 'python-requests/terabox-bot'}
    try:
        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=None)) as resp:
                resp.raise_for_status()
                total = int(resp.headers.get('Content-Length') or 0)
                logger.info('Starting download: %s (size=%s)', url, total)
                with temp.open('wb') as f:
                    downloaded = 0
                    async for chunk in resp.content.iter_chunked(64*1024):
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)
                        if progress_cb:
                            try:
                                progress_cb(downloaded, total)
                            except Exception:
                                pass
                temp.rename(dest)
                logger.info('Download finished: %s', dest)
                return str(dest)
    except Exception as e:
        logger.exception('Download failed: %s', e)
        if temp.exists():
            temp.unlink(missing_ok=True)
        raise
