"""
histogram([2, 3, 6, 5])
Sample Output:

**
***
******
*****

"""
class CreateHistogram:

    def __init__(self,items):
        self.items=items


    def histogram(self,items):
        for n in items:
            output = ''
            times = n
            while( times > 0 ):
              output += '*'
              times = times - 1
            print(output)
            
    def revprintPattern(list1):
    
    output=''
    maxVal=max(list1)
    for i in list1:
        diff=maxVal-i
        while (diff > 0):
            output=output+' '
            diff=diff-1
        while (i > 0):
            output=output+'*'
            i=i-1
        print(output)
        output=''

x=[2, 3, 6, 5]
p=CreateHistogram(x)
p.histogram(x)
