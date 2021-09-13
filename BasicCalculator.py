'''

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5

'''
class BasicCalculator:
    def getCalculation(self,inputStr):
        input_string = inputStr
        result = 0
        counter = -1
        for ch in range(len(input_string)):
            if counter == ch:
                continue
            if input_string[ch] in ['-', '+', '/', '*', '**']:
                next_value = int(input_string[ch+1])
                if input_string[ch] == '-':
                    result -= next_value
                    counter = ch+1
                elif input_string[ch] == '+':
                    result += next_value
                    counter = ch+1
                elif input_string[ch] == '*':
                    result *= next_value
                    counter = ch+1
                elif input_string[ch] == '/':
                    result /= next_value
                    counter = ch+1
                elif input_string[ch] == '**':
                    result **= next_value
                    counter = ch+1
            else:
                result = int(input_string[ch])

        print(result)


x=BasicCalculator()
x.getCalculation('(2+3)')

