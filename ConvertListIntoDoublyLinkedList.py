from SingleLinkedListNode import SingleLinkedListNode


class ConvertListIntoDoublyLinkedList:

    def __init__(self, list):
        self.list = list

    def getDoubleLinkedList(self, list):
        root = SingleLinkedListNode(list[0])   #1
        current = dummy=root
        root.prev = None

        for i in range(1, len(list)):
            current.next = SingleLinkedListNode(list[i])  #2
            current= current.next    #2
        return dummy

    def lst2link(self,list):
        cur = dummy = SingleLinkedListNode(list[0])
        for e in list:
            cur.next = SingleLinkedListNode(e)
            cur = cur.next
        return dummy.next

    def print(self, root):
        while root is not None:
            print(root.data)
            root = root.next


list = [1, 2, 3, 4, 5]
p = ConvertListIntoDoublyLinkedList(list)
x = p.getDoubleLinkedList(list)
p.print(x)
