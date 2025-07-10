# HTML Table Parsing

This repository contains simple utilities for parsing HTML tables in Python.

## Usage

```python
from html_table_parser import parse_tables_pandas, parse_table_bs4

# From a URL or file
tables = parse_tables_pandas('https://example.com/page.html')

# From raw HTML text
with open('table.html', 'r', encoding='utf-8') as f:
    html = f.read()
rows = parse_table_bs4(html)
```

`parse_tables_pandas` returns a list of `pandas.DataFrame` objects for each table found,
while `parse_table_bs4` extracts a single table into a list of rows.
