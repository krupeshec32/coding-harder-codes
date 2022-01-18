class ListCummulativeSum:

    def __init__(self,list1):
        self.list1=list1

    def getAnswer(self,list1):
        sum=0
        y=sorted(list1)
        minVal=y[0]
        maxVal=y[len(y)-1]
        cnt=0
        for i in range(1,len(y)-1,1):
            if y[i] != minVal and y[i] != maxVal:
                sum=sum+y[i]
                cnt=cnt+1
        print(sum)
        print(sum/cnt)




list1=[1,1,2,2,4,5,10,10]
#expected result 2+2+4+5=13/4=3
# if minVal and maxVal repeate don't count
x=ListCummulativeSum(list1)
x.getAnswer(list1)

