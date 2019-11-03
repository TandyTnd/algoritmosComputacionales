import math
import random

keyNum = " 0"
index = []
values = []
file = open("texto.txt", "r")
arr = []
values2 = []

numSET = 0
def nombres():
    print("Alejandro Perez Gonzalez     A01746643")
    print("Oscar Zuniga Lara            A01654827")

def leerTexto():
    print("Leyendo....")
    for line in file:
        if keyNum in line:
            index.append(line.splitlines())
    #print("Index: ")
    #print(index)
    return index

def comparaList(values2):



    print("COMPARANDO")
    print(values2)
    nonTrueSets1 = []
    for i in range(0, len(index)):
        #print(i)
        arr = (str(index[i][0]).split())
        # print("============================================")
        #print("Computing....")
        #print(arr)
        e1 = int(arr[0])
        e2 = int(arr[1])
        e3 = int(arr[2])

        if ((e1) < 0):
            a1 = not values2[int(math.fabs(e1)) - 1]
        else:
            a1 = values2[int(math.fabs(e1)) - 1]
        if ((e2) < 0):
            a2 = not values2[int(math.fabs(e2)) - 1]
        else:
            a2 = values2[int(math.fabs(e2)) - 1]
        if ((e3) < 0):
            a3 = not values2[int(math.fabs(e3)) - 1]
        else:
            a3 = values2[int(math.fabs(e3)) - 1]

        if (a1 or a2 or a3):
            # print("VAL DE SET = TRUE")
            pass
        else:
            #print("VAL DE SET = FALSE   " + str(i))
            nonTrueSets1.append(i)
    nonTrueSets = nonTrueSets1
    print("VALORES NO CUMPLIDOS" + str(nonTrueSets))
    return nonTrueSets
def randomSolution(largo):
    randomSolution = []

    for i in range(largo):
        randomNumber = random.getrandbits(1)
        randomSolution.append(randomNumber)
    return randomSolution

def values2Generator():
    print("NEW SET #####################")
    values = randomSolution((20))
    values2 = []
    print("VALUES" + str(values))
    var = values
    for i in range(0, len(str(var))):
        p = str(var)[i]
        if (p == "0"):
            values2.append(False)
        elif (p == "1"):
            values2.append(True)

    return values2

def intenta(nonTrueSets):
    if (len(nonTrueSets) > 0):
        values2 = values2Generator()
        comparaList(values2)
        for i in range(0, 3):
            print("CAMBIA  VEZ" + str(i))
            if (nonTrueSets==0):
                print("RESUELTO")
                break
            else:
                noc = len(nonTrueSets)
                print("NON TRUE SETS:   " + str(noc))
                setAcambiar = random.randint(0, noc )
                print("SET A CAMBIAR    " + str(setAcambiar))
                valACambiardeSET = random.randint(0, 2)

                valACambiarList = ((index[setAcambiar][0]).split())


                valACambiar = int(valACambiarList[valACambiardeSET])
                valACambiar = abs(valACambiar)

                print(valACambiarList)
                print("valor a cambiar: " + str(valACambiar))

                valFinal = values2[valACambiar-1]

                values2[(valACambiar)-1] = not valFinal
                nonTrueSets = comparaList(values2)


    print(values2)
    print("SETS NO SATISFECHOS:")
    print(nonTrueSets)


if __name__ == '__main__':
    nombres()
    leerTexto()
    nonTrueSets = comparaList(values2Generator())
    intenta(nonTrueSets)


    # print(randomSolution(21))
