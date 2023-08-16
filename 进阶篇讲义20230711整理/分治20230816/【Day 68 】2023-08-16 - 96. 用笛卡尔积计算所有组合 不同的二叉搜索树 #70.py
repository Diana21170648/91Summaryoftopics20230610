【Day 68 】2023-08-16 - 96. 用笛卡尔积计算所有组合 不同的二叉搜索树 #70
Open
azl397985856 opened this issue yesterday · 2 comments
Comments
@azl397985856
azl397985856 commented yesterday
96. 不同的二叉搜索树
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/unique-binary-search-trees/

前置知识
二叉搜索树
分治
题目描述
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

 1         3     3      2      1
  \       /     /      / \      \
   3     2     1      1   3      2
  /     /       \                 \
 2     1         2                 3

@Diana21170648
Diana21170648 commented 1 minute ago
思路
用笛卡尔积计算所有组合
用哈希表优化时间复杂度
分治

代码
class Solution:
    visited=dict()
    def numTrees(self, n: int) -> int:
        if n in self.visited:
            return self.visited.get(n)
        if n<=1:
            return 1
        ans=0
        for i in range(1,n+1):
            ans+=self.numTrees(i-1)*self.numTrees(n-i)#笛卡尔积
        self.visited[n]=ans
        return ans
复杂度分析

时间复杂度：O(N^2)。
空间复杂度：O(N),递归栈的深度和哈希表均为n
@azl397985856 azl397985856 added 分治 68 labels yesterday
@GuitarYs
GuitarYs commented 20 hours ago
class Solution:
    def numTrees(self, n):
        if n == 0 or n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        
        return dp[n]

# 示例用法
solution = Solution()
n = 3
result = solution.numTrees(n)
print(result)
