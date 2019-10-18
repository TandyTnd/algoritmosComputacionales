import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
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

    print("indice: " +str(index))
    print("values: "+str(values))

    for x in range(len(index)):
        print(index[x])

    print("=======================================")
    for i in range (0, len(values)):
        a = (values[i][0])
        i1 = int (a[1])
        i2 = int (a[3])
        values2.append([i1, i2])
def crearGrafo():
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

    print("Nodos del grafo:")
    print(listNodes)
    print("Vecinos de nodo 1: " + str(G[1]))
    print("Vecinos de nodo 2: " + str(G[2]))
    print("Vecinos de nodo 3: " + str(G[3]))
    print("Vecinos de nodo 4: " + str(G[4]))
    print("Vecinos de nodo 5: " + str(G[5]))
    print("Vecinos de nodo 6: " + str(G[6]))
    print("Vecinos de nodo 7: " + str(G[7]))
    print("Vecinos de nodo 8: " + str(G[8]))
    print("Vecinos de nodo 9: " + str(G[9]))

    nx.draw(G, with_labels=True)
    plt.show()


#def pageRank():



def main():
    nombres()
    leerTexto()
    crearGrafo()
    #pageRank()
main()