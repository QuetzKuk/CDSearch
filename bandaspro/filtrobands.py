import csv

tabladediscos = ".\discos.csv"
discosscheme = ["disco","banda","genero","año", "rating"]
discos = []

def list_discos():
    print ("Id | Disco | Banda | Genero | Año | Rating")
    print ("~" * 30)
    for idx, disco in enumerate(discos):
        print ("{DiD} | {disco} | {banda} | {genero} | {año} | {rating}".format(
            DiD= idx,
            disco= disco["disco"],
            banda=disco["banda"],
            genero = disco["genero"],
            año = disco["año"],
            rating= disco["rating"]
        ))

def init_discos_from_store():
    with open(tabladediscos, mode="r") as f:
        reader = csv.DictReader(f, fieldnames=discosscheme)
        for row in reader:
            discos.append(row)

def filtroporbanda(banda):
    listaporbanda = list(filter(lambda item: item["banda"] == banda, discos))
    print (listaporbanda)

def filtroxgenero(genero):
    listaporgenero = list(filter(lambda item: item["genero"] == genero, discos))
    print (listaporgenero)    

def continuar():
    respc = input("Desea regresar al menú? S/N")
    respc = respc.upper()
    if respc == "S":
        portada3()
    elif respc == "N":
        print("Adios")
        exit()    

def menu():
    print("*!"*20)
    print("[L]istar discos")
    print("Filtrar por [B]anda")
    print("filtrar por [G]enero")
    print("[S]alir")

def menufunc():
    menu()
    command = input("Elige una opción \n")
    command = command.upper()
    if command == "L":
        list_discos()
        continuar()

    elif command == "B":
        banda =input("Escribe una banda \n")
        banda = banda.title()
        filtroporbanda(banda)
        continuar()

    elif command == "G":
        genero =input("Escribe un genero \n")
        genero = genero.title()
        filtroxgenero(genero)
        continuar()
    elif command == "N":
        continuar()
    elif command =="S":
        print ("Salir")
        exit()
    else:
        print ("Comando inválido")
        continuar()

def portada2():
    print("Desplegar menú?")
    resp = input("S/N =>")
    resp = resp.upper()
    if resp == "S":
        menu()    

def portada3():
    menufunc()

init_discos_from_store()

portada3()




    






