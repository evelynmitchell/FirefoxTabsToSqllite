def test_correctly_timestamps_urls(self):
    """Correctly timestamps each URL entry with the current date and time"""
    import sqlite3
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite
    from datetime import datetime
    import uuid

    urls = ['http://example.com', 'http://test.com']

    # Call the function
    save_tabs_to_sqlite(urls)

    # Check if the URLs were correctly timestamped
    conn = sqlite3.connect('firefox_tabs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT date FROM tabs')
    dates = cursor.fetchall()
    conn.close()

    current_date = datetime.now().isoformat()
    assert all(date[0] == current_date for date in dates)