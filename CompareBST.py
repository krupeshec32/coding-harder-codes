from Node import Node


class CompareBST:

    def __init__(self, root1, root2):
        self.root1 = root1
        self.root2 = root2

    def compare(self, root1, root2):

        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        if root1.data != root2.data:
            return False
        return self.compare(root1.right, root2.right) and self.compare(root1.left, root2.left)


x = Node(2)
#y = Node(1)
#z = Node(3)
#x.right = z
#x.left = y

a = Node(2)
#b = Node(1)
#c = Node(3)
#a.right = c
#a.left = b

p = CompareBST(x, a)
p.compare(x, a)
assert(p.compare(x, a))