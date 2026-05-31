import sys
sys.path.append(r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer")
from backend.financial_utils import calculate_dcf_valuation
import yfinance as yf
import json

stock = yf.Ticker("SIEMENS.NS")
res = calculate_dcf_valuation("SIEMENS.NS", stock_obj=stock)

print("DCF direct result:")
print(json.dumps(res, indent=2))
