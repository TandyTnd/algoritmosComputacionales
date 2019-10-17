import networkx as nx
import matplotlib.pyplot as plt

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

    for i in range (0, len(values)):
        a = (values[i][0])
        i1 = int (a[1])
        i2 = int (a[3])
        values2.append([i1, i2])
    print(values2)


def PAGERANK():
    G = nx.Graph()

    listNodes = []

    for i in range(0, len(values2)):
        a1, a2 = values2[i][0], values2[i][1]
        #print(a1, a2)
        if not (a1 in listNodes ):
            listNodes.append(a1)
            G.add_node(a1)

    for i in range(0, len(values2)):
        a1, a2 = values2[i][0], values2[i][1]
        G.add_edge(a1, a2)

    print(listNodes)
    print(G)
    G.graph

def main():
    nombres()
    leerTexto()
    PAGERANK()
main()