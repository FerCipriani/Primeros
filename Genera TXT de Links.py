from bs4 import BeautifulSoup
# Levanto los links de un txt donde tengo el HTML
Path= "C:/Users/fcipriani/Downloads/"
Txt= "Pagni.txt"
Archivo = open (Path + Txt,'r')
mensaje = Archivo.read()
Archivo.close()

soup = BeautifulSoup(mensaje, features="lxml")
contene = soup.find(class_="listado")
contenedor = contene.find_all("a", class_="figure")
i=0
Guardando = open("Pagni LaNacion Links.txt", "w")
for conte in contenedor:
  i+= 1
  link = conte.get_attribute_list('href')
  link = "https://www.lanacion.com.ar"+"".join(link).strip()
  print(link, file = Guardando)
print(i)
Guardando.close()


