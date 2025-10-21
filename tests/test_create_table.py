def test_creates_new_table_if_not_exist(self):
    """ Successfully creates a new table in the SQLite database if it doesn't exist"""
    import os
    import sqlite3
    from datetime import datetime
    import uuid
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite

    db_file = 'firefox_tabs.db'

    # Ensure the database file does not exist before the test
    if os.path.exists(db_file):
        os.remove(db_file)

    # Call the function
    save_tabs_to_sqlite(['http://example.com'])

    # Check if the table was created
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tabs'")
    result = cursor.fetchone()
    assert result is not None

    # Clean up
    conn.close()
    if os.path.exists(db_file):
        os.remove(db_file)