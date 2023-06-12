class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.leftChild=None
        self.rightChild=None
    
    def insert(self,data):
        if data <self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild=Node(data)
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
    
    def printTree(self,level=0):
        if self.rightChild:
            self.rightChild.printTree(level +1)
        if self.data!=None:
            print('   ' * level + '|--' + str(self.data))
        if self.leftChild:
            self.leftChild.printTree(level +1)    


    def search(self, target):
        if self.data == target:
            return True
        elif target < self.data and self.leftChild:
            return self.leftChild.search(target)
        elif target > self.data and self.rightChild:
            return self.rightChild.search(target)
        else:
            return False



r = Node(27)
childs = [12,11,35,22,19,22,45]
for i in childs:
    r.insert(i)
r.printTree()

print(r.search(5))