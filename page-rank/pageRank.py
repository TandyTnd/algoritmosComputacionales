import networkx as nx
file = open("graph.txt", 'r')

def nombres():
    print("Alejandro Perez Gonzalez     A01746643")
    print("Oscar Zuniga Lara            A01654827")

def limpiar():
    numset=[]
    for list in file:
        numset.append(list)
    print(numset)

    for elem in numset:
        for char in elem:
            if char == '(':
                char.split("(")
    print(numset)

def main():
    nombres()
    limpiar()
    file.close()
main()