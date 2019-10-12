import networkx as nx
file = open("graph.txt", 'r')

def nombres():
    print("Alejandro Perez Gonzalez     A01746643")
    print("Oscar Zuniga Lara            A01654827")

def limpiar():
    numset=[]
    for list in file:
        for char in list:
            if char.isdigit():
                numset.append(char)
    print(numset)

def main():
    nombres()
    limpiar()
    file.close()
main()