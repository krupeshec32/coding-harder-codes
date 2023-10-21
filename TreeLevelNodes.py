from Node import Node


class TreeLevelNodes:
    def __init__(self, root):
        self.root = root
        self.res = {}

    def getAns(self, root):
        if root is None:
            return
        q=[]
        q.append(root)
        while q:
            count = len(q)
            while count > 0:
                a = q.pop(0)
                print(a.data,end =' ')
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
                count=count-1
        print(' ')
leftNode = Node(400)
rightNode = Node(300)
x = Node(100)
x.left = leftNode
x.right = rightNode
tl = TreeLevelNodes(x)
result= tl.getAns(x)
