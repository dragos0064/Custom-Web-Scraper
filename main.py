import requests

from bs4 import BeautifulSoup


url = 'https://www.audible.com/search?keywords=book&node=18573211011'


response = requests.get(url)


if response.status_code == 200:


    soup = BeautifulSoup(response.text, 'html.parser')


    paragraphs = soup.find_all('p')


    for para in paragraphs:
        print(para.get_text())

else:

    print(f'Failed to retrieve data: {response.status_code}')

import requests

from bs4 import BeautifulSoup

url = 'https://example.com'


response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        title = article.find('h2').get_text()

        link = article.find('a')['href']

        print(f'Title: {title}')

        print(f'Link: {link}')

else:

    print(f'Failed to retrieve data: {response.status_code}')

try:

    response = requests.get(url)

    response.raise_for_status()  

    soup = BeautifulSoup(response.text, 'html.parser')

   
except requests.RequestException as e:

    print(f'Error during requests to {url}: {e}')

except Exception as e:

    print(f'An error occurred: {e}')
