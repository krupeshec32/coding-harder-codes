from collections import Counter
from collections import deque


class Blind75:
    class LinkNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def printdemo(self):
        print('demo')

    def get_k_most_element(self, input, k):
        result = {}
        output = []
        for num in input:
            result[num] = input.count(num)
        print(result)
        values = result.values()
        values_list = list(values)
        print(values_list)
        print(type(values_list))
        values_list_sorted = sorted(values_list, reverse=True)
        print(values_list_sorted)
        for key, value in result.items():
            if k > 0:
                print(len(values_list_sorted))
                target_value = values_list_sorted.pop(0)
                if value == target_value:
                    output.append(key)
                    k = k - 1
            else:
                return output

    def get_k_most_using_counter(self, input, k):
        result = []
        input_counter = Counter(input)
        sorted_items = sorted(input_counter.items(), key=lambda x: x[1], reverse=True)
        for num, freq in sorted_items:
            if k > 0:
                print(num)
                result.append(num)
                k = k - 1
            else:
                return result

    def get_combinations(self, input, target):
        result = []
        if len(input) <= 2:
            return result
        for num in input:
            if num > target:
                continue
            else:
                if input.index(target - num) > 0:
                    result.append([input.index(num), input.index(target - num)])
        return result

    def get_combinations_three(self, input, target):
        result = []
        n = len(input)
        input.sort()
        for i in range(0, n):
            for j in range(i + 1, n):
                needed = target - input[i] - input[j]
                lookup_array = set(input[j + 1:])
                if needed in lookup_array:
                    triplet = sorted([input[i], input[j], needed])
                    if triplet not in result:
                        result.append(triplet)
        return result

    def get_combinations_three_new(self, input, target):
        result = []
        n = len(input)
        input.sort()  # Optional: Helps avoid duplicates

        for i in range(n):
            for j in range(i + 1, n):
                needed = target - input[i] - input[j]
                # Use a set to quickly check for the third value
                seen = set(input[j + 1:])  # Only look forward to avoid using same value twice
                if needed in seen:
                    triplet = sorted([input[i], input[j], needed])
                    if triplet not in result:
                        result.append(triplet)
        return result

    def move_zeros(self, nums):
        pos = 0  # position to place the next non-zero element

        for num in nums:
            print('For Loop')
            print(nums)
            if num != 0:
                nums[pos] = num
                pos += 1

        # Fill the rest of the list with zeros
        while pos < len(nums):
            print('While loop')
            print('**************')
            print(nums)
            nums[pos] = 0
            pos += 1

        return nums

    def get_longest_substr(self, input):
        if len(input) == 0:
            return ''
        visited = set()
        substr = ''
        last_output = ''

        for ch in input:  # O(n)
            if ch in visited:
                if len(last_output) < len(substr):
                    last_output = substr
                    # Reset on repeat
                substr = ch
                visited = {ch}
            else:
                substr += ch
                visited.add(ch)

        # Final check after loop
        if len(last_output) < len(substr):
            last_output = substr

        return last_output

    def word_transformation(self, beginningword, endword, wordslist):
        start_step = 1
        dq = deque([(beginningword, start_step)])
        if endword not in wordslist:
            return 0
        while dq:
            startword, step = dq.popleft()
            for i in range(len(startword)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newword = startword[:i] + ch + startword[i + 1:]
                    if newword == endword:
                        return step + 1
                    if newword in wordslist:
                        dq.append((newword, step + 1))
                        wordslist.remove(newword)
        return 0

    '''
        Input: l1 = [2, 4, 3], l2 = [5, 6, 4]  
        Output: [7, 0, 8] 
    '''

    def get_longest_sub(self, input):
        result = []
        dict = {}
        prev = input[0]
        skip = 0

        for i in range(0, len(input)):
            print(result)
            if input[i] >= prev:
                result.append(input[i])
            else:
                if skip > 0:
                    key = len(result)
                    if key in dict:
                        dict[key].append(result)
                        result = []
                        skip = 0
                    prev = input[i]
                else:
                    skip = skip + 1

        sorted_dict = sorted(dict.items(), key=lambda x: x[0], reverse=True)
        print(type(sorted_dict))
        print(sorted_dict)
        return 0

    '''
    Example 1:
    
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    
    Example 2:
    
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
    '''

    def get_max_profit(self, input):
        n = len(input)  # 5
        profit = 0
        for buy_day in range(0, n):  # 0 to 4
            if buy_day == n - 1:
                return profit
            for sell_day in range(buy_day + 1, n):
                profit = max(profit, input[sell_day] - input[buy_day])
        return profit

    '''
    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
    
    Example 2:
    Input: s = "rat", t = "car"
    Output: false
    '''

    def valid_anagram_no_sort(self, s, t):
        s_array = [0] * 26
        t_array = [0] * 26

        for ch in s:  # O(n)
            key = ord(ch) - 97
            s_array[key] = 1
        for ch in t:  # O(n)
            key = ord(ch) - 97
            t_array[key] = 1
        # O(n)+O(n) = O(n)
        if s_array == t_array:
            return True
        else:
            return False

    def max_subarray(self, nums):
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            print(num)
            current_sum = max(num, current_sum + num)  # extend or restart subarray
            max_sum = max(max_sum, current_sum)  # track the best so far
        return max_sum

    def get_product(self, input):
        mul = 1
        result = []
        for num in input:
            mul = mul * num
        for num in input:
            if num == 0:
                result.append(0)
            else:
                result.append(mul // num)
        return result

    def get_combinations_three(self, input, target):
        result = []
        n = len(input)
        input.sort()  # Optional: Helps avoid duplicates

        for i in range(n):
            for j in range(i + 1, n):
                needed = target - input[i] - input[j]
                # Use a set to quickly check for the third value
                seen = set(input[j + 1:])  # Only look forward to avoid using same value twice
                if needed in seen:
                    triplet = sorted([input[i], input[j], needed])
                    if triplet not in result:
                        result.append(triplet)
        return result

    def get_max_product(self, input):
        current = input[0]
        max_num = input[0]
        for num in input[1:]:
            current = max(num, current * num)
            max_num = max(current, max_num)
        return max_num

    def rotLeft(self, a, d):
        if len(a) == d:
            return a
        if d > len(a):
            d = d % len(a)
        if d == 0:
            return a
        while d > 0 and a:  # O(d * n)
            first_char = a[0]  # O(1)
            temp = a[1:]  # O(n)
            temp.append(first_char)  # O(1)
            a = temp  # O(1)
            d = d - 1  # O(1)
        return a

    def add_node(self, linkedlist, data, position):
        count = 0
        current = linkedlist
        new_node = LinkNode(data)
        if position == count:
            new_node.next = current
            return new_node
        while current and count < position - 1:
            current = current.next
            count = count + 1
        new_node.next

    def get_linkedList(self):
        x = Test.LinkNode(0)
        x.next = Test.LinkNode(1)
        x.next.next = Test.LinkNode(2)
        x.next.next.next = Test.LinkNode(3)
        return x

    # 0-->1--> 2 --> 3
    # 0-->1-->3

    def remove_node(self, input, data):
        # if you data is input.val(head)
        while input and input.val == data:
            input = input.next

        current = input
        while current and current.next:
            if current.next.val == data:
                current.next = current.next.next
            else:
                current = current.next
        return input

    def add_node_at_position(self, input, data, position):
        new_node = Test.LinkNode(data)
        while input and position == 0:
            new_node.next = input
            return new_node
        current = input
        cnt = 0
        while current:
            if cnt == position - 1:
                new_node.next = current.next
                current.next = new_node
            current = current.next
        return current

    def print(self, input):
        while input:
            print(input.val)
            input = input.next

    # "4#lint4#code4#love3#you"
    # lint,code,love
    def get_decode_string(self, encode_string):
        start = -1
        result = []
        for i in range(len(encode_string)):
            if encode_string[i].isalpha():
                if start == -1:
                    start = i
                else:
                    continue
            else:
                if start >= 0 and not encode_string[i].isalpha():
                    result.append(encode_string[start:i])
                    start = -1
                else:
                    continue
        return result

    def combinationSum(self, candidates, target):
        result = []

        def dfs(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                # include the same element again (since it can be used unlimited times)
                dfs(i, path + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return result

    '''
        🔁 1. Subsets (Power Set)
    Problem: Given an integer array nums, return all possible subsets (the power set).
    Example:
    Input: [1,2]
    Output: [[], [1], [2], [1,2]]
    '''
    def get_subsets(self,input):
        result =[]
        def backtrack(start,path):
            result.append(path[:])  # <- Here is where we "collect" the subset
            for i in range(start,len(input)):
                path.append(input[i])
                backtrack(i+1,path)  # explore
                path.pop()  # un-choose (backtrack)

        backtrack(0, [])
        return result

    # find longest substring palindrome
    # i.e. input: bmadam, output: madam
    # i.e. input: madamb, output: madam




x = Blind75()
# print(x.get_decode_string('4#lint4#code4#love3#you'))
print(x.get_subsets([2, 3, 6, 7]))
'''
linkedList = x.get_linkedList()
x.print(linkedList)
print('********************')
outputLinkedList = x.remove_node(linkedList, 1)
x.print(outputLinkedList)
'''

# beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
