"""Haalt dagkoersen op via Yahoo Finance en schrijft prices.json."""
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "trades.json").open(encoding="utf-8") as f:
    cfg = json.load(f)

start = min(t["date"] for t in cfg["trades"])
prices = {}
dividends = {}
for name, ticker in cfg["tickers"].items():
    try:
        hist = yf.Ticker(ticker).history(start=start, auto_adjust=False, actions=True)
        if hist.empty:
            raise ValueError("geen data")

        valid_prices = {}
        for day, value in hist["Close"].items():
            if value is None or (isinstance(value, float) and not math.isfinite(value)):
                continue
            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                continue
            if not math.isfinite(numeric_value):
                continue
            valid_prices[day.strftime("%Y-%m-%d")] = round(numeric_value, 4)

        if not valid_prices:
            raise ValueError("geen geldige koersen")

        prices[ticker] = valid_prices
        valid_dividends = {}
        for day, value in hist["Dividends"].items():
            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                continue
            if math.isfinite(numeric_value) and numeric_value > 0:
                valid_dividends[day.strftime("%Y-%m-%d")] = round(numeric_value, 4)
        dividends[ticker] = valid_dividends
        print(
            f"OK   {name} ({ticker}): {len(valid_prices)} koersen, "
            f"{len(valid_dividends)} dividenddatums"
        )
    except Exception as e:
        print(f"SKIP {name} ({ticker}): {e}", file=sys.stderr)

with (ROOT / "prices.json").open("w", encoding="utf-8") as f:
    prices["_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    json.dump(prices, f, ensure_ascii=False, allow_nan=False)
with (ROOT / "dividends.json").open("w", encoding="utf-8") as f:
    json.dump(dividends, f, ensure_ascii=False, allow_nan=False)
