"""
(1)this program find nth highest value from dict i.e. find 2nd highest salary.
(2) if more than one candidate has salary equal to
nth higest salary, then sort the key and print first one
"""


class PythonDictNthHigestValue:
    def __init__(self, inputDict):
        self.inputDict = inputDict

    def getNthvalue(self, inputDict,rank):

        inputDictSortedbyKey=sorted(inputDict.items(),key=lambda x:x[0].lower(),reverse=False)

        # Get values

        valList=list(inputDict.values())
        valListUnique=list(set(valList))
        valListUniqueSorted=sorted(valListUnique,reverse=True)

        # get nth highted

        valRequired=valListUniqueSorted[rank-1]
        print(valRequired)

        for i in inputDictSortedbyKey:
            if i[1] == valRequired:
                return i




inputDict = {"krupesh": 1000,
             "Dhruti": 2000,
             "Sahaj": 3000,
             "Jigar":3000
             }
x = PythonDictNthHigestValue(inputDict)
print(x.getNthvalue(inputDict,1))
