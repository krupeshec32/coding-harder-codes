from Node import Node
'''
Inorder (Left, Root, Right) : 4 2 5 1 3 
Preorder (Root, Left, Right) : 1 2 4 5 3 
Postorder (Left, Right, Root) : 4
'''

class Tree_Traverse():

    def __init__(self, node):
        self.node = node

    def preOrder(self, node):
        if node is None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data)
        self.inOrder(node.right)

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data)

a = Tree_Traverse(0)
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
#root.right.left = Node(5)
#root.right.right = Node(6)

a.inOrder(root)
