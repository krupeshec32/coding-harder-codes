# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
'''

from Node import Node


class SumOfLeftMostNodesOfTree:
    def sumOfLeftLeaves(self, root: Node) -> int:

        if root is None:
            return 0

        total = 0
        stack = [root]

        while (stack):
            s = stack.pop()
            if self.is_left_most(s.left):
                total = total + s.left.data
            if s.left is not None:
                stack.append(s.left)
            if s.right is not None:
                stack.append(s.right)
        return total

    def is_left_most(self, root):
        if root is not None and root.left is None and root.right is None:
            return True

p=SumOfLeftMostNodesOfTree()
x=Node(1)
y=Node(2)
z=Node(3)
w=Node(4)
x.left=y
x.right=z
x.right.left=w
print(p.sumOfLeftLeaves(x))

