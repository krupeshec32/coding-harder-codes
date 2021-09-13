from Node import Node
import math


class IsValidBinarySearchTree:
    def isValidBST(self, root: Node) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.data <= low or node.data >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.data, high) and
                    validate(node.left, low, node.data))

        return validate(root)
x=IsValidBinarySearchTree()
root=Node(2)
root.right=Node(3)
root.left=Node(1)
print(x.isValidBST(root))
