'''
Find position of all zeros in the given metrix
 example:
 input: [[1,2,3],[4,0,5],[7,0,9]]
 output is : [(1, 1), (2, 1)]

'''


class FindPositionOfAllZerosInMetrix:

    def __init__(self, metrix):
        self.metrix = metrix

    def findPositionsOfZerosFromMetrix(self, metrix):

        # identify row and col value with 0
        row = len(metrix)
        col = len(metrix[0])
        cnt = 0
        list = []
        for i in range(0, row):
            x = metrix[i][:]
            while x.count(0) >= 1:
                # if list has more than one zeros x.index only give
                # position of 1st zero, so to identify position of
                # next zero we need to reset first 0
                j = x.index(0)
                list.append((i, j))
                x[j] = 1
        print(list)
        return list


p = [[1, 2, 3], [4, 0, 5], [7, 0, 9]]
x = FindPositionOfAllZerosInMetrix(p)
x.findPositionsOfZerosFromMetrix(p)
