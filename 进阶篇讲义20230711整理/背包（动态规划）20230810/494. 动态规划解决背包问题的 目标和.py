【Day 62 】2023-08-10 - 494. 目标和 #64
Open
azl397985856 opened this issue 20 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 20 hours ago
494. 目标和
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/target-sum/

前置知识
背包
数学
题目描述
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，target。现在你有两个符号  +  和  -。对于数组中的任意一个整数，你都可以从  +  或  -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 target 的所有添加符号的方法数。

示例：

输入：nums: [1, 1, 1, 1, 1], target: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
动态规划解决背包问题

代码
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        t=sum(nums)+abs(target)
        if t%2:
            return 0
        t=t//2#背包的大小
        dp=[0]*(t+1)
        dp[0]=1
        for i in range(len(nums)):
            for j in range(t,nums[i]-1,-1):
                #if j - nums[i] >= 0:
                dp[j]+=dp[j-nums[i]]
        return dp[-1]
复杂度分析

时间复杂度：T=O(fushu*(sum(nums)+target))/2
空间复杂度：S=O(sum(nums)+target)/2

@azl397985856 azl397985856 added the 62 label 20 hours ago
@freesan44
freesan44 commented 12 hours ago
class Solution {
    func findTargetSumWays(_ nums: [Int], _ target: Int) -> Int {
        let totalSum = nums.reduce(0, +)
        let desiredSum = totalSum + target
        
        if desiredSum % 2 != 0 {
            return 0
        }
        
        let halfSum = desiredSum / 2
        var dp = [Int](repeating: 0, count: halfSum + 1)
        dp[0] = 1
        
        for i in 0..<nums.count {
            for j in (nums[i]...halfSum).reversed() {
                dp[j] += dp[j - nums[i]]
            }
        }
        
        return dp[halfSum]
    }
}
