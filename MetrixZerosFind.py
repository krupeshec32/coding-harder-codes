'''
Given an m x n integer matrix matrix, if an element is 0,
set its entire row and column to 0's, and return the matrix.

example:
convert [[1, 1,1], [1, 0,1], [1, 1,1]]
into   [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
'''


class MetrixZerosFind:

    def __init__(self, inputMat):
        self.inputMat = inputMat

    def getResult(self, inputMat):
        row = len(inputMat)
        col = len(inputMat[0])
        x = []
        for i in range(0, row):
            for j in range(0, col):
                if inputMat[i][j] == 0:
                    x.append((i, j))
        print(x)
        self.makeZeros(inputMat, x)

    def makeZeros(self, inputMat, x):
        for i in x:
            rowNum = i[0]
            colNum = i[1]
        for y in range(0, len(inputMat)):
            inputMat[y][colNum] = 0
        for y in range(0, len(inputMat[0])):
            inputMat[rowNum][y] = 0
        print(inputMat)


inputMat = [[1, 1,1], [1, 0,1], [1, 1,1]]
x = MetrixZerosFind(inputMat)
x.getResult(inputMat)
