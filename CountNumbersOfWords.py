class CountNumbersOfWords:
    def __init__(self, sentence):
        self.sentence = sentence

    def getCnt(self, sentence):
        words = sentence.split()
        print(words)

sentence = "I am Sahaj,Sahaj is good"
x=CountNumbersOfWords(sentence)
x.getCnt(sentence)

