def test_creates_new_sqlite_db_file(self):
    """Successfully creates a new SQLite database file if it doesn't exist"""
    import os
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite

    db_file = 'firefox_tabs.db'

    # Ensure the database file does not exist before the test
    if os.path.exists(db_file):
        os.remove(db_file)

    # Call the function
    save_tabs_to_sqlite(['http://example.com'])

    # Check if the database file was created
    assert os.path.exists(db_file)

    # Clean up
    if os.path.exists(db_file):
        os.remove(db_file)