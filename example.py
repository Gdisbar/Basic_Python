
#78. Subsets: Runtime: 16 ms, faster than 96.05%

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path + [nums[i]], res)     

#90. Subsets II: Runtime: 20 ms, faster than 96.23%

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path + [nums[i]], res)

#77. Combinations: Runtime: 676 ms, faster than 42.96%

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(range(1, n+1), k, [], res)
        return res
    
    def dfs(self, nums, k, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+ [nums[i]], res)

#39. Combination Sum: Runtime: 124 ms, faster than 30.77%

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, candidates, target, path, res):
        if target < 0:
            return   #backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], path + [candidates[i]], res)  

#40. Combination Sum II: Runtime: 36 ms, faster than 91.77%

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, candidates, target, path, res):
        if target < 0:
            return
        
        if target == 0:
            res.append(path)
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
                
            if candidates[i]> target:
                break
                
            self.dfs(candidates[i+1:], target - candidates[i], path + [candidates[i]], res)

#46. Permutations: Runtime: 28 ms, faster than 79.64%

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)   

#47. Permutations II: Runtime: 40 ms, faster than 92.96%

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

#17. Letter combination of a Phone Number::Runtime: 24 ms, faster than 43.40%

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    
    def dfs(self, nums, index, dic, path, res):
        if index >=len(nums):
            res.append(path)
            return
        string1 =dic[nums[index]]
        for i in string1:
            self.dfs(nums, index+1, dic, path + i, res)


79. Word Search
===================
# Given an m x n grid of characters board and a string word, return true if 
# word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

 

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
# word = "ABCCED"
# Output: true

# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
# word = "SEE"
# Output: true

# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
# word = "ABCB"
# Output: false



def exist(self, g: List[List[str]], word: str) -> bool:
    R, C = len(g), len(g[0])

    def spread(i, j, w):
        if not w:
            return True
        original, g[i][j] = g[i][j], '-'
        spreaded = False
        for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if (0<=x<R and 0<=y<C and w[0]==g[x][y]
                    and spread(x, y, w[1:])):
                spreaded = True
                break
        g[i][j] = original
        return spreaded

    for i in range(R):
        for j in range(C):
            if g[i][j] == word[0] and spread(i, j, word[1:]):
                return True
    return False

import re,os,time
from itertools import islice
import pandas as pd 

r_n = 11  ## number of records 
n_t = 10  ## number of times we want to generate the data
n = r_n*n_t + r_n  ## 110 is the last line with data(just previous to the cursor)

cmd1 = 'cat /proc/cpuinfo | grep "cache size" | uniq  >> op.txt'
cmd2 = 'cat /proc/cpuinfo | grep "cpu MHz" | uniq >> op.txt'
cmd3 = 'cat /proc/meminfo | grep "Buffers" |uniq >> op.txt'
cmd4 = 'cat /proc/meminfo | grep "Cached" |uniq >> op.txt'
cmd5 = 'cat /proc/meminfo | grep "SwapFree" |uniq >> op.txt'
cmd6 = 'cat /proc/meminfo | grep "MemFree" |uniq >> op.txt'
cmd7 = 'cat /proc/meminfo | grep "Dirty" |uniq >> op.txt'

for i in range(n_t):
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
    os.system(cmd4)
    os.system(cmd5)
    os.system(cmd6)
    os.system(cmd7)
    time.sleep(1)

print("Raw data saved into op.txt")
with open('op.txt') as f:
    lis = []
    for i in range(n):
        text = f.readline()
        x = re.sub("[a-zA-Z:\t\n]","",text)
        lis.append(str(x).strip())

#print(lis)

lis2 = []
for _ in range(r_n):
    lis2.append(r_n)

def lis_convert(lis, lis2): 
    it = iter(lis) 
    return [list(islice(it, i)) for i in lis2] 

lis3 = lis_convert(lis, lis2)

#print(lis3)

df = pd.DataFrame(lis3, columns =['cache size','cpu(core 1) MHz','cpu(core 2) MHz','cpu(core 3) MHz','cpu(core 4) MHz',
    'Buffers','Cached','SwapCached','SwapFree','MemFree','Dirty'], dtype = float) 

#print(df) 

df.to_csv('op.csv')
print("Formatted data saved into op.csv")
#df = pd.read_csv('op.csv',index_col=0)