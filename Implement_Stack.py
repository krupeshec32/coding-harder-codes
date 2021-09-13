from SingleLinkedListNode import SingleLinkedListNode


class Implement_Stack:
    def __init__(self, node):
        self.node = node

    def push(self, node, val):
        while node.next is not None:
            node = node.next
            pass
        newNode = SingleLinkedListNode(val)
        node.next = newNode
        newNode.prev = node

    def print(self, node):
        while node is not None:
            print(node.data)
            node = node.next

    def pop(self, node):
        while node.next is not None:
            node = node.next
        node.prev.next = None
        node = None


a = SingleLinkedListNode(1)
b = SingleLinkedListNode(2)
a.next = b
p = Implement_Stack(a)
p.print(a)
print('now calling push')
p.push(a, 3)
p.print(a)
print('lets call pop')
p.pop(a)
p.print(a)
