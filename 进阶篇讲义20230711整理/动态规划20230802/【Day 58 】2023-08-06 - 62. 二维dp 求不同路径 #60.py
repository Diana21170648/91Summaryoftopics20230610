【Day 58 】2023-08-06 - 62. 不同路径 #60
Open
azl397985856 opened this issue 18 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 18 hours ago
62. 不同路径
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/unique-paths/

前置知识
暂无

题目描述

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？

 

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9

@Diana21170648
Diana21170648 commented now
思路
DP

代码
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
复杂度分析

时间复杂度：O(M*N)，其中 M,N 为数组长度。
空间复杂度：O(M*N)

@azl397985856 azl397985856 added 动态规划 58 labels 18 hours ago
@SoSo1105
SoSo1105 commented 7 hours ago
思路
动态规划

代码
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                     
        return dp[n-1][m-1]
@snmyj
snmyj commented 3 hours ago
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1)] * (m - 1)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
