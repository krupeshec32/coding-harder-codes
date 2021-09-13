class FindGCPAndLCP:

    def __init__(self,inputList):
        self.inputList=inputList

    def find_gcp(self,num1,num2):
        while(num2):
            num1,num2=num2,num1%num2
        return num1

    def find_lcm(self,x, y):
        if x > y:
            greater = x
        else:
            greater = y
        while (True):
            if (greater % x == 0) and (greater % y == 0):
                lcm = greater
                break
            greater += 1
            print('val of greater:'+str(greater))
        return lcm

    def findGCP(self,inputList):
        num1=inputList[0]
        num2=inputList[1]
        gcp1=self.find_gcp(num1,num2)
        for i in range(2,len(inputList)):
            gcp1=self.find_gcp(gcp1,inputList[i])
        return gcp1

    def findLCP(self,inputList):
        num1=inputList[0]
        num2=inputList[1]
        lcp1=self.find_lcm(num1,num2)
        for i in range(2,len(inputList)):
            lcp1=self.find_lcm(lcp1,inputList[i])
        return lcp1

input1=[18,3]
x=FindGCPAndLCP(input1)
print('GCP:'+ str(x.findGCP(input1)))
print('LCP:'+ str(x.findLCP(input1)))