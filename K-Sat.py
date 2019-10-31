import math
import random

keyNum = " 0"
index = []
values2 = []

nonTrueSets = []


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
    #print("Values: "+ str (values))
    values = values[0]
    values[0] = int(values[0])



    values = randomSolution(len(str(values[0])))
    print("VALUES" + str(values))
    var = values


    for i in range (0, len(str(var))):

        p = str(var)[i]

        if (p == "0"):
            values2.append(False)
        elif (p == "1"):
            values2.append(True)
    #print(values)

    return values
    return index

def comparaList():
    print("AAAAA"+ str(values2))
    for i in range (0, len(index)):
        #print(i)
        arr = (str(index[i][0]).split())
        #print("============================================")
        #print("Computing....")
        #print(arr)
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
            #print("VAL DE SET = TRUE")
            pass
        else:
            #print("VAL DE SET = FALSE")
            nonTrueSets.append(i)
    print(values2)
    print("VALORES NO CUMPLIDOS")
    print(nonTrueSets)

def randomSolution(largo):

    randomSolution = []
    
    for i in range(largo):
        randomNumber = random.getrandbits(1)
        randomSolution.append(randomNumber)
    return randomSolution


if __name__ == '__main__':
    nombres()
    leerTexto()
    comparaList()

    if (len(nonTrueSets) > 0):
        for i in range(0, 4):
            if (len((nonTrueSets))== 0):
                print("ENCONTRADO")
                break
            else:
                print("CAMBIA   "+ str(i))
                noc = len(nonTrueSets)
                print("NON TRUE SETS:   " + str(noc))
                setAcambiar = random.randint(0, noc + 1)
                print("SET A CAMBIAR    " + str(setAcambiar))
                arr = (str(index[setAcambiar][0]).split())

                valACambiar1 = random.randint(0, 3)
                valACambiar = int(arr[valACambiar1])
                print(valACambiar)
                print(arr)

                values2[abs(setAcambiar)] = not (values2[setAcambiar])
                comparaList()
    #print(randomSolution(21))

