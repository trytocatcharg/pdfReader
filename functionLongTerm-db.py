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
DIVIDENDO_ORDINARIO_ROW = 14
PAYOUT_ROW = 15
VALOR_CONTABLE_ACCION_ROW = 16
DEUDA_NETA_ROW = 17
DEUDA_NETA_OVER_EBITDA_ROW = 18
DEUDA_NETA_OVER_CF_EXPLOTACION_ROW = 19
ROA_ROW = 20
ROE_ROW = 21
ROCE_ROW = 22
CF_EXPLOTACION_ROW = 23
CF_EXPLOTACION_PORCENTAJE_ROW = 24
CF_INVERSION_ROW = 25
CF_INVERSION_PORCENTAJE_ROW = 26
CF_FINANCIACION_ROW = 27
CF_FINANCIACION_PORCENTAJE_ROW = 28
VARIACION_TIPO_CAMBIO_ROW = 29
CF_NETO_ROW = 30
CF_NETO_PORCENTAJE_ROW = 31


url = "https://www.invertirenbolsa.info/historicodividendos/empresa/{0}".format(COMPANY)

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

# table_element = soup.select("div > section > div > section > div")
table_element = soup.findAll("div", {"class": "to-fixed"})

print(nowStr)

def format_value(s):
    if "NAN%" in str(s):
        return 0
    if "INF%" in str(s):
        return 0
    if "%" in str(s):
        return s.replace(',', '.')
    if bool(s and s.strip()):
        return s
    else:
        return 0

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
    filter_list.append(format_value(f.text))

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
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(COSTES_DE_VENTA_ROW)
worksheet.write(columName, 'Costes de venta')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(COSTES_DE_VENTA_ROW)
    worksheet.write(columName, convert_to_number(f))
    i += 1
# Coste de ventas

# Margen bruto
i = 0
filter_list = []
for f in table_element[0].select("tr")[5]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(MARGEN_BRUTO_ROW)
worksheet.write(columName, 'Margen bruto')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(MARGEN_BRUTO_ROW)
    worksheet.write(columName, convert_to_number(f))
    i += 1
# Margen bruto

# Margen bruto %
i = 0
filter_list = []
for f in table_element[0].select("tr")[6]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(MARGEN_BRUTO_PORCENTAJE_ROW)
worksheet.write(columName, 'Margen btuto %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(MARGEN_BRUTO_PORCENTAJE_ROW)
    worksheet.write(columName, f)
    i += 1
# Margen bruto %

# EBITDA
i = 0
filter_list = []
for f in table_element[0].select("tr")[7]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(EBITDA_ROW)
worksheet.write(columName, 'EBITDA')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(EBITDA_ROW)
    worksheet.write(columName, convert_to_number(f)) 
    i += 1
# EBITDA

# EBITDA %
i = 0
filter_list = []
for f in table_element[0].select("tr")[8]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(EBITDA_PORCENTAJE_ROW)
worksheet.write(columName, 'EBITDA %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(EBITDA_PORCENTAJE_ROW)
    worksheet.write(columName, f) 
    i += 1
# EBITDA %

# Margen ebitda/ventas
i = 0
filter_list = []
for f in table_element[0].select("tr")[9]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(MARGEN_EBITDA_OVER_VENTAS_ROW)
worksheet.write(columName, 'Margen EBITDA/Ventas')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(MARGEN_EBITDA_OVER_VENTAS_ROW)
    worksheet.write(columName, f)
    i += 1
# Margen ebitda/ventas

# EBIT
i = 0
filter_list = []
for f in table_element[0].select("tr")[10]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(EBIT_ROW)
worksheet.write(columName, 'EBIT')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(EBIT_ROW)
    worksheet.write(columName, convert_to_number(f))
    i += 1
# EBIT

# Margen EBIT/Ventas
i = 0
filter_list = []
for f in table_element[0].select("tr")[12]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(MARGEN_EBIT_OVER_VENTAS_ROW)
worksheet.write(columName, 'Margent EBIT / Ventas')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(MARGEN_EBIT_OVER_VENTAS_ROW)
    worksheet.write(columName, f) 
    i += 1
# Margen EBIT/Ventas

# Resultado neto ordinario
i = 0
filter_list = []
for f in table_element[0].select("tr")[13]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(RESULTADO_NETO_ORDINARIO_ROW)
worksheet.write(columName, 'Resultado neto ordinario')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(RESULTADO_NETO_ORDINARIO_ROW)
    worksheet.write(columName, convert_to_number(f))
    i += 1
# Resultado neto ordinario

# Resultado neto total
i = 0
filter_list = []
for f in table_element[0].select("tr")[14]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(RESULTADO_NETO_TOTAL_ROW)
worksheet.write(columName, 'Resultado neto total')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(RESULTADO_NETO_TOTAL_ROW)
    worksheet.write(columName, convert_to_number(f))
    i += 1
# Resultado neto total


# BPA ordinario
i = 0
filter_list = []
for f in table_element[0].select("tr")[15]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(BPA_ROW)
worksheet.write(columName, 'BPA ordinario')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(BPA_ROW)
    worksheet.write(columName, convert_to_number(f))
    i += 1
# BPA ordinario

# # BPA %
# i = 0
# filter_list = []
# for f in table_element[0].select("tr")[16]:
#     filter_list.append(format_value(f.text))

# del filter_list[0] # borro el texto
# columName = columns[i] + str(BPA_PORCENTAJE_ROW)
# worksheet.write(columName, 'BPA %')
# for f in reversed(filter_list):
#     columName = columns[i + 1] + str(BPA_PORCENTAJE_ROW)
#     worksheet.write(columName, f) 
#     i += 1
# # BPA %


# Dividendo ordinario
i = 0
filter_list = []
for f in table_element[0].select("tr")[19]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(DIVIDENDO_ORDINARIO_ROW)
worksheet.write(columName, 'Dividendo ordinario')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(DIVIDENDO_ORDINARIO_ROW)
    worksheet.write(columName, convert_to_number(f))
    i += 1
# Dividendo ordinario

# # Dividendo %
# i = 0
# filter_list = []
# for f in table_element[0].select("tr")[20]:
#     filter_list.append(format_value(f.text))

# del filter_list[0] # borro el texto
# columName = columns[i] + str(DIVIDENDO_ORDINARIO_PORCENTAJE_ROW)
# worksheet.write(columName, 'Dividendo %')
# for f in reversed(filter_list):
#     columName = columns[i + 1] + str(DIVIDENDO_ORDINARIO_PORCENTAJE_ROW)
#     worksheet.write(columName, f) 
#     i += 1
# # Dividendo %

# Payout %
i = 0
filter_list = []
for f in table_element[0].select("tr")[21]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(PAYOUT_ROW)
worksheet.write(columName, 'Payout %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(PAYOUT_ROW)
    worksheet.write(columName, f) 
    i += 1
# Payout %

# Deuda neta
i = 0
filter_list = []
for f in table_element[0].select("tr")[29]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(DEUDA_NETA_ROW)
worksheet.write(columName, 'Deuda neta')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(DEUDA_NETA_ROW)
    worksheet.write(columName, convert_to_number(f))
    i += 1
# Deuda neta

# Deuda neta / EBITDA
i = 0
filter_list = []
for f in table_element[0].select("tr")[31]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(DEUDA_NETA_OVER_EBITDA_ROW)
worksheet.write(columName, 'Deuda neta / EBITDA')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(DEUDA_NETA_OVER_EBITDA_ROW)
    worksheet.write(columName, convert_to_number(f) )
    i += 1
# Deuda neta / EBITDA


# ROA %
i = 0
filter_list = []
for f in table_element[0].select("tr")[33]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(ROA_ROW)
worksheet.write(columName, 'ROA %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(ROA_ROW)
    worksheet.write(columName, f) 
    i += 1
# ROA %

# ROE %
i = 0
filter_list = []
for f in table_element[0].select("tr")[34]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(ROE_ROW)
worksheet.write(columName, 'ROE %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(ROE_ROW)
    worksheet.write(columName, f) 
    i += 1
# ROE %

# ROCE %
i = 0
filter_list = []
for f in table_element[0].select("tr")[35]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(ROCE_ROW)
worksheet.write(columName, 'ROCE %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(ROCE_ROW)
    worksheet.write(columName, f) 
    i += 1
# ROCE %

# Cash-flow explotacion
i = 0
filter_list = []
for f in table_element[0].select("tr")[37]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(CF_EXPLOTACION_ROW)
worksheet.write(columName, 'CF explotacion')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(CF_EXPLOTACION_ROW)
    worksheet.write(columName, convert_to_number(f) )
    i += 1
# Cash-flow explotacion

# Cash-flow explotacion %
i = 0
filter_list = []
for f in table_element[0].select("tr")[38]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(CF_EXPLOTACION_PORCENTAJE_ROW)
worksheet.write(columName, 'CF explotacion %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(CF_EXPLOTACION_PORCENTAJE_ROW)
    worksheet.write(columName, f) 
# Cash-flow explotacion %


# Cash-flow inversion
i = 0
filter_list = []
for f in table_element[0].select("tr")[39]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(CF_INVERSION_ROW)
worksheet.write(columName, 'CF inversion')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(CF_INVERSION_ROW)
    worksheet.write(columName, convert_to_number(f) )
    i += 1
# Cash-flow inversion

# Cash-flow inversion %
i = 0
filter_list = []
for f in table_element[0].select("tr")[40]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(CF_INVERSION_PORCENTAJE_ROW)
worksheet.write(columName, 'CF inversion %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(CF_INVERSION_PORCENTAJE_ROW)
    worksheet.write(columName, f) 
# Cash-flow inversion %

# Cash-flow financiacion
i = 0
filter_list = []
for f in table_element[0].select("tr")[41]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(CF_FINANCIACION_ROW)
worksheet.write(columName, 'CF financiacion')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(CF_FINANCIACION_ROW)
    worksheet.write(columName, convert_to_number(f) )
    i += 1
# Cash-flow financiacion

# Cash-flow financiacion %
i = 0
filter_list = []
for f in table_element[0].select("tr")[42]:
    filter_list.append(format_value(f.text))

del filter_list[0] # borro el texto
columName = columns[i] + str(CF_FINANCIACION_PORCENTAJE_ROW)
worksheet.write(columName, 'CF financiacion %')
for f in reversed(filter_list):
    columName = columns[i + 1] + str(CF_FINANCIACION_PORCENTAJE_ROW)
    worksheet.write(columName, f) 
# Cash-flow financiacion %

workbook.close() 



