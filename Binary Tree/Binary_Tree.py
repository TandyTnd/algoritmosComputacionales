
setNumbers=[]


class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = int(key)


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
            c += 1

    print("List: "+ str(setNumbers))
    return setNumbers

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def addNodes():
    r = Node(setNumbers[0])
    for number in range(1,len(setNumbers)):
        insert(r, Node(setNumbers[number]))
    inorder(r)


def main():
    nombres()
    print("/////////////////////")
    createList()
    print("###############################")
    print("Sorted: ")
    addNodes()

main()