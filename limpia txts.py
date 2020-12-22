#levanta los txt de /pagni y les saca los acentos, pasa amnimísculas y quita enies. Casi siempre funciona
#los archovos tienen que estar en UFT-8 para que no de error
import os
def QuitaAcentos(s):
    reemplaza = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
    )
    for a, b in reemplaza:
        s = s.replace(a, b).replace(a.upper(), b.upper()).replace("¿"," ").replace("%"," ")
    return s

Path = 'C:/Users/fcipriani/Downloads/Programas/Scrap Udemy/HuDig/IVE/'
with os.scandir(Path) as Archivos:
    for Archivo in Archivos:
        Tex1 = open(Archivo,'r', encoding='utf-8')
        print(Archivo.name, 'Leido')
        Contenido = QuitaAcentos(''.join(Tex1.readlines()))
        Contenido = Contenido.replace('(aplausos.)','').replace('Señor presidente', '').replace('\n', ' ').replace('\r', '')
        Contenido = Contenido.lower().replace('        ', '')
        Tex1.close()
        Tex1 = open(Archivo,'w+', encoding='utf-8')
        Tex1.write(Contenido)
        print(Archivo.name, 'Escrito')
        Tex1.close()





