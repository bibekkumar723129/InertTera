# Parses Netscape cookies.txt format into a requests.Session cookiejar (dict-like)
import os
from http.cookiejar import MozillaCookieJar
from pathlib import Path
from helpers.logger import logger

COOKIES_PATH = Path('cookies.txt')


def load_cookies():
    """Return dict of cookie name -> value. If cookies.txt missing, return {}."""
    if not COOKIES_PATH.exists():
        logger.warning('cookies.txt not found in project root.')
        return {}
    cj = MozillaCookieJar()
    try:
        cj.load(str(COOKIES_PATH), ignore_discard=True, ignore_expires=True)
    except Exception as e:
        logger.exception('Failed to load cookies.txt: %s', e)
        return {}
    cookies = {c.name: c.value for c in cj}
    logger.info('Loaded %d cookies', len(cookies))
    return cookies
