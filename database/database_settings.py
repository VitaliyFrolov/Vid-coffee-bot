import sqlite3

db = sqlite3.connect('./database/vid_coffee.db', check_same_thread=False)

db_cursor = db.cursor()

db_cursor.execute("""CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone_number TEXT,
    tg_id INTEGER,
    coffee_point INTEGER DEFAULT 0,
    free_coffee INTEGER DEFAULT 0
)""")

db_cursor.execute("""
CREATE TRIGGER IF NOT EXISTS update_free_coffee
AFTER UPDATE OF coffee_point ON cards
WHEN NEW.coffee_point >= 6
BEGIN
UPDATE cards
SET free_coffee = free_coffee + 1,
coffee_point = coffee_point - 6
WHERE id = NEW.id;
END;
""")

db_cursor.execute("""CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER         
)""")

db.commit()
db.close()
