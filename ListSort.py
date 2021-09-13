class ListSort:

    def __init__(self, list):
        self.list = list

    def sortedList(self, list):
        output_list = []
        for i in list:
            print(i)


input_list = [1, 2, 3, 4, 5]
p = ListSort(input_list)
p.sortedList(input_list)
