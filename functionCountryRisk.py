from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup

arg='2'
url = 'http://www.ambito.com/economia/mercados/riesgo-pais/info/?id={0}'.format(arg)

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

element = soup.select("#ultimo > big")
risk = element[0].text

if int(risk) < 700:
    print("vamos bien estamos en {0}".format(risk))
else:
    print("A la pelota...{0}".format(risk))


