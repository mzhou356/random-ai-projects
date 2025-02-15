import json
from typing import Dict

import yfinance as yf
from langchain_core.tools import tool


@tool
def get_stock_info(ticker: str) -> Dict[str, str]:
    """Get basic stock ticker information such as price, quotes, and more.

    Args:
        ticker (str): the ticker of a stock
    """
    data = yf.Ticker(ticker).fast_info
    if data.fast_info.shares:
        return json.loads(data.toJSON())
    return {}
