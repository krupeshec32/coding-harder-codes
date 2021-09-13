"""
Original List: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
extpected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
class FlatternList:

    def __init__(self,inputList):
        self.inputList=inputList

    def getList(self,inputList):
        resultList=[]
        for i in inputList:
            if type(i)==list:
                for x in i:
                    resultList.append(x)
            elif type(i)==set:
                for w in i:
                    resultList.append(w)
            else:
                resultList.append(i)
        print(set(resultList))


list1=[1,2,[3,4],5,{6,7},5]
x=FlatternList(list1)
x.getList(list1)