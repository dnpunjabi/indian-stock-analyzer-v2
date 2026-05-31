import sys
sys.path.append(r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer")
import sqlite3
import os
from backend.financial_utils import get_complete_financial_profile

# Database Path
DATABASE_DIR = r"c:\Users\dheer\Desktop\AI\indian-stock-analyzer\backend\data"
DATABASE_PATH = os.path.join(DATABASE_DIR, "watchlist_database.db")

print("Deleting GVT&D.NS from database cache...")
if os.path.exists(DATABASE_PATH):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cached_profiles WHERE symbol = 'GVT&D.NS'")
    conn.commit()
    conn.close()
    print("Deleted successfully.")
else:
    print("Database path not found.")

print("\nRebuilding profile with bypass_db_cache=True...")
profile = get_complete_financial_profile("GVT&D.NS", bypass_db_cache=True)
fundamentals = profile.get("fundamentals", {})

print(f"\nSelf-Healed GVT&D.NS P/E Ratio: {fundamentals.get('pe_ratio')}")
