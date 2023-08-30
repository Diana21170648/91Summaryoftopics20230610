leetcode-pp
/
91alg-11-daily-check

Type / to search

Code
Issues
82
Pull requests
Discussions
Actions
Projects
Security
Insights
【Day 82 】2023-08-30 - 47 全排列 II #84
Open
azl397985856 opened this issue 19 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 19 hours ago
47 全排列 II
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/permutations-ii/

前置知识
回溯
数组
剪枝
题目描述
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
[1,1,2],
[1,2,1],
[2,1,1]
@azl397985856 azl397985856 added 剪枝 回溯 82 labels 19 hours ago
@GuitarYs
GuitarYs commented 8 hours ago
class Permutations:
    def __init__(self):
        self.result = []
        
    def permuteUnique(self, nums):
        if not nums:
            return []
        
        used = [False] * len(nums)
        current_permutation = []
        self.backtrack(sorted(nums), used, current_permutation)
        
        return self.result
    
    def backtrack(self, nums, used, current_permutation):
        if len(current_permutation) == len(nums):
            self.result.append(list(current_permutation))
            return
        
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
                
            used[i] = True
            current_permutation.append(nums[i])
            self.backtrack(nums, used, current_permutation)
            used[i] = False
            current_permutation.pop()
@Diana21170648
Diana21170648 commented 8 hours ago
思路
回溯剪枝，去掉重复解看先处理左边，再处理右边

代码
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,pre):
            nonlocal res
            if len(nums)<=1:
                res.append(pre+nums)
                return
            for key,value in enumerate(nums):
                if value not in nums[:key]:
                    backtrack(nums[:key]+nums[key+1:],pre+[value])
        res=[]
        if not len(nums):
            return []
        backtrack(nums,[])
        return res
复杂度分析

时间复杂度：O(N!*op(res))，其中 N 为数组长度。
空间复杂度：O(N*N!)
