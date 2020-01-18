class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def PrintTree(self):
        if(self.root != None):
            self._PrintTree(self.root)

    def _PrintTree(self,node):
        if(node != None):
            self._PrintTree(node.left)
            print(str(node.value)+ ' ')
            self._PrintTree(node.right)

    def add(self,val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.value):
            if (node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if (node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)


    def find(self, val):
        if(self.root != None):
            return self.findx(val, self.root)
        else:
            return None
    def findx(self, val, node):
        if (val == node.value):
            print (node.value, "is found")
            return node.value
        elif(val < node.value):
            if (node.left != None):
                return self.findx(val, node.left)
            else:
                print(val, "is not in tree")
        elif(val > node.value):
            if (node.right != None):
                return self.findx(val, node.right)
            else:
                print(val, "is not in tree")


    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return (self._size(node.left) + 1 + self._size(node.right))

    def height(self):
        return self._height(self.root)


    def _height(self, node):
        if node == None:
            return 0
        else:
            lheight = self._height(node.left)
            rheight = self._height(node.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def printLevelOrder(self):
        h = self.height()
        '''for i in range(1, h+1):
            print("--------- %d ---------"%i)'''
        self.printGivenLevel(self.root, 3)
        print("abc")

    def printGivenLevel(self, node, level):
        if node is None:
            return 0
        if level == 1:
            #print("%s==============="%level)
            print(node.value)
        elif(level > 1):
            self.printGivenLevel(node.left, level-1)
            self.printGivenLevel(node.right, level-1)
        print("returning from PGL")



tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
print("@@@@@@@@@@@@@@@@@@@@@")
tree.PrintTree()
print("@@@@@@@@@@@@@@@@@@@@@")
print(tree.find(3))
print(tree.find(0))
print(tree.find(10))
print(tree.find(-1))
print(" BST Size is: " + str(tree.size()))
print(" Height of BST: " + str(tree.height()))
tree.printLevelOrder()