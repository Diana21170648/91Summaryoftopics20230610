【Day 61 】2023-08-09 - 416. 分割等和子集 #63
Open
azl397985856 opened this issue 16 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
416. 分割等和子集
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/partition-equal-subset-sum/

前置知识
暂无

题目描述
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

@Diana21170648
Diana21170648 commented now
思路
动态规划

代码
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tar=sum(nums)//2
        if tar+tar !=sum(nums):
            return False
        dp=[False]*(tar+1)
        dp[0]=True
        for i in range(1,len(nums)+1):
            for j in range(tar,0,-1):
                if dp[j] or (j-nums[i-1]>-1 and dp[j-nums[i-1]]):
                    dp[j]=True
        return dp[-1]
复杂度分析

时间复杂度：O(N*N)，其中 N 为数组长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added DFS 动态规划 61 labels 16 hours ago
@GuitarYs
GuitarYs commented 6 hours ago
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(target_sum + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - num]
        return dp[len(nums)][target_sum]
