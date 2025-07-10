# HTML Table Parsing

This repository contains simple utilities for parsing HTML tables in Python.

## Usage

```python
from html_table_parser import parse_html_tables, parse_html_table

# From a URL or file
tables = parse_html_tables('https://example.com/page.html')

# From raw HTML text
with open('table.html', 'r', encoding='utf-8') as f:
    html = f.read()
rows = parse_html_table(html)
```

`parse_html_tables` returns a list of `pandas.DataFrame` objects for each table found,
while `parse_html_table` extracts a single table into a list of rows. Pass
`index` to `parse_html_table` to parse a table other than the first one.
