import os
def Limpia(s): # Funcion limpia caracteres
    reemplaza = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
        (")", " "),
        (".", " "),
        (",", " "),
        ("-", " "),
        (";", " "),
        ("(", " "),
        ("¿", " "),
        ("%", " "),
        ("–", " "),
        ("‑", " "),
        (":", " "),
         )
    for a, b in reemplaza:
        s = s.replace(a, b)
    return s

Path = 'C:/Users/fcipriani/Downloads/Programas/Scrap Udemy/HuDig/'
FileReem = 'reem.txt'   # archivo de reemplazos

Palabros = open(Path + FileReem,'r', encoding='utf-8')
Lista = Palabros.readlines()
Palabros.close()

del Lista[0]
Uno = []
Dos = []

for lis in Lista:
     XX = lis.find(',')
     Uno.append(lis[0:lis.find(',')])
     Dos.append(lis[lis.find(',')+2:len(lis)].replace('\n', ''))

PathT = 'C:/Users/fcipriani/Downloads/Programas/Scrap Udemy/HuDig/IVE limpio nuevo/'

with os.scandir(PathT) as Archivos:

   for Archivo in Archivos:
        Cambio = open(Archivo,'r', encoding='utf-8')
        Cont = ''.join(Cambio.readlines()).lower().strip() # lo pongo en minúsculas y sin espacios
        Cambio.close()
        ListaCont = Cont.split() # lo transformo en lista
        del ListaCont[0]

        ListaLimpia = []

        for LCon in ListaCont:
            OrCon = ListaCont.index(LCon)
            ListaCont[OrCon] = Limpia(LCon.replace('\n', '')).strip() #Quito retornos y espacios en blanco y limpio

        for LisR in Uno:
            OrdUno = Uno.index(LisR)
            for LisP in ListaCont:
                if LisR == LisP:
                    Ord = ListaCont.index(LisP)
                    ListaCont[Ord] = Dos[OrdUno]
        listo = ' '.join(ListaCont)
        #print(listo)
        Tex1 = open(Archivo, 'w+', encoding='utf-8')
        Tex1.write(listo)
        Tex1.close()
