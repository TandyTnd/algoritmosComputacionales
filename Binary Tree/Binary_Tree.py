import networkx as nx
import matplotlib.pyplot as plt
setNumbers=[]

def nombres():
    print("Alejandro Perez Gonzalez     A01746643")
    print("Oscar Zuniga Lara            A01654827")

def createList():
    size = int(input("Enter the list size: "))
    c = 0
    while c < size:
        number =  int(input("Enter number: "))
        if setNumbers == None:
            setNumbers.append(number)
            c += 1
        elif number in setNumbers:
            print("Repeated values are not allowed!")

        else:
            setNumbers.append(number)
            c += 1

    print("List: "+ str(setNumbers))
    return setNumbers
def tree():
    t = nx.Graph()
    t.add_node(setNumbers[0])
    plt.title("Binary tree")
    nx.draw_networkx(t)

    plt.show()

def extree():
    G = nx.Graph()

    G.add_node("ROOT")

    for i in range(5):
        G.add_node("Child_%i" % i)
        G.add_node("Grandchild_%i" % i)
        G.add_node("Greatgrandchild_%i" % i)

        G.add_edge("ROOT", "Child_%i" % i)
        G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
        G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

    plt.title("draw_networkx")
    nx.draw_networkx(G)

    plt.show()


def main():
    nombres()
    print("/////////////////////")
    createList()
    print("###############################")
    tree()
    print("################################")
    extree()
main()