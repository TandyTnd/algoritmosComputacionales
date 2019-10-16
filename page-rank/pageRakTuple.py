import networkx as nx

keyNum = " 0"
index = []
values2 = []


file = open("graph.txt", 'r')

def nombres():
    print("Alejandro Perez Gonzalez     A01746643")
    print("Oscar Zuniga Lara            A01654827")

def leerTexto():
    values=[]
    print("Leyendo....")
    for line in file:
        if keyNum in line:
            index.append(line.splitlines())

        else:
            values.append(line.splitlines())

    print("Index: ")
    for x in range(len(index)):
        print(index[x])
    values.pop(0)
    values.pop(0)
    print("=======================================")
    print("Values: "+ str (values))
    values = values[0]
    values[0] = int(values[0])


    var = values[0]


    for i in range (0, len(str(var))):

        p = str(var)[i]

        if (p == "0"):
            values2.append(False)
        elif (p == "1"):
            values2.append(True)
    return values

def main():
    nombres()
    leerTexto()
main()