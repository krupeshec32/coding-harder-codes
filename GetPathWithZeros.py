class GetPathWithZeros:

    def getPaths(self,metrix, i, j, paths):
        row = len(metrix)
        col = len(metrix[0])
        flag=False
        if i == row - 1 and j == col - 1:
            paths.append(metrix[i][j])
            if len(paths) == paths.count(0):
                flag=True
            paths.pop()
            return
        paths.append(metrix[i][j])
        '''
        if i <= row - 1 and j + 1 <= col - 1:
            self.getPaths(metrix, i, j + 1, paths)
        if i + 1 <= row - 1 and j <= col - 1:
            self.getPaths(metrix, i + 1, j, paths)
        '''
        if i + 1 <= row - 1 and j + 1 <= col - 1:
            if flag:
                return flag
            else:
                self.getPaths(metrix, i + 1, j + 1, paths)
        paths.pop()
        return

metrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
x=GetPathWithZeros()
assert(x.getPaths(metrix, 0, 0, []))