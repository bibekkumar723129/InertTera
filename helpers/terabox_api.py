import requests
from urllib.parse import urlparse
from helpers.logger import logger
from config import USER_AGENT


HEADERS = {'User-Agent': USER_AGENT}


def resolve_terabox_link(shared_url, cookies: dict):
    """Try to resolve a TeraBox share link to a direct downloadable link.

    Approach:
    - Try a GET request with cookies and follow redirects
    - If response contains JSON or redirect to a file, return final URL
    - This is a best-effort implementation — some TeraBox links require JS.
    """
    try:
        s = requests.Session()
        s.headers.update(HEADERS)
        if cookies:
            s.cookies.update(cookies)
        # first try a HEAD to get redirect
        resp = s.head(shared_url, allow_redirects=True, timeout=30)
        final = resp.url
        # if HEAD returns a direct file or redirect ends in a file, return
        if is_probably_file_url(final):
            logger.info('Resolved direct url via HEAD: %s', final)
            return final

        # fallback: try GET and inspect
        resp = s.get(shared_url, allow_redirects=True, timeout=30)
        final = resp.url
        if is_probably_file_url(final):
            logger.info('Resolved direct url via GET: %s', final)
            return final

        # sometimes the page contains a JSON link or a downloadable endpoint
        text = resp.text
        # quick heuristic: look for "download" or .apk/.zip/.mp4 etc in page
        for ext in ['.zip', '.rar', '.mp4', '.mkv', '.apk', '.jpg', '.png']:
            if ext in final.lower() or ext in text.lower():
                logger.info('Heuristic found file pattern; returning final: %s', final)
                return final

        logger.warning('Could not reliably resolve a direct file URL for: %s', shared_url)
        return None
    except Exception as e:
        logger.exception('Error resolving terabox link: %s', e)
        return None


def is_probably_file_url(url: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path.lower()
    return any(path.endswith(ext) for ext in ('.zip', '.rar', '.mp4', '.mkv', '.apk', '.jpg', '.png', '.7z', '.tar', '.gz'))
