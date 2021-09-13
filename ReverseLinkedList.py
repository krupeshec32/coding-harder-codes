'''
reverse linked list
'''

from SingleLinkedListNode import SingleLinkedListNode


class ReverseLinkedList:

    def __init__(self, root):
        self.root = root

    def getReverse(self, root):
        current=root
        prev= None

        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        root=prev
        print(self.printrev(root))

    def printrev(self,root):
        while root is not None:
            print(root.data)
            root=root.next



x = SingleLinkedListNode(1)
y = SingleLinkedListNode(2)
z = SingleLinkedListNode(3)
x.next = y
y.next = z
x.prev = None
y.prev = x
z.prev = y
w=ReverseLinkedList(x)
w.printrev(x)
w.getReverse(x)