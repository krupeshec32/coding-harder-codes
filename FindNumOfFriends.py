'''
Given a two dimensional list, for example [[2,3],[3,4],[5]]
person 2 is friends with 3 etc,
find how many friends each person has. Note, one person has no friends


case:2

You have a 2-D array of friends like
[[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]].
Write a function that creates a dictionary of how many friends each person has.
People can have 0 to many friends. However, there
won't be repeat relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship
'''


class FindNumOfFriends:

    def __init__(self, inputList):
        self.inputList = inputList

    def getResult(self, inputList):
        dictOut={}
        for i in inputList:
            if type(i) == list:
                if(len(i)>1):
                    if ([i[1], i[0]]) in inputList:
                        inputList.remove([i[1], i[0]])
                    for f in i[0]:
                        if f in dictOut.keys():
                            dictOut[f]=dictOut.get(f)+1
                        else:
                            dictOut[f] =1
                else:
                    dictOut[i[0]]=0
        print(dictOut)


list1 = [['A','B'],['B','A'],['A','C'],['B','D'],['B','C'],['R','M'], ['S'],['P']]
x=FindNumOfFriends(list1)
x.getResult(list1)
