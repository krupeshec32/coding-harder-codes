'''
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''


class SumOfTwoBinaryNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getSum(self,a,b):
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Initialize the result
        result = ''

        # Initialize the carry
        carry = 0

        # Traverse the string
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result

            # Compute the carry.
            carry = 0 if r < 2 else 1

        if carry != 0:
            result = '1' + result

        print(result.zfill(max_len))

p=SumOfTwoBinaryNumbers('11','1')
p.getSum('11','1')