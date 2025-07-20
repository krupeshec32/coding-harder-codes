from collections import deque

from Test.Node_With_Neighbours import Node_With_Neighbours


class Test:
    def move_zero(self, input):
        last_non_zero_index = 0
        i = 0
        while i < len(input):
            if input[i] != 0:
                input[last_non_zero_index] = input[i]
                last_non_zero_index = last_non_zero_index + 1
            i = i + 1
        while last_non_zero_index < len(input):
            input[last_non_zero_index] = 0
            last_non_zero_index += 1
        return input

    def merge_intervals(self, input):
        merge_list = [input[0]]
        for interval in input[1:]:
            merged_interval = merge_list[-1:]
            print(merged_interval)
            start = merged_interval[0]
            end = merged_interval[1]
            if start < interval[0]:
                end = max(end, interval[1])
        return merge_list

    '''
         Problem Statement
    You are given a total of numCourses courses labeled from 0 to numCourses - 1. You are also given an array prerequisites where prerequisites[i] = [a, b] indicates that to take course a, you must first take course b.
    Return true if you can finish all courses. Otherwise, return false.
    This is a cycle detection problem in a directed graph.
    
    [1] numCourses = 2 and prerequisites = [[1, 0]]  Output: True 
    [2] numCourses = 2 and prerequisites = [[1, 0], [0, 1]] Output: False 

    
    '''

    def canFinish(numCourses, prerequisites):
        from collections import defaultdict

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(course):
            if visited[course] == 1:
                return False  # cycle detected
            if visited[course] == 2:
                return True  # already checked and no cycle

            visited[course] = 1  # mark as visiting

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 2  # mark as visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    '''
        beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    ✅ Expected Output:
    5 because "hit" → "hot" → "dot" → "dog" → "cog"
    '''

    def wordLadder(self,beginWord,endword,wordList):
        word_set = set(wordList)
        if endword not in word_set:
            return 0
        queue = deque()
        queue.append((beginWord,1))
        while queue:
            word,start = queue.popleft()
            if word == endword:
                return start
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i]+c+word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word,start+1))
        return 0

    '''
     🧩 Problem Statement (Leetcode 739)
    Given a list of daily temperatures temperatures, return a list answer such that:
    answer[i] is the number of days you have to wait after the i-th day to get a warmer temperature.
    If there's no future day for which this is possible, set answer[i] = 0.
    
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    ✅ Output:[1, 1, 4, 2, 1, 1, 0, 0]
    
    temperatures = [30, 40, 50, 60]
    ✅ Output:[1, 1, 1, 0]
    '''

    '''
    target = 12
    position = [10, 8, 0, 5, 3]
    speed =    [2, 4, 1, 1, 3]
    
    Output : 3
    '''
    def carFleet(self,target, position, speed):
        # Pair up cars with their time to reach the target
        cars = sorted(zip(position, speed), reverse=True)  # Sort by position descending
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            # Only add to stack if it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

    '''
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    ✅ Output:[1, 1, 4, 2, 1, 1, 0, 0]
    
    temperatures = [30, 40, 50, 60]
    output :[1, 1, 1, 0]
    
    '''

    def dailyTemperatures(temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices
        for i in range(n):
            # Check for a warmer temperature than what’s on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer
x = Test()
print(x.wordLadder("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))


'''
node1 = Node_With_Neighbours(1, [])
node2 = Node_With_Neighbours(2, [])
node3 = Node_With_Neighbours(3, [])
node4 = Node_With_Neighbours(4, [])

node1.neighbours = [node2, node4]
node2.neighbours = [node1, node3]
node3.neighbours = [node2, node4]
node4.neighbours = [node1, node3]
#print(x.transverse(node1))
'''
