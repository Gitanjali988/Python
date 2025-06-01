  
#!/usr/bin/python

"""
Object Oriented Programming and Python Classes
"""

"""
QUESTION 1: 
========================================================================================================
Write a class with name iterator which creates iterator type that iterates from 1 to a given limit. 
For example, if the limit is 10, then it prints  1 2 3 4 5 6 7 8 9 10. 

sample output = [1, 2 ,3 ,4 ,5 , 6, 7, 8, 9, 10] 

Hint: You could have three methods: __init__, __iter__, and _next_.
"""
class iterator:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.i=1
        return self

    def __next__(self):
            i = self.i
            if i > self.limit:
                raise StopIteration()
            self.i += 1
            return i
for i in iterator(10):
                print(i)
    
    
"""
QUESTION 2: 
========================================================================================================
Write a class with name unique_subsets to get all possible unique subsets from a set of distinct integers.
Example:
Input : [1, 2, 3]
output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

===========================
"""

class Unique_Subsets:

    def __init__(self, nums, n):
        self.nums = nums
        self.n = n

    def subsets(self, first = 0, curr = []):
            if len(curr) == k:  
                output.append(curr[:])
                return

            for i in range(first, self.n):
                curr.append(self.nums[i])
                self.subsets(i + 1, curr)
                curr.pop()
        
output = []
inp_list = list(map(int, input("Enter List: ").strip().split()))
inp_len = len(inp_list)
unq_Subsets = Unique_Subsets(inp_list, inp_len)
for k in range(inp_len + 1):
    unq_Subsets.subsets()
print(output)
