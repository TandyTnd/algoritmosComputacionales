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

    #values = values[0]
    #values[0] = int(values[0])


    for i in range (0, len(values)):
        a = (values[i][0])
        i1 = int (a[1])
        i2 = int (a[3])
        print(i1)
        print(i2)
        values2.append([i1, i2])
    print(values2)


def main():
    nombres()
    leerTexto()
main()