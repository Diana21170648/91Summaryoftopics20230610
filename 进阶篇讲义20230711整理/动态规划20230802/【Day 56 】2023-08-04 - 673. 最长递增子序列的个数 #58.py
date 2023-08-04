
Open
azl397985856 opened this issue 11 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
673. 最长递增子序列的个数
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/

前置知识
动态规划
题目描述
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
动态规划LIS

代码
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[1,1]for i in range(n)]#[1,1]第一个1表示长度，第二个1表示个数
        ans=[1,1]
        longest=1
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    if dp[i][0]+1>dp[j][0]:
                        dp[j][0]=dp[i][0]+1
                        dp[j][1]=dp[i][1]
                        longest=max(longest,dp[j][0])
                    elif dp[j][0]==dp[i][0]+1:
                        dp[j][1]+=dp[i][1]
        return sum(dp[i][1] for i in range(n) if dp[i][0]==longest)
复杂度分析
时间复杂度：O(N^2)，其中 N 为数组长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added 动态规划 56 labels 11 hours ago
@GuitarYs
GuitarYs commented 4 hours ago
class Solution:
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        lengths = [1] * n  
        counts = [1] * n   
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        max_length = max(lengths)
        res = sum(count for length, count in zip(lengths, counts) if length == max_length)
        return res
@freesan44
freesan44 commented 3 hours ago
class Solution {
    func findNumberOfLIS(_ nums: [Int]) -> Int {
        let n = nums.count
    var dp = [[1, 1]] + Array(repeating: [1, 1], count: n-1)
    var ans = [1, 1]
    var longest = 1
    
    for i in 0..<n {
        for j in i+1..<n {
            if nums[j] > nums[i] {
                if dp[i][0] + 1 > dp[j][0] {
                    dp[j][0] = dp[i][0] + 1
                    dp[j][1] = dp[i][1]
                    longest = max(longest, dp[j][0])
                } else if dp[i][0] + 1 == dp[j][0] {
                    dp[j][1] += dp[i][1]
                }
            }
        }
    }
    
    return dp.filter { $0[0] == longest }.reduce(0) { $0 + $1[1] }
    }
}
