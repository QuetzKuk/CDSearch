import csv
import os

tabladediscos = ".\discos.csv"
discosscheme = ["disco","banda","genero","año", "rating"]
discos = []

def crear_disco (disco):
    global discos
    discos.append(disco)

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

def update_disc(disco_id, updated_disco):
    global discos
    if len(discos) -1 >= disco_id:
        discos[disco_id] = updated_disco
    else:
        print("Disco no registrado")

def borrar_disco():
    global discos
    for idx, disco in enumerate(discos):
        if idx == disco_id:
            del discos[idx]
            list_discos()
            break

def get_disco_field(field_name, message="Ingresa el {} \n"):
    field = None
    while not field:
        field = input(message.format(field_name))
    return field

def get_datos_disco():
    disco={
        "disco":get_disco_field("disco").title(),
        "banda":get_disco_field("banda").title(),
        "genero": get_disco_field("genero").title(),
        "año":int(get_disco_field("año")),
        "rating":float(get_disco_field("rating"))
    }
    return disco

def init_discos_from_store():
    with open(tabladediscos, mode="r") as f:
        reader = csv.DictReader(f, fieldnames=discosscheme)
        for row in reader:
            discos.append(row)

def save_discos():
    tmp_table_name = "{}.tmp".format(tabladediscos)
    with open(tmp_table_name, mode="w") as f:
        writer = csv.DictWriter(f,fieldnames=discosscheme)
        writer.writerows(discos)
    os.remove(tabladediscos)
    os.rename(tmp_table_name, tabladediscos)

def salir():
    print ("~"*10, "Adios lml", "~"*10)
    exit()

def portadaprincipal():
    print("Desplegar menú principal \n")
    resp1 = input ("S/N =>")
    resp1 = resp1.upper()
    if resp1 == "S":
        portada()
    if resp1 == "N":
        salir()        

def portada():
    print ("+" *5, "Menu principal", "+" *5)
    print ("[C]rear registro de disco(Nombre,Banda Género, Año, Rating)")
    print("[E]ditar/Actualizar disco")
    print("[B]orrar disco")
    print("[R]evisar discos")
    print ("[F]iltro por bandas")
    print("[S]alir")
    menuex()

def menuex():
    command = input()
    command = command.upper()

    if command == "C":
        client = get_datos_disco()
        crear_disco(client)
    
    elif command == "E": #editar
        disco_id = int(get_disco_field("id"))
        updated_disco = get_datos_disco()
        update_disc(disco_id, updated_disco)

    elif command == "B":
        disco_id = int(get_disco_field("id"))
        borrar_disco()

    elif command == "R": #revisar lista
        list_discos()
        portadaprincipal()

    elif command == "F":
        import filtrobands
        banda =input("Escribe una banda \n")
        banda = banda.title()
        filtrobands.filtroporbanda(banda)
        retmenu = input("Regresar a menu principal? S/N \n")
        retmenu = retmenu.upper()
        if retmenu == "S":
            portadaprincipal()
        elif retmenu == "N":
            print ("Fin de consulta")

    elif command == "S":
        salir()

    else:
        print ("Comando inválido")


if __name__=="__main__":
    init_discos_from_store()
    portadaprincipal()
    

    save_discos()