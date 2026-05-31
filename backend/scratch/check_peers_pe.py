import sys
sys.path.append(r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer")
from backend.agent import get_complete_financial_profile
import json

p = get_complete_financial_profile("GVT&D.NS")
peers = p.get("peers", [])
print(f"Number of peers found: {len(peers)}")
for peer in peers[:5]:
    print(json.dumps(peer, indent=2))
