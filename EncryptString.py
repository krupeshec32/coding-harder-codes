"""
input is KKAPWWWXYZ
output should be K2A1P1W3X1Y1Z1
"""


class EncryptString:

    def __init__(self, inputStr):
        self.inputStr = inputStr

    def getEncryptedString(self, inputstr):
        cnt = 1
        out_str = ''
        print(len(inputstr))

        for i in range(0, len(inputstr)):
            if i + 1 == len(inputstr):
                out_str = out_str + str(inputstr[i]) + str(cnt)
            elif inputstr[i] == inputstr[i + 1]:
                cnt = cnt + 1
            else:
                out_str = out_str + str(inputstr[i]) + str(cnt)
                cnt = 1
        print(out_str)


x = EncryptString("KKAPWWWXYZZ")
x.getEncryptedString("KKAPWWWXYZZ")
