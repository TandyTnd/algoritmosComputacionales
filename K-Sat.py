keyNum = " 0"
index = []

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


    for x in range(len(index)):
        print(index[x])
    print("sobrante:")
    for y in range(len(values)):
        print(values[y])
    values.pop(0)
    values.pop(0)

    print("solo sobra: "+ str (values))
    values = values[0]
    values[0] = int(values[0])

    ##print(values)
    var = values[0]

    ##print(var)
    values2 =[]
    for i in range (0, len(str(var))):
        ##print(str(var)[i])
        p = str(var)[i]

        if (p == "0"):
            values2.append(False)
        elif (p == "1"):
            values2.append(True)
    print(values2)

    return values
    return index






def main():
    nombres()
    leerTexto()

main()