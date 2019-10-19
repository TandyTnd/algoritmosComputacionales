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
    print("Reading....")
    for line in file:
        if keyNum in line:
            index.append(line.splitlines())

        else:
            values.append(line.splitlines())



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

    print("Graph nodes:")
    print(listNodes)
    print("Node 1 succesors: " + str(G[1]))
    print("Node 2 succesors: " + str(G[2]))
    print("Node 3 succesors: " + str(G[3]))
    print("Node 4 succesors: " + str(G[4]))
    print("Node 5 succesors: " + str(G[5]))
    print("Node 6 succesors: " + str(G[6]))
    print("Node 7 succesors: " + str(G[7]))
    print("Node 8 succesors: " + str(G[8]))
    print("Node 9 succesors: " + str(G[9]))




def pageRank():
    rank=[]
    pr = nx.pagerank(G)
    print(pr)
    for x in range(len(pr)+1):
        rank.append(pr.get(x))
    rank.pop(0)
    print("======")
    print(rank)
    for i in range(len(rank)):
        for j in range(0,len(rank)-i-1):
            if rank[j]>rank[j+1]:
                rank[j],rank[j+1] = rank[j+1],rank[j]
    num = 1

    for place in rank:
        print(str(num)+"  "+str(place))
        num +=1



    nx.draw(G, with_labels=True)
    plt.show()





def main():
    nombres()
    leerTexto()
    crearGrafo()
    pageRank()
main()