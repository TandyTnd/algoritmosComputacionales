import math

keyNum = " 0"
index = []
values2 = []


file = open("texto.txt", "r")
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
    return index

def comparaList():
    for i in range (0, len(index)):
        arr = (str(index[i][0]).split())
        print("============================================")
        print("Computing....")
        print(arr)

        e1 = int(arr[0])
        e2 = int(arr[1])
        e3 = int(arr[2])

        if ((e1) <0 ):
            a1 = not values2[int(math.fabs(e1))-1]
        else:
            a1 = values2[int(math.fabs(e1))-1]

        if ((e2) <0 ):
            a2= not values2[int(math.fabs(e2))-1]
        else:
            a2 = values2[int(math.fabs(e2))-1]

        if ((e3) <0 ):
            a3 = not values2[int(math.fabs(e3))-1]
        else:
            a3 = values2[int(math.fabs(e3))-1]

        if (a1 or a2 or a3):
            pass
        else:
            return ("Result:\nP = 0")
if __name__ == '__main__':
    nombres()
    leerTexto()
    print(comparaList())
