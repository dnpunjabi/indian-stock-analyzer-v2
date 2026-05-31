import yfinance as yf
import json

ticker = yf.Ticker("GVT&D.NS")
info = ticker.info

print("GVT&D.NS trailingPE:", info.get("trailingPE"))
print("GVT&D.NS forwardPE:", info.get("forwardPE"))
print("GVT&D.NS currentPrice:", info.get("currentPrice"))
print("GVT&D.NS trailingEps:", info.get("trailingEps"))
print("GVT&D.NS regularMarketPrice:", info.get("regularMarketPrice"))
print("GVT&D.NS shortName:", info.get("shortName"))
