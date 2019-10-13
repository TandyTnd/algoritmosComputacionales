import networkx as nx
file = open("graph.txt", 'r')

def nombres():
    print("Alejandro Perez Gonzalez     A01746643")
    print("Oscar Zuniga Lara            A01654827")

def limpiar():
    numset=[]
    tempset=[]
    for list in file:
        for char in list:
            if char.isdigit():
                tempset.append(char)
                numset.append(tempset)
            tempset.clear()
    print(numset)



def main():
    nombres()
    limpiar()
    file.close()
main()