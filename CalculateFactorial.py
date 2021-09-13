class CalculateFactorial:
    def __init__(self,num):
        self.num=num

    def getFactorial(self,num):
        x=1
        for i in range(1,num+1):
            x=x*i
        return x

    def getFactorialRecursive(self,num):
        if (num==1):
            return num
        else:
            return num*self.getFactorialRecursive(num-1)

p=CalculateFactorial(5)
#print(p.getFactorial(5))
print(p.getFactorialRecursive(5))