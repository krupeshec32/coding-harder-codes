class FindNonDuplicateNums:
    def __init__(self,inputList):
        self.inputList=inputList

    def getUniqueValues(self,inputList):
        if len(inputList)==0:
            return inputList
        outputList=[]
        for i in inputList:
            if outputList.__contains__(i):
                pass
            else:
                outputList.append(i)
        print(outputList)
        return outputList



inputList=[]
x=FindNonDuplicateNums(inputList)
x.getUniqueValues(inputList)
