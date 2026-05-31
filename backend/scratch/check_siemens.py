import sys
sys.path.append(r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer")
from backend.agent import get_complete_financial_profile
import json

try:
    p = get_complete_financial_profile("SIEMENS.NS")
    fundamentals = p.get("fundamentals", {})
    score_metrics = p.get("score_metrics", {})
    dcf_model = p.get("dcf_model", {})
    
    print("Siemens Financial Profile Metrics:")
    print(f"Company Name: {p.get('company_name')}")
    print(f"P/E Ratio: {fundamentals.get('pe_ratio')}")
    print(f"ROE %: {fundamentals.get('roe_pct')}")
    print(f"ROCE %: {fundamentals.get('roce_pct')}")
    print(f"Debt to Equity: {fundamentals.get('debt_to_equity')}")
    print(f"CFO to PAT: {fundamentals.get('cfo_to_pat')}")
    print(f"3Y EPS Growth %: {fundamentals.get('eps_growth_3y_pct')}")
    print(f"3Y Sales Growth %: {fundamentals.get('sales_growth_3y_pct')}")
    print(f"3Y Profit Growth %: {fundamentals.get('profit_growth_3y_pct')}")
    print(f"PEG Ratio: {score_metrics.get('peg_ratio')}")
    print(f"DCF Margin of Safety %: {dcf_model.get('margin_of_safety')}")
    print(f"DCF Intrinsic Value: {dcf_model.get('intrinsic_value')}")
    print(f"Current Price: {fundamentals.get('current_price')}")
    
except Exception as e:
    print(f"Error: {e}")
