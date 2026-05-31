import yfinance as yf

stock = yf.Ticker("SIEMENS.NS")
info = stock.info

print(f"sharesOutstanding: {info.get('sharesOutstanding')}")
print(f"marketCap: {info.get('marketCap')}")
print(f"totalDebt: {info.get('totalDebt')}")
print(f"cash: {info.get('cash') or info.get('totalCash')}")
