'''
This program is to convert binary into integer
example:

10001---> 17
100000 --->32

'''

class ConvertBinaryIntoInteger:

    def convertBinaryToInt(self,input):

        sum=0
        temp = len(input)-1
        for i in range(0,len(input)):
            if input[i] == '1':
                sum=sum+(2**temp)
                temp=temp-1
            else:
                temp=temp-1
        return sum



x=ConvertBinaryIntoInteger()
print(x.convertBinaryToInt('100000'))


# 1---> 2**(len-1)---> 2*2=4
#2 ---> 2**(len-2)----> 2
#3 ---> 2**(len-3)---->1