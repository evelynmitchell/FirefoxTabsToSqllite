def test_parse_json_content(self):
    """# Parse JSON content from decompressed session store file
    # Call the function get_firefox_tabs to parse JSON content"""
    result = get_firefox_tabs()
    assert isinstance(result, list)