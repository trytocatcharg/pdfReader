from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup


url="https://www.bde.es/bde/es/"


#Opening bde site using urllib
html_page = html_page = urlopen(url)
html_bytes_array=html_page.read()
html_parse = html.fromstring(html_bytes_array)

# for link in html_parse.xpath("//a"):
#     print ("Name", link.text, "URL", link.get("href"))

# https://medium.com/@epicshane/using-beautifulsoup4-to-find-class-exact-match-3e263a95e330
# #Feeding the content
# soup = bs4(html_parse, 'html.parser')
# print(soup.prettify())

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')
tag = soup.find(lambda tag: tag.name == 'dd' and tag['class'] == ['euroDolar'])


# test="<div class='price'> first </div><div class='value'> second </div><div class='value price '>third </div>"
# soup = BeautifulSoup(test, 'lxml')
# tag = soup.find(lambda tag: tag.name == 'div' and tag['class'] == ['price'])


print(tag)
# html2 = bs4.BeautifulSoup(html_parse, 'html.parser'))

# tag = html2.find(lambda tag: tag.name == 'div' and tag['class'] == ['euroDolar'])

# print(tag)
