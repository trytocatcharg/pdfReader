
from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
import time
from colorama import init, Fore

init()


url = "https://www.lanacion.com.ar/economia/divisas"
# url = "http://www.dolarhoy.com/"
while 1==1:
    with urlopen(url) as html_txt:
        soup = BeautifulSoup(html_txt, 'lxml')

        table_element = soup.select(".caja")
        dolar_retail_label = table_element[0].select("div")[1].select("label")[0].text
        dolar_retail = table_element[0].select("div")[1].select("label")[1].text
        dolar_retail_var = table_element[0].select("div")[1].select("label")[3].text
        dolar_retail_time = table_element[0].select("div")[1].select("label")[4].text

        print(dolar_retail_label)
        print(Fore.GREEN + dolar_retail + Fore.RESET)
        print(dolar_retail_var)
        print(dolar_retail_time)

        table_element = soup.select(".caja")
        dolar_nat_label = table_element[0].select("div")[17].select("label")[0].text
        dolar_nat = table_element[0].select("div")[17].select("label")[1].text
        dolar_nat_var = table_element[0].select("div")[17].select("label")[3].text
        dolar_nat_time = table_element[0].select("div")[17].select("label")[4].text

        print(dolar_nat_label)
        print(Fore.GREEN + dolar_nat + Fore.RESET)
        print(dolar_nat_var)
        print(dolar_nat_time)
        time.sleep(60)
    # table_element = soup.select(".body-content")
    # dolar_sell = table_element[0].select("div > div")[0].select("div")[1].select("div")[1].select("h4")[0].text

    # print(Fore.GREEN + dolar_sell + Fore.RESET)
    # print("Variación " + table_element[0].select(".update")[0].text)
    # print(table_element[0].select(".update")[1].text)
    # time.sleep(60)
