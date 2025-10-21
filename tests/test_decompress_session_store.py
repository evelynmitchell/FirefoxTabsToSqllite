def test_decompress_session_store(self):
    """Decompress sessionstore.jsonlz4 file using lz4.block"""
    import lz4.block
    # Call the function get_firefox_tabs to decompress session store file
    result = get_firefox_tabs()
    assert result is not None