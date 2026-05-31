import sys
sys.path.append(r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer")
from backend.financial_utils import fetch_screener_data

print("Fetching GVT&D:")
s1 = fetch_screener_data("GVT&D")
print("GVT&D Ratios scraped successfully?", s1.get("scraped_successfully"))
print("GVT&D Ratios:", s1.get("ratios"))

print("\nFetching GVTD:")
s2 = fetch_screener_data("GVTD")
print("GVTD Ratios scraped successfully?", s2.get("scraped_successfully"))
print("GVTD Ratios:", s2.get("ratios"))
