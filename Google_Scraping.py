import requests
from bs4 import BeautifulSoup

search_input = input('aramak istediğiniz kelime: ').replace(' ','+')
link = "https://www.google.com/search?q=" + search_input

headerParams = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/}'}

response = requests.get(link, headers = headerParams)

soup = BeautifulSoup(response.content,"html.parser")

results = soup.find_all('div', class_="rc")

for div in results:
    anchor = div.find('a')

    link = anchor['href']
    text = anchor.find('h3').string
    description = anchor.parent.next_sibling.find('span').text

    print(link + "*** " + text + "*** " + description)
    print('*******************')
