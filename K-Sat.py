keyNum = " 0"
index = []

file = open("texto.txt", "r")
def nombres():
    print("Alejandro Perez Gonzalez     A01746643")

def leerTexto():
    arrayVals=[]
    values=[]
    print("Leyendo....")
    for line in file:
        if keyNum in line:
            index.append(line)
        else:
            values.append(line)

    for x in range(len(index)):
        print(index[x])
    print("====================================================")

    values.pop(0)
    values.pop(0)
    print("Index values: ")
    for elements in values:
        for digits in elements:
            arrayVals.append(digits)
    arrayVals.pop(20)

    print(arrayVals)

    return arrayVals
    return index

def calculateSAT():
    for set in index:
        for digit in set:
            print("====")
            print(digit)

def main():
    nombres()
    leerTexto()
    calculateSAT()
main()