import yfinance as yf
import json

stock = yf.Ticker("SIEMENS.NS")
info = stock.info

print("yfinance info keys related to valuation/income:")
print(f"trailingPE: {info.get('trailingPE')}")
print(f"trailingEps: {info.get('trailingEps')}")
print(f"returnOnEquity: {info.get('returnOnEquity')}")
print(f"returnOnAssets: {info.get('returnOnAssets')}")

financials = stock.financials
print("\nFinancials index diluted EPS:")
if not financials.empty and "Diluted EPS" in financials.index:
    print(financials.loc["Diluted EPS"])

balance_sheet = stock.balance_sheet
print("\nBalance sheet total equity index:")
if not balance_sheet.empty:
    for idx in balance_sheet.index:
        if "Equity" in idx or "Stockholders" in idx:
            print(f"{idx}:")
            print(balance_sheet.loc[idx])
