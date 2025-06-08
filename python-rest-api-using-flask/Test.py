class Test:
    def move_zero(self,input):
        last_non_zero_index = 0
        i = 0
        while i < len(input):
            if input[i] != 0:
                input[last_non_zero_index] = input[i]
                last_non_zero_index = last_non_zero_index+1
            i=i+1
        while last_non_zero_index < len(input):
            input[last_non_zero_index] = 0
            last_non_zero_index += 1
        return input

    def merge_intervals(self,input):
        merge_list = [input[0]]
        for interval in input[1:]:
            merged_interval= merge_list[-1:]
            print(merged_interval)
            start = merged_interval[0]
            end = merged_interval[1]
            if start < interval[0]:
                end = max(end, interval[1])
        return merge_list


x = Test()
print(x.merge_intervals([[1,5],[2,4],[3,8]]))
