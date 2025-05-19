import sqlite3

def init_db():
    conn = sqlite3.connect('backend/database/shop.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        items TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    conn.commit()
    c.execute("SELECT COUNT(*) FROM products")
    if c.fetchone()[0] == 0:
        c.executemany("INSERT INTO products (name, price, description) VALUES (?, ?, ?)", [
            ("Смартфон", 19999.99, "6.5-дюймовый дисплей, Android"),
            ("Ноутбук", 49999.99, "Core i5, 16 ГБ RAM, SSD 512 ГБ"),
            ("Наушники", 2999.99, "Bluetooth, шумоподавление")
        ])
        conn.commit()
    conn.close()

def get_product_by_id(product_id):
    conn = sqlite3.connect('backend/database/shop.db')
    c = conn.cursor()
    c.execute("SELECT id, name, price, description FROM products WHERE id = ?", (product_id,))
    product = c.fetchone()
    conn.close()
    return product

