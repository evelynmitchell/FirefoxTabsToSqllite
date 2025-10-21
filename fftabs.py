import os
import json
import sqlite3
import uuid
from datetime import datetime

def get_firefox_tabs():
    # Path to Firefox's session store file (adjust for your OS)
    firefox_path = os.path.expanduser('~/.mozilla/firefox')
    profiles_path = os.path.join(firefox_path, 'profiles.ini')
    
    with open(profiles_path, 'r') as f:
        for line in f:
            if line.startswith('Path='):
                profile = line.split('=')[1].strip()
                break
    
    session_store_path = os.path.join(firefox_path, profile, 'sessionstore.jsonlz4')
    
    # Read and decompress the session store file
    import lz4.block
    with open(session_store_path, 'rb') as f:
        data = f.read()
        if data[:8] == b'mozLz40\0':
            content = lz4.block.decompress(data[8:])
        else:
            content = data
    
    session = json.loads(content)
    
    urls = []
    for window in session.get('windows', []):
        for tab in window.get('tabs', []):
            entry = tab['entries'][-1]
            urls.append(entry['url'])
    
    return urls

def save_tabs_to_sqlite(urls):
    conn = sqlite3.connect('firefox_tabs.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tabs
    (uniqueid TEXT PRIMARY KEY, date TEXT, url TEXT)
    ''')
    
    # Insert data
    current_date = datetime.now().isoformat()
    for url in urls:
        cursor.execute('''
        INSERT INTO tabs (uniqueid, date, url) VALUES (?, ?, ?)
        ''', (str(uuid.uuid4()), current_date, url))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    urls = get_firefox_tabs()
    save_tabs_to_sqlite(urls)
    print(f"Saved {len(urls)} tabs to the SQLite database.")