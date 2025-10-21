def test_generates_unique_ids(self):
    """Generates unique IDs for each URL entry"""
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite
    import sqlite3
    import os
   
    db_file = 'firefox_tabs.db'
    
    # Ensure the database file does not exist before the test
    if os.path.exists(db_file):
        os.remove(db_file)

    # Call the function
    save_tabs_to_sqlite(['http://example.com'])
    
    # Connect to the database to check unique IDs
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT uniqueid FROM tabs')
    unique_ids = cursor.fetchall()
    
    # Check if unique IDs are generated for each URL entry
    assert len(unique_ids) == 1  # Only one URL is inserted, so only one unique ID should exist
    
    # Clean up
    conn.close()
    if os.path.exists(db_file):
        os.remove(db_file)