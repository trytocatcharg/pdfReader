import requests
import datetime
import PyPDF2



url="https://www.bde.es/webbde/es/estadis/infoest/tc_1_1.pdf"
now =  datetime.datetime.now()
# yyy--mm--dd
nowStr=(str(now)).split(' ')[0] 
# Nombre del archivo pdf formato bce_fecha_actual.pdf
pdfName='./pdf/bce_{0}.pdf'.format(nowStr)

r = requests.get(url, stream=True)
fd=open(pdfName, 'wb')

with fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

pdfReader = PyPDF2.PdfFileReader(pdfName)
# creating a page object
pageObj = pdfReader.getPage(0)
 
# extracting text from page
print(pageObj.extractText())
