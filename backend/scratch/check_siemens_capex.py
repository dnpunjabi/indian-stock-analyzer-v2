import yfinance as yf

stock = yf.Ticker("SIEMENS.NS")
cf = stock.cashflow

if not cf.empty:
    print("Cashflow Statement PPE and Capex keys:")
    for key in ["Operating Cash Flow", "Capital Expenditure", "Purchase Of PPE", "Sale Of PPE"]:
        if key in cf.index:
            print(f"\n{key}:")
            print(cf.loc[key])
