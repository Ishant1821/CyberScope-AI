import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), 'cyberscope.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # 1. Existing Incidents Table
    c.execute('''CREATE TABLE IF NOT EXISTS incidents
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  sensor_id TEXT,
                  temperature REAL,
                  voltage REAL,
                  timestamp TEXT,
                  classification TEXT)''')
                  
    # 2. NEW: Users Table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )''')
                
    # 3. Create default admin if it doesn't exist
    c.execute("SELECT * FROM users WHERE username='admin'")
    if not c.fetchone():
        hashed_pw = generate_password_hash('admin123')
        c.execute("INSERT INTO users (username, password_hash) VALUES ('admin', ?)", (hashed_pw,))
        
    conn.commit()
    conn.close()

def log_incident(sensor_id, temp, volt, timestamp, classification):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO incidents (sensor_id, temperature, voltage, timestamp, classification) VALUES (?, ?, ?, ?, ?)",
              (sensor_id, temp, volt, timestamp, classification))
    conn.commit()
    conn.close()

def get_incidents():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM incidents")
    rows = c.fetchall()
    conn.close()
    return rows

def clear_incidents():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM incidents')
    c.execute('DELETE FROM sqlite_sequence WHERE name="incidents"')
    conn.commit()
    conn.close()

# NEW: Helper functions for user authentication
def get_user_by_username(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user