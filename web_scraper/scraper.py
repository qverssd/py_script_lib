import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h1')
        
        for idx, title in enumerate(titles, start=1):
            print(f"Title {idx}: {title.get_text()}")
        else:
            print(f"Failed to retrive page. Status code: {response.status_code}")

if __name__ == "__main__":
    url = 'https://example.com'
    scrape_website(url)