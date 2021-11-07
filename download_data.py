import os
import requests
from bs4 import BeautifulSoup

def load_page(url):
    print(f'Loading {url}...')
    headers = {'Accept-Language': 'de-at;it-it;en-us'}
    response = requests.get(url, headers=headers)
    return response.text

def save_html_to_file(text, filename, dir_path='data'):
    # Need to take into accound cwd
    if not os.path.exists(dir_path):
        print(f'Creating directory {dir_path}')
        os.makedirs(dir_path)

    print('Saving...')
    with open(f'{dir_path}/{filename}', 'w', encoding="utf8") as File:
        soup = BeautifulSoup(text, 'html.parser')
        File.write(soup.prettify())    

if __name__ == "__main__":
    for i in range(1, 400):
        url = f"https://www.bolha.com/racunalnistvo?typeOfTransaction=Prodam&sort=expensive&page={i}"
        filename = f"bolha-oglasi-racunalnistvo-{i}.html"

        save_html_to_file(load_page(url), filename)
