'''

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

'''


class FindLongestPalindromicSubstring:

    def __init__(self, inputStr):
        self.inputStr = inputStr

    def getResult(self, inputStr):
        result = {}
        if len(inputStr) == 1:
            # print(inputStr)
            return inputStr
        for i in range(0, len(inputStr)):
            # we need len(inputStr)+1 below because temp[i:j] substring need that
            # to include last character of the string
            for j in range(i+1, len(inputStr)+1):
                tempStr = inputStr[i:j]
                reversedStr = tempStr[::-1]
                if tempStr == reversedStr:
                    result[len(tempStr)] = tempStr
        print(result)
        answer = sorted(result.items(), key=lambda x: x[0], reverse=True)
        # print(answer[0][1])
        return answer[0][1]


inputStr = 'madamkrupeshdadpatel'
x = FindLongestPalindromicSubstring(inputStr)
result = x.getResult(inputStr)
assert x.getResult(inputStr) == 'madam'
