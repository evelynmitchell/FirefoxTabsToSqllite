def test_handles_list_of_urls(self):
    """Handles a list of URLs and processes each one correctly"""
    import sqlite3
    from datetime import datetime
    import uuid
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tabs
    (uniqueid TEXT PRIMARY KEY, date TEXT, url TEXT)
    ''')

    # Insert data
    urls = ['http://example.com', 'http://test.com']
    save_tabs_to_sqlite(urls)

    # Check if data is inserted correctly
    cursor.execute('SELECT * FROM tabs')
    rows = cursor.fetchall()
    assert len(rows) == len(urls)

    conn.close()