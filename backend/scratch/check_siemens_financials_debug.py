import yfinance as yf
import pandas as pd
import json

stock = yf.Ticker("SIEMENS.NS")
financials = stock.financials

print("yfinance financials index:")
print(list(financials.index))

print("\nTotal Revenue series:")
if "Total Revenue" in financials.index:
    print(financials.loc["Total Revenue"])
    
print("\nNet Income series:")
if "Net Income" in financials.index:
    print(financials.loc["Net Income"])
    
if "Net Income Common Stockholders" in financials.index:
    print("\nNet Income Common Stockholders series:")
    print(financials.loc["Net Income Common Stockholders"])
    
# Re-run CAGR logic
rev_series = financials.loc["Total Revenue"].dropna().sort_index(ascending=True)
print("\nSorted Revenue:")
print(rev_series)
print(f"iloc[-4]: {rev_series.iloc[-4] if len(rev_series) >= 4 else 'N/A'}")
print(f"iloc[-1]: {rev_series.iloc[-1] if len(rev_series) >= 4 else 'N/A'}")

prof_series = financials.loc["Net Income"].dropna().sort_index(ascending=True)
print("\nSorted Profit:")
print(prof_series)
p_start = prof_series.iloc[-4]
p_end = prof_series.iloc[-1]
print(f"p_start (iloc[-4]): {p_start}")
print(f"p_end (iloc[-1]): {p_end}")
print(f"Calculated 3y profit CAGR: {((p_end / p_start) ** (1/3) - 1) * 100.0}")
