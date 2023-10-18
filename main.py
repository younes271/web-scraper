import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get('https://www.your-website.com')

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(r.text, 'html.parser')

# Find all the desired tags
data = soup.find_all('tag-name')

# Loop through the data and extract necessary information
for item in data:
    print(item.text)
