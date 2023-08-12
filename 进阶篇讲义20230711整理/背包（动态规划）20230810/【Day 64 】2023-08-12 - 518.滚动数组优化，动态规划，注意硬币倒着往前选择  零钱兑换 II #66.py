【Day 64 】2023-08-12 - 518. 零钱兑换 II #66
Open
azl397985856 opened this issue 10 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 10 hours ago
518. 零钱兑换 II
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/coin-change-2/

前置知识
暂无

题目描述
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1
 

注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
@Diana21170648
Diana21170648 commented 1 minute ago
思路
滚动数组优化，动态规划，注意硬币倒着往前选择

代码
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)#求max，dp初始化为0
        dp[0]=1
        for j in range(len(coins)):#硬币大小
            for i in range(1,amount+1):#背包大小
                if i>=coins[j]:
                    #dp[i - coins[j]] 表示在从总金额中减去当前硬币面额的值后，剩余的金额的方法数
                    #硬币面额小于当前面额，才能通过硬币组合实现amount
                    dp[i]+=dp[i-coins[j]]#选择i，dp[i]表示凑成zmount的次数
        return dp[-1]
复杂度分析

时间复杂度：O(n*amount)，n=len(coins)。
空间复杂度：O(amount),amount即为背包的大小

@azl397985856 azl397985856 added 动态规划 64 labels 10 hours ago
@yetfan
yetfan commented 4 hours ago
代码
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount+1):
                dp[i] += dp[i-c]

        return dp[amount]
