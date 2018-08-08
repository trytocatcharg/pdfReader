from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
import datetime

now =  datetime.datetime.now()
# yyy--mm--dd
nowStr=(str(now)).split(' ')[0] 
url="https://www.degussa-mp.es/precios"

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

table_element = soup.select("table > tbody > tr")

print(nowStr)

# valor del precio del oro de 1g
print (table_element[0].select("td")[2].text) 
print (table_element[0].select("td")[4].text) 

# valor del precio del oro de 2.5g
print (table_element[1].select("td")[2].text) 
print (table_element[1].select("td")[4].text) 