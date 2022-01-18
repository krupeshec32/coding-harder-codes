class MinWindowSubstring:

    def __init__(self, input, subStr):
        self.input = input
        self.subStr = subStr

    def getResult(self, input, subStr):
        require_list = []
        temp = {}
        strTemp = ''
        for i in subStr:
            require_list.append(i)
        for j in input:
            if j in require_list:
                strTemp = strTemp + j
            else:
                print('No')
        return input


input = 'ADOBECODEBANC'
subStr = 'BE'
x = MinWindowSubstring(input, subStr)
print(x.getResult(input, subStr))
