def test_successfully_inserts_multiple_urls(self):
    """Successfully inserts multiple URLs into the SQLite database"""
    import sqlite3
    from datetime import datetime
    import uuid
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite

    # Prepare test data
    urls = ['http://example1.com', 'http://example2.com']

    # Call the function
    save_tabs_to_sqlite(urls)

    # Connect to the database to check inserted data
    conn = sqlite3.connect('firefox_tabs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tabs')
    rows = cursor.fetchall()

    # Check if all URLs were inserted
    assert len(rows) == len(urls)

    # Clean up
    conn.close()