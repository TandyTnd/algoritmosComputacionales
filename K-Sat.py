keyNum = " 0"
index = []

file = open("texto.txt", "r")
def nombres():
    print("Alejandro Perez Gonzalez     A01746643")

def leerTexto():
    values=[]
    print("Leyendo....")
    for line in file:
        if keyNum in line:
            index.append(line)
        else:
            values.append(line)


    for x in range(len(index)):
        print(index[x])
    print("sobrante:")
    for y in range(len(values)):
        print(values[y])
    values.pop(0)
    values.pop(0)
    print("solo sobra: "+(str(values)))

    return values
    return index





def main():
    nombres()
    leerTexto()
main()