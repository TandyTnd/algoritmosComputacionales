keyNum = " 0"
satValues = []
def nombres():
    print("Alejandro Perez Gonzalez     A01746643")

def leerTexto():
    print("Leyendo....")
    with open("texto.txt") as lines:
        for line in lines:
            if keyNum in line:
                satValues.append(line)
    for x in range(len(satValues)):
        print(satValues[x])


def main():
    nombres()
    leerTexto()
main()
