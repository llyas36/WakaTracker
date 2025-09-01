import sqlite3
import datetime

DB_FILE = "waka_users.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            api_key TEXT NOT NULL,
            last_update TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_api_key(telegram_id: int, api_key: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (telegram_id, api_key, last_update)
        VALUES (?, ?, ?)
        ON CONFLICT(telegram_id) DO UPDATE SET
            api_key=excluded.api_key,
            last_update=excluded.last_update
    """, (telegram_id, api_key, datetime.datetime.now()))
    conn.commit()
    conn.close()

# <--- Add this function
def get_api_key(telegram_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT api_key FROM users WHERE telegram_id=?", (telegram_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
