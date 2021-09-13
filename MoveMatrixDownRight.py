class MoveMatrixDownRight:
    def __init__(self, input):
        self.input = input

    def getPaths(self, input, i, j, paths):
        row = len(input)
        col = len(input[0])

        if (i == row - 1) and (j == col - 1):
            paths.append(input[i][j])
            print(paths)
            paths.pop()
            return
        paths.append(input[i][j])

        if ((i >= 0) and (i <= row - 1) and (j + 1 > 0) and (j + 1 <= col - 1)):
            self.getPaths(input, i, j + 1, paths)
        if ((i + 1 > 0) and (i + 1 <= row - 1) and (j >= 0) and (j <= col - 1)):
            self.getPaths(input, i + 1, j, paths)
        paths.pop()

    def moveOnlyDiagonally(self, input, i, j, paths):

        row = len(input)
        col = len(input[0])

        if (i == row - 1 and j == col - 1):
            paths.append(input[i][j])
            print(paths)
            paths.pop()
            return
        paths.append(input[i][j])
        if (i + 1 <= row - 1 and j + 1 <= col - 1):
            self.moveOnlyDiagonally(input, i + 1, j + 1, paths)
        paths.pop()


    def moveDiagonallydownright(self,metrix, i, j, paths):
        row = len(metrix)
        col = len(metrix[0])

        if (i == row - 1 and j == col - 1):
            paths.append(metrix[i][j])
            print(paths)
            paths.pop()
            return
        paths.append(metrix[i][j])

        if (i + 1 >= 0 and i + 1 <= row - 1 and j + 1 >= 0 and j + 1 <= col - 1):
            self.getPaths(metrix, i + 1, j + 1, paths)
        paths.pop()

input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = MoveMatrixDownRight(input)
paths = []
i = 0
j = 0
a.getPaths(input, i, j, paths)
print('move only diagonally')
a.moveOnlyDiagonally(input, i, j, paths)
print('move diagonally+left+right')
a.moveDiagonallydownright(input,i,j,paths)