from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
import datetime
import xlsxwriter


now =  datetime.datetime.now()
# yyy--mm--dd HH:MM
nowStr = (str(now)).split(' ')[0 ]+ '_{0}'.format(now.strftime("%H-%M"))
COMPANY = 'zardoya-otis'
url = "https://www.invertirenbolsa.info/historicodividendos/empresa/{0}".format(COMPANY)

with urlopen(url) as html_txt:
    soup = BeautifulSoup(html_txt, 'lxml')

# table_element = soup.select("div > section > div > section > div")
table_element = soup.findAll("div", {"class": "to-fixed"})

print(nowStr)

def format_value(s):
    value = s.strip()
    if "NAN%" in str(value):
        return 0
    if "INF%" in str(value):
        return 0
    if "%" in str(value):
        return float(value.replace('%', '').replace(',', '.'))
    if bool(s and value):
        return float(value.replace('.', '').replace(',', '.'))
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
fix_rows = ['Ingresos', 'EBITDA', 'Coste de Ventas', 'Margen bruto', 'Margen EBITDA / Ventas', 'EBIT', 'Margen EBIT / Ventas', 'Resultado neto ordinario', 'BPA ordinario', 'Pay-out', 'Dividendo total', 'Deuda neta', 'Deuda neta / EBITDA', 'ROA', 'ROE', 'ROCE', 'Cash-flow de explotación', 'Cash-flow de inversión', 'Cash-flow de financiación', 'Cash-flow neto', 'CFE-CFI-PID', 'Pago por dividendos', 'Cotización máxima', 'Cotización mínima', 'PER máximo', 'PER medio', 'PER mínimo', 'RD% máxima', 'RD% media', 'RD% mínima', 'EV / EBITDA máximo', 'EV / EBITDA medio', 'EV / EBITDA mínimo']

i = 1
# # Años
for f in reversed(table_element[0].select("th")):
    columName = columns[i] + str(1)
    worksheet.write(columName, f.text) 
    i += 1
# # Años

i = 1
row_in_excel = 1
for row_excel_name in fix_rows:
    print (row_excel_name)
    i += 1
    row_in_excel +=1
    worksheet.write(columns[0] + str(i), row_excel_name) # columna 0 el titulo ( ingresos, ebitda, etc)
    for element_id in range(1, len(table_element[0].select("tr"))):
        row_selected = []
        for f in table_element[0].select("tr")[element_id]:
            row_selected.append(f.text)

        title_row = row_selected[0].strip()
        del row_selected[0] # borro el texto de la columna 0 (ingresos, ebitda, etc)
        column_in_excel = 1
        if row_excel_name == title_row:
            for f in reversed(row_selected):
                columName = columns[column_in_excel] + str(row_in_excel)
                print(columName)
                value_to_insert = format_value(f) 
                print(value_to_insert)
                worksheet.write(columName, value_to_insert)
                column_in_excel += 1
            break
            
            
        
workbook.close() 
