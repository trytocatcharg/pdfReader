import csv
import requests
from lxml import html


url="https://www.bde.es/webbde/es/estadis/infoest/series/tc_1_1.csv"

with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content
    #cr = csv.reader(decoded_content, delimiter=',')
    html_parse = html.fromstring(decoded_content)
    print(html_parse)
    # my_list = list(decoded_content)
    # for row in my_list:
    #     print(row)