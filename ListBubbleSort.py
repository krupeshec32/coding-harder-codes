'''

Remember after 1st interation max value go at last
so, for 2nd interation ignore last element for array

After 2nd iteration, 2nd largest value will go to 2nd last at list
so, for 3rd intreation ignore last 2 values

[11, 12, 22, 25, 34, 64, 90]
array length=7

i --> 0 to 7
  j in 0 to (7-i-1):
      0 to 6---> when i =0
      0 to 5--> when i=1
      0 to 4--> when i=2
'''


class ListBubbleSort:

    def __init__(self, list):
        self.list = list

    def bubbleSort(self, arr):
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def bubbleSortRecursive(self,array,n):

        # Base case
        if n == 1:
            return

        # One pass of bubble sort. After
        # this pass, the largest element
        # is moved (or bubbled) to end.
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i +1] = array[i + 1], array[i]

        # Largest element is fixed,
        #  recur for remaining array
        self.bubbleSortRecursive(array,n-1)


arr = [64, 34, 25, 12, 22, 11, 90]
x = ListBubbleSort(arr)
x.bubbleSortRecursive(arr,len(arr))
print(arr)
