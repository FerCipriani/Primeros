import requests
import json
import os
from bs4 import BeautifulSoup

def QuitaAcentos(s):
    reemplaza = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplaza:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

Path= "C:/Users/fcipriani/Downloads/Programas/Scrap Udemy/"
Txt= "Pagni LaNacion Links.txt"
Archivo = open (Path + Txt,'r')
i = 185

print(i)

link ="".join(Archivo.readlines()[i])
Archivo.close()
link = link.strip()
print(link)

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}
url = 'https://www.lanacion.com.ar/politica/espionaje-maria-eugenia-vidal-elisa-carrio-acorralan-nid2232135'
respuesta = requests.get(link, headers=headers)
soup = BeautifulSoup(respuesta.text, features="lxml")
Titu = soup.find("h1", class_="titulo").text

cast = soup.find_all("body")
for ca in cast:
    tx="".join(ca.text)
    Ca1 = int(tx.find('podcast'))
    print(Ca1, "Podcast")
    Ca2 = int(tx.find('A continuación, sus principales conceptos:'))
    print(Ca2, 'Principales concep')

if (Ca1 != -1) or (Ca2 != -1):
    Pod = "Podc "
    print("Es un podcast")
    Cuerpo = soup.find_all(class_="lista-desordenada")
    Nota = []
    for i in range (len(Cuerpo)):
        Cuerpo[i] = Cuerpo[i].text
        Nota.append(Cuerpo[i])
    Nota = "\n".join(Nota)
else:
    Pod = ""
    print("Nota Normal")
    Cuer = soup.find(id="cuerpo")
    Parr = Cuer.find_all("p")
    Nota = []
    for i in range (len(Parr)-1):
        Parr[i]=Parr[i].text
        Nota.append(Parr[i])
    Nota = "".join(Nota)

datos = json.loads(soup.find('script', {'type':'application/ld+json'}).string)
Datecreado = datos["datePublished"][:10].replace('/','-')
Autor = QuitaAcentos(', '.join(datos["author"]))

Year= Datecreado[6:10]
mes= Datecreado[3:5]
dia = Datecreado[0:2]

Nota = QuitaAcentos(Nota).lower()
Titu = Titu.replace('"',"").replace("¿","").replace("?","").replace(":","")
Titu = QuitaAcentos(Titu)

Path= "C:/Users/fcipriani/Downloads/Programas/Scrap Udemy/HuDig/"
Archivo = "La Nacion "+ Year + "-" + mes+ "-" + dia + " " + Autor +" " + Pod + Titu
ftxt = open(Path + Archivo + ".txt", "w",encoding="utf8")
ftxt.write(Titu + "\n" + Nota)
ftxt.close()
print(Archivo)
print(os.path.getsize (Path + Archivo + ".txt"))

