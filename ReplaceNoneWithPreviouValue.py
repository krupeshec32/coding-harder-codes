class ReplaceNoneWithPreviousValue:

    def __init__(self,list):
        self.list=list

    def getList(self,inputList):
        if (inputList==[]):
            print(inputList)
            return inputList
        resultList=[]
        p=None
        for i in inputList:
            if i is not None:
                p=i
                resultList.append(i)
            else:
                resultList.append(p)
        print(resultList)


list=[1,None,'5','6']
# expected output [1,2,2,4,4,5]
x=ReplaceNoneWithPreviousValue(list)
x.getList(list)
