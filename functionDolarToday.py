
from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
import time
from colorama import init, Fore

init()



url = "http://www.dolarhoy.com/"
while 1==1:
    with urlopen(url) as html_txt:
        soup = BeautifulSoup(html_txt, 'lxml')

    table_element = soup.select(".body-content")
    dolar_sell = table_element[0].select("div > div")[0].select("div")[1].select("div")[1].select("h4")[0].text

    print(Fore.GREEN + dolar_sell + Fore.RESET)
    print("Variación " + table_element[0].select(".update")[0].text)
    print(table_element[0].select(".update")[1].text)
    time.sleep(60)