'''

1) Digits (one of ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

2) Both decimal numbers and integers must contain at least one digit.
A sign ("+" or "-")

(3)
Sign characters are optional for both decimal numbers and integers,
but if one is present, it will always be the first character.
Note, this means that a sign character can also appear immediately after an exponent.
An exponent ("e" or "E")

(4)
Exponents are also optional, but if the string contains one then it must be after a decimal number or an integer.
An integer must follow the exponent.
A dot (".")

A decimal number should only contain one dot. Integers cannot contain dots.
Anything else


'''


class FindValidNumber:

    def __init__(self, input):
        self.input = input

    def checkInput(self, input):
        if input.isdigit():
            return True
        elif input.find('.') >= 0:
            if input.index('.') == 0 and input[1::].isdigit():
                return True
            elif input.count('.') == 1:
                l1 = input.split('.')
                flag = False
                for i in l1:
                    if i.isdigit():
                        flag = True
                    else:
                        return False
                return flag
        elif input.find('+') >= 0 and input.index('+') == 0 and input[1::].isdigit():
            return True
        elif input.find('-') >= 0 and input.index('-') == 0 and input[1::].isdigit():
            return True
        else:
            return False


x = FindValidNumber('1E2')
assert (x.checkInput('1E2'))
