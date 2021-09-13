from SingleNode import SingleNode


class SumOfTwoLinkedList:

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def getSum(self, l1, l2):

        l1Str=''
        l2Str=''
        startNode=l1
        secondNode=l2
        while startNode is not None:
            l1Str=l1Str+str(startNode.val)
            startNode=startNode.next
        while secondNode is not None:
            l2Str=l2Str+str(secondNode.val)
            secondNode=secondNode.next
        print(int(l1Str)+int(l2Str))


node1 = SingleNode(1)
node2=SingleNode(2)
node3=SingleNode(3)
node1.next=node2
node2.next=node3
node4=SingleNode(4)
node3.next=node4

x=SumOfTwoLinkedList(node1,node2)
x.getSum(node1,node2)




