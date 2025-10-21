def test_handles_special_characters_in_urls(self):
    """# Handles URLs with special characters"""
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite
    import os

    db_file = 'firefox_tabs.db'

    # Ensure the database file does not exist before the test
    if os.path.exists(db_file):
        os.remove(db_file)

    # Call the function with URLs containing special characters
    save_tabs_to_sqlite(['http://example.com', 'https://site.com/?q=1&param=2'])

    # Check if the database file is created
    assert os.path.exists(db_file)

    # Clean up
    if os.path.exists(db_file):
        os.remove(db_file)