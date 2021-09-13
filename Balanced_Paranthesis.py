'''

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced


class Balanced_Paranthesis:

    def __init__(self):
'''


class Balanced_Paranthesis:

    def __init__(self, input):
        self.input = input

    def isBalanced(self, input):
        openList = ['[', '{', '(']
        dict = {']':'[', '}':'{', ')':'('}
        list1 = []
        list2 =[]
        for i in input:
            if i in openList:
                print('adding:'+str(i))
                list1.append(i)
            else:
                if i in dict.keys():
                    list2.append(dict[i])
        for i in list2:
            if i in list1:
                list1.remove(i)
            else:
                return False
        if not list1:
            return True
        else:
            return False

'''
edge cases: }}{{
'''

input = '}}{]{['
x = Balanced_Paranthesis(input)
print (x.isBalanced(input))
