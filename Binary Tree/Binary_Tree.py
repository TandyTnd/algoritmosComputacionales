import networkx as nx
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
            c +=1

    print("List: "+ str(setNumbers))
    return setNumbers


def main():
    nombres()
    createList()
main()