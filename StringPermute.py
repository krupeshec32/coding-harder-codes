class StringPermute:

    def __init__(self, inputStr):
        self.inputStr = inputStr

    def permute(self, data, i, length):
        if i == length:
            print(''.join(data))
        else:
            for j in range(i, length):
                # swap
                data[i], data[j] = data[j], data[i]
                self.permute(data, i + 1, length)
                data[i], data[j] = data[j], data[i]


inputStr = "ABC"
w = StringPermute(inputStr)
data = list(inputStr)
w.permute(data, 0, len(inputStr))
