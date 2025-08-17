import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://councillors.liverpool.gov.uk/documents"

def fetch_new_reports():
    page = requests.get(f"{BASE_URL}?T=1")
    soup = BeautifulSoup(page.text, "html.parser")
    reports = []

    for link in soup.select("a[href$='.pdf']")[:5]:  # get latest 5
        url = link['href']
        title = link.text.strip()
        reports.append({
            'title': title,
            'url': url,
            'content': f"Download PDF at {url}",  # placeholder; real PDF parsing could be added
            'date': datetime.today().strftime("%Y-%m-%d")
        })
    return reports
