from Node import Node
from collections import deque
'''
Inorder (Left, Root, Right) : 4, 2, 5, 1, 3
Preorder (Root, Left, Right) : 1 2 4 5 3 
Postorder (Left, Right, Root) : 4, 5, 2, 3, 1
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

    def transver_layer_by_layer(self,root):
        '''
        It is breath first search. So, first define deque
        :param root:
        :return:
        '''
        if root is None:
            return []
        queqe = deque([root])
        result = []
        while queqe:
            level_size = len(queqe)
            current_level = []
            for _ in range(level_size):
                node = queqe.popleft()
                current_level.append(node.val)
                if node.left:
                    queqe.append(node.left)
                if node.right:
                    queqe.append(node.right)
            result.append(current_level)
        return result


a = Tree_Traverse(0)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#root.right.left = Node(5)
#root.right.right = Node(6)

'''
      1
    2    3  
 4   5
'''

a.postOrder(root)
