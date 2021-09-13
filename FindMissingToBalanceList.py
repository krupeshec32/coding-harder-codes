'''
Given a list of ints, balance the list so that each int appears equally in the list.
Return a dictionary where the key is the int and the value is the count needed to balance the list.

[1, 1, 2] => {2: 1}--> 1 appreas 2 times and 2 appear 1 times. To make 2 appear two time, we need one more 2
[1, 1, 1, 5, 3, 2, 2] => {5: 2, 3: 2, 2: 1}

'''

class FindMissingToBalanceList:

    def __init__(self,inputList):
        self.inputList=inputList

    def getResult(self,inputList):
        output={}
        for i in inputList:
            if i in output:
                getVal= output[i]
                output[i]=getVal+1
            else:
                output[i]=1
        #sorted output

        sortedOut=sorted(output.items(),key=lambda x:x[1],reverse=True)
        maxVal=int(sortedOut[0][1])
        result={}

        for i in range(0,len(sortedOut)):
            if sortedOut[i][1] !=maxVal:
                result[sortedOut[i][0]]=maxVal-sortedOut[i][1]
        print(result)


list1=[1, 1, 1, 5, 3, 2, 2]
x=FindMissingToBalanceList(list1)
x.getResult(list1)
