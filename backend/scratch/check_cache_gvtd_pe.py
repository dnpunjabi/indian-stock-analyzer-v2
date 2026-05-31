import sys
sys.path.append(r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer")
from backend.agent import get_complete_financial_profile
import json

try:
    p = get_complete_financial_profile("GVT&D.NS")
    fundamentals = p.get("fundamentals", {})
    pe_bands = p.get("pe_bands", {})
    
    print("GVT&D.NS Valuation Stats:")
    print(f"Current P/E: {fundamentals.get('pe_ratio')}")
    print(f"Sector Median P/E: {fundamentals.get('sector_pe')}")
    print(f"5Y Median P/E: {pe_bands.get('median_pe')}")
    print(f"5Y Min P/E: {pe_bands.get('min_pe')}")
    print(f"5Y Max P/E: {pe_bands.get('max_pe')}")
    
except Exception as e:
    print(f"Error: {e}")
