class MetrixMoveUpLeft:

    def __init__(self, input):
        self.input = input

    def getPaths(self, input, i, j, paths):

        row = len(input)
        col = len(input[0])

        if i == 0 and j == 0:
            paths.append(input[i][j])
            print(paths)
            paths.pop()
            return
        paths.append(input[i][j])

        if (i >= 0) and (i <= row - 1) and (j - 1 >= 0) and (j - 1 <= col - 1):
            self.getPaths(input, i, j - 1, paths)
        if (i - 1 >= 0) and (i - 1 <= row - 1) and (j >= 0) and (j <= col - 1):
            self.getPaths(input, i - 1, j, paths)
        paths.pop()


input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = MetrixMoveUpLeft(input)
paths = []
i = 2
j = 2
a.getPaths(input, i, j, paths)
