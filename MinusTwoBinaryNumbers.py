class MinusTwoBinaryNumbers:

    def minusBinaryNumbers(self,s1,s2):
        maxlen = max(len(s1), len(s2))

        s1 = s1.zfill(maxlen)
        s2 = s2.zfill(maxlen)

        result = ''
        carry = 0

        i = maxlen - 1
        while (i >= 0):
            s = int(s1[i]) - int(s2[i])
            if s <= 0:
                if carry == 0 and s != 0:
                    carry = 1
                    result = result + "1"
                else:
                    result = result + "0"
            else:
                if carry == 1:
                    result = result + "0"
                    carry = 0
                else:
                    result = result + "1"
            i = i - 1

        if carry > 0:
            result = result + "1"

        return result[::-1]

x=MinusTwoBinaryNumbers()
print(x.minusBinaryNumbers('100000','10000'))