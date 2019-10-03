#Funcion para leer el txt


 main():
    #arr = [123,983,2,5,76,4,-12,43,-5,53,71,-34]
    temp=[]
    arr=[]

    file = open("texto.txt","r")
    for lines in file:
        num = lines.split(",")
        for i in range(len(num)):
            num[i]=int(num[i])
    for j in range(len(num)):
        temp.append(num[j])
    for k in range(len(temp)):
        arr.append(temp[k])2

    print("Input:"+ str(arr))
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Output:" + str(arr))


main()
