import requests
import datetime
import PyPDF2



url="https://www.bde.es/webbde/es/estadis/infoest/tc_1_1.pdf"
now =  datetime.datetime.now()
nowStr=(str(now)).split(' ')[0]
r = requests.get(url, stream=True)
pdfName='./pdf/bce_{0}.pdf'.format(nowStr)
fd=open(pdfName, 'wb')

with fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

 fileReader = PyPDF2.PdfFileReader(file)
 