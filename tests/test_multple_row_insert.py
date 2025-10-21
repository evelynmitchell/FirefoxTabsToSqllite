def test_inserts_multiple_urls_with_unique_ids_and_current_date(self):
    """ Inserts multiple URLs into the 'tabs' table with unique IDs and current date"""
    import sqlite3
    from datetime import datetime
    import uuid
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite

    # Prepare test data
    urls = ['http://example1.com', 'http://example2.com']

    # Call the function to insert URLs
    save_tabs_to_sqlite(urls)

    # Check if the data is inserted correctly
    conn = sqlite3.connect('firefox_tabs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tabs')
    result = cursor.fetchall()
    conn.close()

    # Assert the number of rows inserted
    assert len(result) == len(urls)

    # Assert unique IDs and current date
    for row in result:
        assert isinstance(row[0], str)  # Check uniqueid is a string
        assert isinstance(row[1], str)  # Check date is a string
        assert row[2] in urls  # Check URL is in the original list