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
        ('"', " "),
        ("?", " "),
         )
    for a, b in reemplaza:
        s = s.replace(a, b)
    return s
Path = 'C:/Users/fcipriani/Downloads/Programas/Scrap Udemy/HuDig/'
FileStop = 'stop.txt'   # archivo de stopwords
FileTest = 'test.txt'   # archivo a limpiar

Palabros = open(Path + FileStop,'r', encoding='utf-8')
Lista = Palabros.readlines()
Palabros.close()
del Lista[0]

for lis in Lista:
    Orden = Lista.index(lis)
    Lista[Orden] = lis.replace('\n', '')  # elimino saltos de línea


PathT = 'C:/Users/fcipriani/Downloads/Programas/Scrap Udemy/HuDig/Trabajo/'

with os.scandir(PathT) as Archivos:
   for Archivo in Archivos:
        print("Leyendo", Archivo)
        Cambio = open(Archivo,'r', encoding='utf-8')
        Cont = ''.join(Cambio.readlines()).lower().strip() # lo pongo en minúsculas y sin espacios
        Cambio.close()
        ListaCont = Cont.split() # lo transformo en lista
        del ListaCont[0] #Elimino el primero que trae basura del UTF-8

        ListaLimpia = []
        for LCon in ListaCont:
            OrCon = ListaCont.index(LCon)
            ListaCont[OrCon] = Limpia(LCon.replace('\n', '')).strip() #Quito retornos y espacios en blanco y limpio
            if len(ListaCont[OrCon]) > 2:
                ListaLimpia.append(ListaCont[OrCon]) #solo me quedo con de mas de dos letras

        ListaOtra = ListaLimpia
        NuevaLista = []
        for LisS in Lista:
            for LisL in ListaLimpia:
                if LisL == LisS:
                    ListaOtra[ListaLimpia.index(LisL)] = ""
        Finale = []
        for LiF in ListaOtra:
            if LiF  != "":
                Finale.append(LiF)
        print(len(Finale), Finale)
        listo = ' '.join(Finale)

        Tex1 = open(Archivo,'w+', encoding='utf-8')
        Tex1.write(listo)
        Tex1.close()
