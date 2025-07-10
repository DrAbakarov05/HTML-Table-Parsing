import pytest
from html_table_parser import parse_html_tables, parse_html_table

SAMPLE_HTML = """
<table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td>2</td></tr></table>
<table><tr><td>x</td><td>y</td></tr></table>
"""


def test_parse_html_tables():
    dfs = parse_html_tables(SAMPLE_HTML)
    assert len(dfs) == 2
    assert dfs[0].iloc[0, 0] == 1


def test_parse_html_table_index():
    rows = parse_html_table(SAMPLE_HTML, index=1)
    assert rows == [["x", "y"]]
