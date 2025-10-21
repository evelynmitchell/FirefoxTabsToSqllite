
def test_handles_empty_url_list(self):
    """Handles an empty list of URLs without errors"""
    from FirefoxTabsToSqlLite.fftabs import save_tabs_to_sqlite

    db_file = 'firefox_tabs.db'

    # Ensure the database file does not exist before the test
    if os.path.exists(db_file):
        os.remove(db_file)

    # Call the function with an empty URL list
    try:
        save_tabs_to_sqlite([])
        success = True
    except Exception as e:
        success = False

    # Check if the function handled the empty list without errors
    assert success

    # Clean up
    if os.path.exists(db_file):
        os.remove(db_file)