from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
from colorama import init, Fore

init()

# # venezuela
# contry_id='20' 
# # basil
# contry_id='3' 

# argentina
contry_id='2' 
url = 'http://www.ambito.com/economia/mercados/riesgo-pais/info/?id={0}'.format(contry_id)

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

element = soup.select("table > tr")
risk_today = int(element[0].select("tr")[1].select("td")[1].text.replace(".",""))
risk_yesterday = int(element[0].select("tr")[2].select("td")[1].text.replace(".",""))

date_today = element[0].select("tr")[1].select("td")[0].text
date_yesterday = element[0].select("tr")[2].select("td")[0].text


if risk_today < risk_yesterday:
    str_value = "{0}{1}{2} y el de ayer {3}".format(Fore.GREEN,risk_today,Fore.RESET,risk_yesterday)
else:
    str_value = "{0}{1}{2} y el de ayer {3}".format(Fore.RED,risk_today,Fore.RESET,risk_yesterday)

country = soup.select("#pais")
print(country[0].text)

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