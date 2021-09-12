'''
This program is to convert integer into binary
example: 32 ---> 100000
        17 ----> 10001
'''


class ConvertIntegerToBinary:

    def getBinary(self, input):

        if input == 0 or input == 1:
            return input
        result=''
        while input >=1:
            if input % 2 ==0:
                result=result+'0'
                input =input/2
            else:
                result=result+'1'
                input=(input-1)/2
        return result[::-1]

x=ConvertIntegerToBinary()
print(x.getBinary(31))



