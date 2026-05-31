import requests
from bs4 import BeautifulSoup
import re

url = "https://www.screener.in/company/SIEMENS/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers, timeout=8)
print(f"Status Code: {res.status_code}")
if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    
    print("\nScreener.in Page Title:")
    print(soup.title.text.strip())
    
    # Check if there is a Consolidated / Standalone warning or toggle
    toggle_div = soup.find("div", class_="show-consolidated") or soup.find("div", class_="flex-space-between")
    if toggle_div:
        print("\nFound Toggle/Flex container:")
        print(toggle_div.text.strip())
        
    print("\nRatio Cards:")
    ratio_list = soup.select("ul#top-ratios li")
    for li in ratio_list:
        name_el = li.find("span", class_="name")
        value_el = li.find("span", class_="number")
        if name_el and value_el:
            print(f"{name_el.text.strip()}: {value_el.text.strip()}")
            
    # Check for "Consolidated" or "Standalone" text anywhere in page
    text_matches = soup.find_all(string=re.compile(r'(consolidated|standalone)', re.IGNORECASE))
    print(f"\nOccurrences of 'consolidated' or 'standalone': {len(text_matches)}")
    for match in text_matches[:10]:
        print(f"- {match.strip()[:100]}")
