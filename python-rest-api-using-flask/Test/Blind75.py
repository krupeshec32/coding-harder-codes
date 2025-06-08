from collections import Counter
from collections import deque
from collections import defaultdict


class LinkNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Blind75:
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
        x = Blind75.LinkNode(0)
        x.next = Blind75.LinkNode(1)
        x.next.next = Blind75.LinkNode(2)
        x.next.next.next = Blind75.LinkNode(3)
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
        new_node = Blind75.LinkNode(data)
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

    def get_subsets(self, input):
        result = []

        def backtrack(start, path):
            result.append(path[:])  # <- Here is where we "collect" the subset
            for i in range(start, len(input)):
                path.append(input[i])
                backtrack(i + 1, path)  # explore
                path.pop()  # un-choose (backtrack)

        backtrack(0, [])
        return result

    # find longest substring palindrome
    # i.e. input: bmadam, output: madam
    # i.e. input: madamb, output: madam

    '''
    Rotate matrix 
    Input : matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]] 
    '''

    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):  # this will convert row columns into row
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
            # OR
            '''
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
            '''
        return matrix

    '''

    Problem 21: Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

    Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

    Example 1:

    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
    Example 2:

    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
    Example 3:

    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
    '''

    def erase_overlap_interval(self, input):
        input.sort(key=lambda x: x[1])
        count = 0
        prev_end = float('-inf')
        for start, end in input:
            if start >= prev_end:
                prev_end = end
            else:
                count = count + 1
        return count

    '''
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    Example 1:
    
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]..give me python code
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    Example 2:
    
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.
    '''

    def max_subarray_sum(nums):
        max_current = max_global = nums[0]

        for num in nums[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)

        return max_global

    '''
    Spiral Matrix
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
    
    '''

    def spiralOrder(matrix):
        result = []
        if not matrix:
            return result

        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while top < bottom and left < right:
            # Traverse top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            # Traverse right column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            # Traverse bottom row
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom - 1][i])
                bottom -= 1
            # Traverse left column
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result

    '''
    55. Jump Game
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    Example 1:
    
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    Example 2:
    
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    '''

    def canJump(self, nums):
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
        return True

    '''
    
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
    
    Example 1:
    
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    '''

    def merge_intervals(self, intervals):
        if not intervals:
            return []
        # Sort intervals based on the starting value
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            # Check for overlap
            if current[0] <= last[1]:
                # Merge intervals
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged

    '''
    57. Insert Interval
    You are given an array of non-overlapping intervals intervals where 
    intervals[i] = [starti, endi] represent the start and the end of the ith interval 
    and intervals is sorted in ascending order by starti. You are also given an interval 
    newInterval = [start, end] that represents the start and end of another interval.
    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
    Return intervals after the insertion.
    Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
    '''

    def insert_and_merge_intervals(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        # Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        return result

    '''
    Find interval intersaction
    interval1 = [[0,2],[5,10]]
    interval2 = [[1,5],[8,12]]
    output = [[1,2],[5,5],[8,10]]
    '''

    def get_intervals_intersaction(self,interval1,interval2):
        result = []
        i,j = 0,0
        while i < len(interval1) and j < len(interval2):
            start = max(interval1[i][0],interval2[j][0])
            end = min(interval1[i][1],interval2[j][1])

            if start <= end:
                result.append([start,end])
            # move pointer that has the smaller end

            if interval1[i][1] < interval2[j][1]:
                i +=1
            else:
                j +=1
        return result
    '''
     
    
    '''


    '''
    Problem: https://leetcode.com/problems/subtree-of-another-tree/description/?envType=problem-list-v2&envId=oizxjoit
    572. Subtree of Another Tree
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with 
    the same structure and node values of subRoot and false otherwise.A subtree of a binary tree tree is a
    tree that consists of a node in tree and all of this node's descendants. 
    The tree tree could also be considered as a subtree of itself.
    '''

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    '''
    Problem : Unique paths. 
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
    
    Example : Input: m = 3, n = 7
    Output: 28
    
    '''

    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D grid initialized with 1s
        dp = [[1] * n for _ in range(m)]

        # Fill the grid using the relation:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    '''
    Reverse bits of a given 32 bits unsigned integer.
    Example 1:
    
    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
    so return 964176192 which its binary representation is 00111001011110000010100101000000.
    '''

    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

    def int_to_binary(self, num):
        binary = ""
        while num > 0:
            bit = num % 2
            binary = str(bit) + binary
            num = num // 2
        return binary

    '''
    Example : find the next greater element. 
    Example: input=[1,4,6,3,2,7]--> output : [4,6,7,7,7,-1].give me python code
    '''

    def next_greater_elements(self, nums):
        result = [-1] * len(nums)
        stack = []

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[i]
            stack.append(i)  # hint we are saving index

        return result

    '''
      window sizing
    '''

    def sliding_window_example(nums):
        window_size = 3
        for i in range(len(nums) - window_size + 1):
            window = nums[i:i + window_size]
            print(f"Window {i + 1}: {window}")

    def sliding_window_sum(self, input):
        window_size = 3
        result = []
        for i in range(0, len(input) - window_size + 1):
            result.append(sum(input[i:i + window_size]))
        return result

    def longest_nonrepeat(self, input):
        start = 0
        dict = defaultdict(int)
        visited = []

        for end in range(1, len(input)):
            substr = input[start:end]

    '''
    Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].
    '''

    def merge_sorted_array(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        result = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < m:
            result.append(nums1[i])
            i += 1
        while j < n:
            result.append(nums2[j])
            j += 1
        return result

    def myPow(self, x: float, n: int) -> float:
        result = 1
        for i in range(abs(n)):
            result = result * abs(x)
        if n > 0:
            return result
        else:
            return 1 / result

    '''
        Simplify Path.Example 1:
    Input: path = "/home/"
    Output: "/home"
    
    Explanation:
    The trailing slash should be removed.
    Example 2:
    Input: path = "/home//foo/"
    Output: "/home/foo"
    Explanation:
    Multiple consecutive slashes are replaced by a single one.
    Example 3:
    Input: path = "/home/user/Documents/../Pictures"
    '''

    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                continue  # skip empty and current directory
            elif part == '..':
                if stack:
                    stack.pop()  # go up one directory
            else:
                stack.append(part)  # valid folder name

        return '/' + '/'.join(stack)

    def max_sum_subarray(self, input):
        current_sum = input[0]
        max_sum = input[0]
        for num in input[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        return max_sum

    '''
    # aeexyz,k=2---> answer aee
    # abcd,k=2---> none
    # aeedfge--> edfge
    '''

    def get_repeated_chars_string(self, input, k):
        right = 0
        left = 0
        dict = {}
        result = ''
        while right < len(input):
            print(right)
            print(left)
            dict[input[right]] = dict.get(input[right], 0) + 1
            if max(dict.values()) == k:
                if len(input[left:right+ 1]) > len(result):
                    result = input[left:right+ 1]
                    left = right
                    dict={}
                    dict[input[right]] = 1
            right = right + 1
        return result

    def get_non_repeated_substring(self,input):
        right = 0
        left = 0
        visited = []
        result = ''

        while right < len(input):
            if input[right] in visited:
                if len(result) < len(input[left:right]):
                    result = input[left:right]
                    visited = [input[right]]
                    left = right
            else:
                visited.append(input[right])
            right = right +1
        if visited:
            if len(result) > len(visited):
                return result
            else:
                return ''.join(visited)




x = Blind75()
# print(x.sliding_window_sum([1, 2, 3, 4, 5, 6]))
# print(x.simplifyPath("/home/test"))
# print(x.max_sum_subarray([1, 2, 3, -8, 10]))
print(x.get_non_repeated_substring('abcaefghi'))

'''
# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(x.spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]
# Example usage:
print(x.max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(x.max_subarray_sum([1]))                     # Output: 1
# print(x.get_decode_string('4#lint4#code4#love3#you'))
# print(x.get_subsets([2, 3, 6, 7]))
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(x.rotate(matrix))
print(x.erase_overlap_interval([[1,2],[3,4],[2,5],[8,9]]))
# Examples
print(x.canJump([2, 3, 1, 1, 4]))  # Output: True
print(x.canJump([3, 2, 1, 0, 4]))  # Output: False
print(x.merge_intervals([[1, 2], [3, 6], [8, 10], [15, 18]]))
linkedList = x.get_linkedList()
x.print(linkedList)
print('********************')
outputLinkedList = x.remove_node(linkedList, 1)
x.print(outputLinkedList)
print(x.merge_new_interval([[1,3],[6,9]],[10,15]))
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(x.insert_and_merge_intervals(intervals, newInterval))
'''

# beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
