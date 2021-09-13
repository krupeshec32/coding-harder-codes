# put all zeros at the end

inputlist = [1, 2, 0, 5]


def getResult(inputList):
    cnt = 0
    outputList = []
    for i in inputList:
        if i == 0:
            cnt = cnt + 1
        else:
            outputList.append(i)
    while cnt > 0:
        outputList.append(0)
        cnt = cnt - 1
    print(outputList)
    return outputList

getResult(inputlist)
