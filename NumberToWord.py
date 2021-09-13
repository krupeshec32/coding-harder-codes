'''
print input number 0-99 in word

example 9--Nine
99- Nighty Nine

'''


class NumberToWord:

    def __init__(self, inputNum):
        self.inputNum = inputNum
        self.lookupdict = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six'
        }
        self.lookupdict_tens = {
            2: 'Twenty',
            3: 'Thirty'
        }

    def getNumInWord(self, inputNum):
        if inputNum <= 20:
            return self.lookupdict[inputNum]
        if 20 < inputNum < 100:
            # 21
            rem = int(inputNum % 10)
            div = int(inputNum / 10)
            return str(self.lookupdict_tens[div])+' ' + str(self.lookupdict[rem])
        return inputNum


p = 34
x = NumberToWord(24)
print(x.getNumInWord(p))
