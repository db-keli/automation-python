from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)


source = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')


print(soup.prettify())
