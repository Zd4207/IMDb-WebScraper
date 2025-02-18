from bs4 import BeautifulSoup
import requests

# IMDb URL
url = 'https://www.imdb.com/title/tt15435876/?ref_=ttrel_ov'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# Request the page with a timeout
try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()  # Raises HTTPError 
    soup = BeautifulSoup(response.text, "html.parser")
    

    def get_title(soup):
        try:
            title = soup.find('h1').get_text(strip=True)
            return title
        except AttributeError:
            return "Could not find the title"
    
    # extract plot summary
    def get_plot(soup):
        try:
            plot = soup.find(class_='sc-3ac15c8d-0 hRUoSB').get_text(strip=True)
            return plot
        except AttributeError:
            return "Could not find movie's plot"
    
    # extract creators name
    def get_creator(soup):
        try:
            Creator_ = soup.find(class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').get_text(strip=True)
            return Creator_
        except AttributeError:
            return "Could not find the release date"
        
    # extract release date
    def get_release_date(soup):
        try:
            release_date = soup.find('a', {'title': 'See more release dates'}).get_text(strip=True)
            return release_date 
        except AttributeError:
            return "Could not find the release date"
    
    # Print results
    print("Movie Title:", get_title(soup))
    print("Plot:", get_plot(soup))
    print("Creator:", get_creator(soup))
    print("Released:s", get_release_date(soup))



except requests.exceptions.RequestException as e:
    print(f"Error: Unable to access the page. {e}")
