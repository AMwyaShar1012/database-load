import sqlite3

def create_database():
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE files
                 (id INTEGER PRIMARY KEY, name TEXT, content TEXT)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created")
