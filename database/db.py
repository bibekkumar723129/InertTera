# Minimal SQLite tracker for future use
import sqlite3
from pathlib import Path

DB_PATH = Path('database/bot.db')
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS downloads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    url TEXT,
    filename TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()


def add_download(user_id, url, filename, status='started'):
    cur.execute('INSERT INTO downloads (user_id,url,filename,status) VALUES (?,?,?,?)', (user_id,url,filename,status))
    conn.commit()
    return cur.lastrowid
