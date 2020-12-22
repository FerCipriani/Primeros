from bs4 import BeautifulSoup

# Levanto los links de un txt
Path= "C:/Users/fcipriani/Downloads/Scrap Udemy/"
Txt= "Pagni LaNacion Links.txt"
Archivo = open (Path + Txt,'r')
link ="".join(Archivo.readlines(3))
Archivo.close()
print(link)

