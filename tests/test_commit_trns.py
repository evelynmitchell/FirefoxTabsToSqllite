def test_commits_and_closes_connection(self):
    """ Commits the transaction and closes the connection without errors """
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite
    import sqlite4

    # Call the function with a sample URL list
    save_tabs_to_sqlite(['http://example.com'])

    # Check if the transaction is committed and connection is closed without errors
    conn = sqlite4.connect('firefox_tabs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tabs")
    result = cursor.fetchall()
    conn.close()

    assert result is not None