import yfinance as yf
import requests

url = "https://query2.finance.yahoo.com/v1/finance/search?q=GE%20Vernova%20T%26D&quotesCount=10"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers).json()
print("Search results:")
for q in res.get("quotes", []):
    print(q)
