import sys
sys.path.append(r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer")
from backend.financial_utils import get_complete_financial_profile

ticker = "GVT&D.NS"
try:
    print(f"==================== Revalidating {ticker} ====================")
    profile = get_complete_financial_profile(ticker, bypass_db_cache=True)
    
    fundamentals = profile.get("fundamentals", {})
    pe_bands = profile.get("pe_bands", {})
    
    current_pe = fundamentals.get("pe_ratio")
    median_pe = pe_bands.get("median_pe")
    max_pe = pe_bands.get("max_pe")
    min_pe = pe_bands.get("min_pe")
    
    # Calculate premium/discount to 5Y median
    pe_diff = 0.0
    if current_pe and median_pe:
        pe_diff = ((current_pe - median_pe) / median_pe) * 100.0
        
    print(f"Current Trailing P/E:   {current_pe:.2f}" if current_pe else "Current Trailing P/E:   N/A")
    print(f"5Y Historical Median:   {median_pe:.2f}" if median_pe else "5Y Historical Median:   N/A")
    print(f"5Y Max P/E Peak:        {max_pe:.2f}" if max_pe else "5Y Max P/E Peak:        N/A")
    print(f"5Y Min P/E Floor:       {min_pe:.2f}" if min_pe else "5Y Min P/E Floor:       N/A")
    print(f"Premium/Discount:       {pe_diff:+.1f}% {'Premium' if pe_diff > 0 else 'Discount'}")
    
except Exception as e:
    print(f"Error checking {ticker}: {e}")
