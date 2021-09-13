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

x=[2, 3, 6, 5]
p=CreateHistogram(x)
p.histogram(x)