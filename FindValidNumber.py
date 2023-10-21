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
    def isNumber(self, s: str) -> bool:
        seenDigit = seenExpo = seenSign = seenDot = False
        for i in range(len(s)):
            if s[i].isdigit():
                seenDigit = True
            elif s[i] in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif s[i] in ["e", "E"]:
                if seenExpo or not seenDigit:
                    return False
                seenExpo = True
                seenDigit = False
            elif s[i] == ".":
                if seenSign or seenExpo:
                    return False
                seenDot = True
            else:
                return False
        return seenDigit


x = FindValidNumber('1E2')
assert (x.checkInput('1E2'))
