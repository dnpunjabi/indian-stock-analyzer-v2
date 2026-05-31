import yfinance as yf

stock = yf.Ticker("SIEMENS.NS")
info = stock.info

print("yfinance info cashflow keys:")
print(f"operatingCashflow: {info.get('operatingCashflow')}")
print(f"netIncomeToCommon: {info.get('netIncomeToCommon')}")
print(f"netIncome: {info.get('netIncome')}")

cashflow = stock.cashflow
print("\nCashflow statement index:")
print(list(cashflow.index) if not cashflow.empty else "Empty cashflow statement")

if not cashflow.empty and "Operating Cash Flow" in cashflow.index:
    print("\nOperating Cash Flow series:")
    print(cashflow.loc["Operating Cash Flow"])
