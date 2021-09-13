'''
Word List:
[cat, bat, rat, drat, dart, drab]

Queries:

cat -> true
c.t -> true
.at -> true
..t -> true
d..t -> true
dr.. -> true
... -> true
.... -> true

..... -> false
h.t -> false
c. -> false
*/
'''


class SimpleWordCheck:

    def __init__(self, inputStr):
        self.inputStr = inputStr

    def spellCheck(self,word, list):

        if word is None:
            return True
        if word.lower() in [x.lower() for x in list]:
            return True
        if len(word) not in [len(x) for x in list]:
            return False
        else:

            for i in list:
                cnt = 0
                if len(i) == len(word):
                    for j in range(0, len(word)):
                        if i.lower()[j] == word.lower()[j] or word[j] == '.':
                            cnt = cnt + 1
                            print('cnt sum :' + str(cnt))
                        else:
                            cnt = 0
                    print('cnt is :'+str(cnt))
                    if cnt == len(word):
                        print('here')
                        return True
            if cnt <= len(word):
                print('coming here')
                return False




inputStr='d.ap'
arrayList=['cat', 'bat', 'rat', 'drat', 'dart', 'drab']
x=SimpleWordCheck(inputStr)
print(x.spellCheck(inputStr,arrayList))

