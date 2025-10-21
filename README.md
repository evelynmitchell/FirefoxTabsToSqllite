# Firefox Tabs to SQLite

A Python utility to extract open Firefox tabs from the browser's session store and save them to a SQLite database with timestamps and unique identifiers.

## Features

- Extracts URLs from Firefox's sessionstore.jsonlz4 file
- Handles LZ4 compression automatically
- Stores tabs with unique IDs and ISO timestamps
- Supports multiple windows and tabs
- Comprehensive test coverage (16 test files)

## Installation

### Requirements

- Python 3.10+
- Firefox browser

### Dependencies

```bash
pip install lz4
```

Or using the project's build system:

```bash
pip install -e .
```

## Usage

### Basic Usage

Run the script to extract all currently open Firefox tabs:

```bash
python fftabs.py
```

This will:
1. Locate your Firefox profile directory
2. Read and decompress the sessionstore.jsonlz4 file
3. Extract all URLs from open tabs
4. Save them to `firefox_tabs.db` with unique IDs and timestamps

### Database Schema

The SQLite database contains a single table `tabs` with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| uniqueid | TEXT (PRIMARY KEY) | UUID v4 for each tab entry |
| date | TEXT | ISO 8601 timestamp when the tab was saved |
| url | TEXT | The URL of the tab |

### Example

```python
from fftabs import get_firefox_tabs, save_tabs_to_sqlite

# Get all open tabs
urls = get_firefox_tabs()
print(f"Found {len(urls)} tabs")

# Save to database
save_tabs_to_sqlite(urls)
```

## How It Works

1. **Profile Discovery**: Reads `~/.mozilla/firefox/profiles.ini` to find the active Firefox profile
2. **Session Store Access**: Locates the `sessionstore.jsonlz4` file in the profile directory
3. **LZ4 Decompression**: Decompresses the Mozilla LZ4 format (magic bytes: `mozLz40\0`)
4. **JSON Parsing**: Extracts URLs from the JSON structure (windows → tabs → entries)
5. **SQLite Storage**: Creates/updates database with unique IDs and timestamps

## Testing

The project includes comprehensive test coverage with 16 test files:

```bash
pytest tests/
```

Test coverage includes:
- URL extraction and handling
- LZ4 decompression
- Firefox profile path detection
- Database operations (create, insert, commit)
- Edge cases (empty URLs, Unicode, multiple rows)
- Transaction handling

## Platform Support

Currently supports Linux/Unix systems with standard Firefox installations at:
- `~/.mozilla/firefox/`

For other platforms:
- **Windows**: Modify `firefox_path` to `%APPDATA%\Mozilla\Firefox`
- **macOS**: Modify `firefox_path` to `~/Library/Application Support/Firefox`

## Project Structure

```
FirefoxTabsToSqllite/
├── fftabs.py              # Main module
├── pyproject.toml         # Project configuration
├── tests/                 # Test suite (16 files)
│   ├── test_firefox_tabs.py
│   ├── test_extract_urls.py
│   ├── test_decompress_session_store.py
│   └── ... (13 more test files)
└── README.md
```

## Development

### Building

This project uses Hatchling as the build backend:

```bash
pip install build
python -m build
```

### Running Tests

```bash
pytest tests/ -v
```

### Dependencies

- **Runtime**: `lz4` for decompression
- **Standard Library**: `os`, `json`, `sqlite3`, `uuid`, `datetime`
- **Development**: `pytest` for testing

## Use Cases

- **Tab Management**: Archive open tabs before closing Firefox
- **Research**: Track browsing history with timestamps
- **Backup**: Save important tab collections
- **Analytics**: Analyze browsing patterns over time
- **Migration**: Transfer tabs between devices or profiles

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Areas for improvement:

- Cross-platform path detection
- Support for other browsers (Chrome, Edge, Safari)
- GUI interface
- Export to other formats (CSV, JSON)
- Deduplication of URLs
- Tag/category support

## Credits

Generated with comprehensive test coverage by CodiumAI.

## Related Projects

- [Mozilla Session Store Format](https://wiki.mozilla.org/Session_Restore)
- [LZ4 Compression](https://github.com/lz4/lz4)
