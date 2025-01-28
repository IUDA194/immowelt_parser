import sqlite3

def setup_database():
    conn = sqlite3.connect("flats.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flats (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        address TEXT,
                        link TEXT UNIQUE,
                        price TEXT,
                        details TEXT,
                        image_url TEXT
                    )''')
    conn.commit()
    return conn

def is_flat_new(conn, link):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flats WHERE link = ?", (link,))
    return cursor.fetchone() is None

def save_flat(conn, flat):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flats (address, link, price, details, image_url) VALUES (?, ?, ?, ?, ?)",
                   (flat['address'], flat['link'], flat['price'], flat['details'], flat['image_url']))
    conn.commit()

