
"""Utilities for parsing HTML tables.

This module was reworked during the last update to expose two main
functions with clearer names and to allow selecting a specific table
by index.  The comments below explain the purpose of each function and
highlight the lines that changed from the prior version of the code.
"""

# pandas is used for convenient DataFrame extraction from HTML. It requires
# the optional dependency ``lxml`` which should be installed separately.


# BeautifulSoup provides lightweight parsing when a DataFrame is not needed.
=======

import pandas as pd
from bs4 import BeautifulSoup


def parse_html_tables(source: str):
    """Parse all HTML tables from the given source.
    This function is essentially a thin wrapper over :func:`pandas.read_html`.
    It kept the same behavior as the earlier helper ``parse_table_pandas`` but
    was renamed to better reflect that multiple tables are returned.  ``source``
    can be a URL, a file path, or raw HTML text.

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

        # ``read_html`` handles fetching the content and returning a list of
        # DataFrames. This line remained unchanged but is now wrapped in a more
        # descriptive function name.
       
        # When no tables are present ``read_html`` raises ValueError. Returning
        # an empty list keeps the API consistent with previous versions.

        tables = pd.read_html(source)
        return tables
    except ValueError:
        # No tables found

        return []


def parse_html_table(html: str, index: int = 0):
    """Parse a single HTML table using BeautifulSoup.


    This helper replaces the older function that only returned the first
    table.  The new ``index`` argument lets callers choose which table to
    extract when multiple are present.


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

        # Returning an empty list mirrors the behavior of ``parse_html_tables``
        # when no data is found.
=======

        return []
    table = tables[index]

    rows: list[list[str]] = []
    for tr in table.find_all('tr'):

        # Collect the text from both ``td`` and ``th`` cells so that headers
        # and data rows are treated uniformly.
=======

        cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
        if cells:
            rows.append(cells)
    return rows

