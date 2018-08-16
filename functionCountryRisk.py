from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style

init()

arg='2'
url = 'http://www.ambito.com/economia/mercados/riesgo-pais/info/?id={0}'.format(arg)

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

element = soup.select("table > tr")
risk_today = int(element[0].select("tr")[1].select("td")[1].text)
risk_yesterday = int(element[0].select("tr")[2].select("td")[1].text)

date_today = element[0].select("tr")[1].select("td")[0].text
date_yesterday = element[0].select("tr")[2].select("td")[0].text


if risk_today < risk_yesterday:
    str_value = "{0}{1}{2} y el de ayer {3}".format(Fore.GREEN,risk_today,Fore.RESET,risk_yesterday)
else:
    str_value = "{0}{1}{2} y el de ayer {3}".format(Fore.RED,risk_today,Fore.RESET,risk_yesterday)


if int(risk_today) > 1000:
    print("Esto tiene olor a 2001...{0}".format(str_value))
elif int(risk_today) > 900:
    print("Se viene el estallido...{0}".format(str_value))
elif int(risk_today) > 800:
    print("Macri gato...{0}".format(str_value))
elif int(risk_today) > 700:
    print("A la pelota...{0}".format(str_value))
else:
    print("vamos bien estamos en {0}".format(str_value))


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'