import requests

from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape

url = 'https://www.audible.com/search?keywords=book&node=18573211011'

# Send an HTTP GET request to the URL

response = requests.get(url)

# Check if the request was successful

if response.status_code == 200:

    # Parse the HTML content of the page

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data - this example assumes we're extracting all paragraph text

    paragraphs = soup.find_all('p')

    # Print the text of each paragraph

    for para in paragraphs:
        print(para.get_text())

else:

    print(f'Failed to retrieve data: {response.status_code}')

import requests

from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape

url = 'https://example.com'

# Send an HTTP GET request to the URL

response = requests.get(url)

# Check if the request was successful

if response.status_code == 200:

    # Parse the HTML content of the page

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data - this example assumes we're extracting all article titles and links

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

    response.raise_for_status()  # Check for HTTP errors

    soup = BeautifulSoup(response.text, 'html.parser')

    # Your scraping logic here

except requests.RequestException as e:

    print(f'Error during requests to {url}: {e}')

except Exception as e:

    print(f'An error occurred: {e}')
