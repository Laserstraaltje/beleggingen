"""Haalt dagkoersen op via Yahoo Finance en schrijft prices.json."""
import json, sys
import yfinance as yf

with open("trades.json") as f:
    cfg = json.load(f)

start = min(t["date"] for t in cfg["trades"])
prices = {}
for name, ticker in cfg["tickers"].items():
    try:
        hist = yf.Ticker(ticker).history(start=start, auto_adjust=False)["Close"]
        if hist.empty:
            raise ValueError("geen data")
        prices[ticker] = {d.strftime("%Y-%m-%d"): round(float(p), 4) for d, p in hist.items()}
        print(f"OK   {name} ({ticker}): {len(hist)} dagen")
    except Exception as e:
        print(f"SKIP {name} ({ticker}): {e}", file=sys.stderr)

with open("prices.json", "w") as f:
    json.dump(prices, f)
