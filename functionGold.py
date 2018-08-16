from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
import datetime
from mongoDB import *



now =  datetime.datetime.now()
# yyy--mm--dd HH:MM
nowStr = (str(now)).split(' ')[0 ]+ ' {0}'.format(now.strftime("%H:%M"))
url = "https://www.degussa-mp.es/precios"

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

table_element = soup.select("table > tbody > tr")

print(nowStr)

# # valor del precio del oro de 1g
# print (table_element[0].select("td")[2].text) 
# print (table_element[0].select("td")[4].text) 

# # valor del precio del oro de 2.5g
# print (table_element[1].select("td")[2].text) 
# print (table_element[1].select("td")[4].text) 

# convierto el precio a  numerico
value_gold = float(table_element[0].select("td")[4].text.replace("€","").replace(",","."))
# genero una variable para el nombre del producto
name_gold = table_element[0].select("td")[2].text
# guardo la info en Mongo
db_store = {'name':name_gold, 'value':value_gold, 'time':nowStr,'type_id':'1G'}

# Inserto barra de 1 gr
save_data(db_store)
# Inserto barra de 1 gr
##################################

##################################
# convierto el precio a  numerico
value_gold = float(table_element[1].select("td")[4].text.replace("€","").replace(",","."))
# genero una variable para el nombre del producto
name_gold = table_element[1].select("td")[2].text
# guardo la info en Mongo
db_store = {'name':name_gold, 'value':value_gold, 'time':nowStr, 'type_id':'2.5G'}

# Inserto barra de 2.5 gr
save_data(db_store)
# Inserto barra de 2.5 gr