from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
import datetime
import xlsxwriter


now =  datetime.datetime.now()
# yyy--mm--dd HH:MM
nowStr = (str(now)).split(' ')[0 ]+ '_{0}'.format(now.strftime("%H-%M"))
COMPANY = 'national-grid'
INGRESOS_ROW = 2
COSTES_DE_VENTA_ROW = 3
MARGEN_BRUTO_ROW = 4
MARGEN_BRUTO_PORCENTAJE_ROW = 5
EBITDA_ROW = 5
EBITDA_PORCENTAJE_ROW = 6
MARGEN_EBITDA_OVER_VENTAS_ROW = 7
EBIT_ROW = 8
EBIT_PORCENTAJE_ROW = 9
MARGEN_EBIT_OVER_VENTAS_ROW = 10
RESULTADO_NETO_ORDINARIO_ROW = 11
RESULTADO_NETO_TOTAL_ROW = 12
BPA_ROW = 13
BPA_PORCENTAJE_ROW = 14
DIVIDENDO_ORDINARIO_ROW = 15
DIVIDENDO_ORDINARIO_PORCENTAJE_ROW = 16
PAYOUT_ROW = 17
DIVIDENDO_TOTAL_ROW = 18
VALOR_CONTABLE_ACCION_ROW = 19
DEUDA_NETA_ROW = 20
DEUDA_NETA_PORCENTAJE_ROW = 21
DEUDA_NETA_OVER_CF_EXPLOTACION_ROW = 22
ROA_ROW = 23
ROE_ROW = 24
ROCE_ROW = 25
CF_EXPLOTACION_ROW = 26
CF_EXPLOTACION_PORCENTAJE_ROW = 27
CF_INVERSION_ROW = 28
CF_INVERSION_PORCENTAJE_ROW = 29
CF_FINANCIACION_ROW = 30
CF_FINANCIACION_PORCENTAJE_ROW = 31
VARIACION_TIPO_CAMBIO_ROW = 32
CF_NETO_ROW = 33
CF_NETO_PORCENTAJE_ROW = 34


url = "https://www.invertirenbolsa.info/historicodividendos/empresa/{0}".format(COMPANY)

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

# table_element = soup.select("div > section > div > section > div")
table_element = soup.findAll("div", {"class": "to-fixed"})

print(nowStr)

def is_not_blank(s):
    return bool(s and s.strip())

def convert_to_number(value):
    if isinstance(value, int):
        return value
    
    return float(value.replace('.', '').replace(',', '.'))


# # print (table_element[0].select("td")[2].text) 
workbook = xlsxwriter.Workbook("./excel/{0}_{1}.xlsx".format(COMPANY, nowStr)) 
worksheet = workbook.add_worksheet() 
columns = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE']

i = 1
# # Años
for f in reversed(table_element[0].select("th")):
    columName = columns[i] + str(1)
    worksheet.write(columName, f.text) 
    i += 1
# # Años

# # Ingresos
i = 0
filter_list = []
for f in table_element[0].select("tr")[1]:
    if is_not_blank(f.text):
        filter_list.append(f.text)
    else:
        filter_list.append(0)

del filter_list[0] # borro el texto
columName = columns[i] + str(INGRESOS_ROW)
worksheet.write(columName, 'Ingresos')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(INGRESOS_ROW)
    worksheet.write(columName,convert_to_number(f)) 
    i += 1
# # Ingresos

# Coste de ventas
i = 0
filter_list = []
for f in table_element[0].select("tr")[3]:
    if is_not_blank(f.text):
        filter_list.append(f.text)
    else:
        filter_list.append(0)

del filter_list[0] # borro el texto
columName = columns[i] + str(COSTES_DE_VENTA_ROW)
worksheet.write(columName, 'Costes de venta')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(COSTES_DE_VENTA_ROW)
    worksheet.write(columName, f) 
    i += 1
# Coste de ventas

# Margen bruto
i = 0
filter_list = []
for f in table_element[0].select("tr")[5]:
    if is_not_blank(f.text):
        filter_list.append(f.text)
    else:
        filter_list.append(0)

del filter_list[0] # borro el texto
columName = columns[i] + str(MARGEN_BRUTO_ROW)
worksheet.write(columName, 'Margen btuto')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(MARGEN_BRUTO_ROW)
    worksheet.write(columName, f) 
    i += 1
# Margen bruto

# Margen bruto %
i = 0
filter_list = []
for f in table_element[0].select("tr")[6]:
    if is_not_blank(f.text):
        filter_list.append(f.text)
    else:
        filter_list.append(0)

del filter_list[0] # borro el texto
columName = columns[i] + str(MARGEN_BRUTO_PORCENTAJE_ROW)
worksheet.write(columName, 'Margen btuto %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(MARGEN_BRUTO_PORCENTAJE_ROW)
    worksheet.write(columName, f) 
    i += 1
# Margen bruto %

# Margen bruto %
i = 0
filter_list = []
for f in table_element[0].select("tr")[7]:
    if is_not_blank(f.text):
        filter_list.append(f.text)
    else:
        filter_list.append(0)

del filter_list[0] # borro el texto
columName = columns[i] + str(EBITDA_ROW)
worksheet.write(columName, 'EBITDA')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(EBITDA_ROW)
    worksheet.write(columName, f) 
    i += 1
# Margen bruto %



workbook.close() 



