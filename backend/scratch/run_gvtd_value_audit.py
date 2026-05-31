import sys
sys.path.append(r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer")

from backend.agent import run_single_stock_audit
import json

res = run_single_stock_audit("GVT&D.NS", horizon="Long-term (3+ years)", risk_profile="Moderate")
if "error" in res:
    print(res["error"])
else:
    for combo in res["combinations"]:
        if combo["strategy"] == "bottom_up" and combo["style"] == "value":
            print("Bottom-Up Value style combination:")
            print(json.dumps(combo, indent=2))
