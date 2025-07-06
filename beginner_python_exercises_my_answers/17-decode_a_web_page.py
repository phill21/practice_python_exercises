"""
Note: this is a 4-chili exercise, not because it introduces a concept
(although it introduces a new library), but because this exercise is more like a project.
Feel free to skip this and come back when you’re more ready!

Use the BeautifulSoup and requests Python packages to print out a list of all the article
titles on the New York Times homepage.
"""
import requests
from bs4 import BeautifulSoup

url = 'http://www.globo.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
page = response.text
# print(page)

soup = BeautifulSoup(page, 'html.parser')
# print(soup.find_all('h2')[3].string)
titlesite = soup.find_all('h2')
print(type(len(titlesite)))
for title in range(len(titlesite)):
    noticia = titlesite[title].string
    print(noticia)

# soup = BeautifulSoup(html, 'html.parser')
# titulos = soup.find_all('story-wrapper')
# for titulos in titulos:
#     print(titulos.get_text())


