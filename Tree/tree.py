class Node:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = Node

def insert(root, t):
    new = Node(t)
    if root == None:
        root = new
    else:
        node = root
        while True:
            if t < node.key:
            # go left
                if node.left == None:
                    node.left = new
                    node.parent = node
                    break
                node = node.left
            else:
            #go right
                if node.right == None:
                    node.right = new
                    node.parent = node
                    break
                node = node.right

    return new



