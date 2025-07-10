"""Utilities for parsing HTML tables."""

import pandas as pd
from bs4 import BeautifulSoup


def parse_html_tables(source: str):
    """Parse all HTML tables from the given source.

    Parameters
    ----------
    source : str
        HTML text, path to a local file or URL.

    Returns
    -------
    list[pd.DataFrame]
        A list of DataFrames for each table found.
    """
    try:
        tables = pd.read_html(source)
        return tables
    except ValueError:
        # No tables found
        return []


def parse_html_table(html: str, index: int = 0):
    """Parse a single HTML table using BeautifulSoup.

    Parameters
    ----------
    html : str
        HTML markup containing at least one table.

    Returns
    -------
    list[list[str]]
        Parsed table as a list of rows with cell values.
    """
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    if not tables or index >= len(tables):
        return []
    table = tables[index]

    rows: list[list[str]] = []
    for tr in table.find_all('tr'):
        cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
        if cells:
            rows.append(cells)
    return rows

