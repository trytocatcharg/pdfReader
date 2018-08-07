from urllib.request import urlopen



url='https://www.bde.es/webbde/es/secciones/informes/banota/bp0201.txt'
with urlopen(url) as txt:
    lines=[]
    for line in txt:
        line_words=line.split()
        for word in line_words:
            lines.append(word)

for w in lines:
    print(w)
