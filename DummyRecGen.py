import random
import pandas as pd


class DummyRecGen:

    def __init__(self):
        self.itemNumbers=[1,2,3,4,5]

    def generateStoreNumber(self):
        store_number = random.randint(1, 1000)
        print(store_number)

    def generateItemNumber(self):
        item_number = random.choice(self.itemNumbers)
        print(item_number)

    def bubble(self,list):
        temp = list[0]
        for i in range(0,len(list)):
            for j in range(i,len(list)):
                if list[i] >= list[j]:
                    list[i],list[j] = list[j],list[i]
        print(list)

    def selection_sort(self,list):
        n=len(list)
        for i in range(n):
            min_index = i
            for j in range(i+1,n):
                if list[j] < list[min_index]:
                    min_index= j
            list[i],list[min_index] = list[min_index],list[i]
        print(list)

test = DummyRecGen()
list=[1,2,10,5,8,5]
test.selection_sort(list)
#test.generateStoreNumber()
#test.generateItemNumber()
