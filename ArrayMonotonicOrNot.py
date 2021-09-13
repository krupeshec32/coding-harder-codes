'''

Given an array of integers, we would like to determine whether the array
is monotonic (non-decreasing/non-increasing) or not. Examples:
 // 1 2 5 5 8
// true
// 9 4 4 2 2
// true
// 1 4 6 3
// false
//1 1 1 1 1 1
// true

'''


class ArrayMonotonicOrNot:

    def __init__(self, inputArray):
        self.inputArray = inputArray

    def getResult(self, inputArray):
        if len(inputArray)==1:
            return True
        for i in range(1,len(inputArray)):
            if(inputArray[i-1] > inputArray[i]):
                return (self.checkMonotonic(inputArray,'decrease'))
            elif(inputArray[i-1] < inputArray[i]):
                return (self.checkMonotonic(inputArray, 'increase'))
            else:
                pass
        return True

    def checkMonotonic(self,inputArray,flag):
        if flag == 'decrease':
            for i in range(1,len(inputArray)):
                if inputArray[i - 1] < inputArray[i]:
                    return False
            return True
        else:
            for i in range(1, len(inputArray)):
                if inputArray[i - 1] > inputArray[i]:
                    return False
            return True

list1 = [3,1,1,1]
x=ArrayMonotonicOrNot(list1)
print(x.getResult(list1))
