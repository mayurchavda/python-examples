class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def PrintTree(self):
        if self.root != None:
            self._PrintTree(self.root)
    def _PrintTree(self, node):
        if (node != None):
            self._PrintTree(node.left)
            print(node.value)
            self._PrintTree(node.right)

    def add(self,val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(self.root, val)

    def _add(self, node, val):
        if (val < node.value):
            if (node.left == None):
                node.left = Node(val)
            else:
                self._add(node.left, val)
        else:
            if (node.right == None):
                node.right = Node(val)
            else:
                self._add(node.right, val)

    def countNode(self):
        return self._countNode(self.root)
    def _countNode(self, node):
        if node == None:
            return 0
        else:
            return self._countNode(node.left) + 1 + self._countNode(node.right)

    

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
tree.PrintTree()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(tree.countNode())