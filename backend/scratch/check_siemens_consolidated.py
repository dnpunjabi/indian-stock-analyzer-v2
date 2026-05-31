import requests
from bs4 import BeautifulSoup

url = "https://www.screener.in/company/SIEMENS/consolidated/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers, timeout=8)
print(f"Consolidated Status Code: {res.status_code}")
if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    print("\nConsolidated Page Title:")
    print(soup.title.text.strip())
    
    print("\nConsolidated Ratio Cards:")
    ratio_list = soup.select("ul#top-ratios li")
    for li in ratio_list:
        name_el = li.find("span", class_="name")
        value_el = li.find("span", class_="number")
        if name_el and value_el:
            print(f"{name_el.text.strip()}: {value_el.text.strip()}")
            
    # Check if this page has Consolidated metrics
    toggle_div = soup.find("div", class_="show-consolidated") or soup.find("div", class_="flex-space-between")
    if toggle_div:
        print("\nFound Toggle container:")
        print(toggle_div.text.strip())
