import sqlite3

def init_db():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        password TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY,
        room_id INTEGER,
        device_id TEXT,
        FOREIGN KEY (room_id) REFERENCES rooms (id)
    )
    ''')
    conn.commit()
    conn.close()

def add_room(name, password):
    try: 
        conn = sqlite3.connect('devices.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO rooms (name, password) VALUES (?, ?)', (name, password))
        conn.commit()
    except sqlite3.IntegrityError:
        raise Exception('Room already exists')
    finally:
        conn.close()
        
def get_rooms():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM rooms')
    rooms = cursor.fetchall()
    conn.close()
    return rooms

def add_device(room_id, device_id):
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO devices (room_id, device_id) VALUES (?, ?)', (room_id, device_id))
    conn.commit()
    conn.close()

def get_room(name):
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms WHERE name = ?', (name,))
    room = cursor.fetchone()
    conn.close()
    return room

def get_devices(room_id):
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT device_id FROM devices WHERE room_id = ?', (room_id,))
    devices = cursor.fetchall()
    conn.close()
    return devices

init_db()
