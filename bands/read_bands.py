import csv

def readcsv(path):
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        header = next(reader)
    
        totalbandas = []
        for row in reader:
            encabezado = zip(header,row)
            bandas_dic = {key: value for key, value in encabezado}
            totalbandas.append(bandas_dic)
        return totalbandas


def opciones(path):
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        header = next(reader)
        return header


def filterop():
    listaop = list(filter(
        lambda item: item["Origen"] == option, readcsv("bands/bandas.csv")
    ))
    print (listaop)

option = input("Elige el origen =>")
filterop()

if __name__ == "__main__":
    totalbandas = readcsv("bandas.csv")
    opciones1 = opciones("bandas.csv")
    


'''       
if __name__ == "__main__":
    data = readcsv ("bandas.csv")
    print (data[0])
'''
'''        
def readcsv2(path):
	with open(path,"r") as csvfile:
		reader = csv.reader(csvfile,delimiter=",")
		for row in reader:
		    print ("fila ====", row)

if __name__ == "__main__":
    readcsv2 ("bandas.csv")

    '''