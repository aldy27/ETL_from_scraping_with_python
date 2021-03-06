import pandas as pd
import logging

from typing import List

logging.basicConfig(level=logging.INFO)


def scrape(url):
    logging.info(f"Scraping website with url: '{url}' ...")
    return pd.read_html(url, header=None)
