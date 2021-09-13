# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
class Fibonachi:

    def __init__(self, num):
        self.num = num

    def getFibo(self, num):
        i = 0
        j = 1
        if (i == 0 and j == 1):
            print(i)
            print(j)
        while True:
            sum = i + j
            print(sum)
            i = j
            j = sum
            while sum >= num:
                return

    def getFiboRecursive(self, i, j, num):

        if i == 0 and j == 1:
            print(i)
            print(j)
        sum = i + j
        print(sum)
        if sum >= num:
            return
        else:
            i = j
            j = sum
            self.getFiboRecursive(i, j, num)


x = Fibonachi(89)
# x.getFibo(89)
x.getFiboRecursive(0, 1, 89)
