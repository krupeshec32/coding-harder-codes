'''
Find out pair that reach target by doing sum
example: Target:2 and input is [1,1,3,1]
anser should be 1,1 becuase 1+1 =2
'''
class FindSumCombination:

    def __init__(self, inputList):
        self.inputList = inputList

    def getResult(self, inputList, target):

        for i in range(0, len(inputList)):
            for j in range(0, len(inputList)):
                if j >= target:
                    pass
                if inputList[i] + inputList[j] == target:
                    print(str(i) + " " + str(j))
                    return i, j


list1 = [2, 1, 1, 1]
target = 2
x = FindSumCombination(list1)
x.getResult(list1, target)
