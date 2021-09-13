class permuteStr1:

    def __init__(self,inputStr):
        self.inputStr=inputStr

    def permut(self,data,i,length):

        if i==length:
            print("".join(data))
        else:
            for j in range(i,length):
                data[i],data[j]=data[j],data[i]
                self.permut(data,i+1,length)
                data[i],data[j]=data[j],data[i]
inputStr='abc'
x=permuteStr1(inputStr)
x.permut(list(inputStr),0,len(inputStr))