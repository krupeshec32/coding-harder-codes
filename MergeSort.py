class MergeSort:

    def merge_sort(self,array):
        ret = []
        if len(array) == 1:
            return array;
        half = len(array) // 2
        lower = self.merge_sort(array[:half])
        upper = self.merge_sort(array[half:])
        lower_len = len(lower)
        upper_len = len(upper)
        i = 0
        j = 0
        while i != lower_len or j != upper_len:
            if i != lower_len and (j == upper_len or lower[i] < upper[j]):
                ret.append(lower[i])
                i += 1
            else:
                ret.append(upper[j])
                j += 1

        return ret

array = [4, 2, 3, 8, 8, 43, 6, 1, 0]
p=MergeSort()
ar=p.merge_sort(array)
print (" ".join(str(x) for x in ar))

