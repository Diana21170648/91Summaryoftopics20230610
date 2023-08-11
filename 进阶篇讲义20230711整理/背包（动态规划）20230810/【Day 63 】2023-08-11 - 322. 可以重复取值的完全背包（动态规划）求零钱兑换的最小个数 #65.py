【Day 63 】2023-08-11 - 322. 零钱兑换 #65
Open
azl397985856 opened this issue 18 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 18 hours ago
322. 零钱兑换
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/coin-change/

前置知识
暂无

题目描述
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回  -1。

你可以认为每种硬币的数量是无限的。

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

@Diana21170648
Diana21170648 commented 1 minute ago
思路
可以重复取值的完全背包

代码
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        
        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin:#还没有达到目标值则更新dp，取小值
                    dp[i]=min(dp[i],dp[i-coin]+1)#dp是要取的最少硬币数，在统计数量
        return -1 if dp[amount]==amount+1 else dp[amount]
复杂度分析

时间复杂度：O(N*amount)，其中 N 为len(coins)。
空间复杂度：O(amount),背包容量大小就是空间复杂度

@azl397985856 azl397985856 added 动态规划 63 labels 18 hours ago
@GuitarYs
GuitarYs commented 9 hours ago
class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
@freesan44
freesan44 commented 8 hours ago
class Solution {
    func coinChange(_ coins: [Int], _ amount: Int) -> Int {
                var dp = [Int](repeating: amount + 1, count: amount + 1)
        dp[0] = 0
        
        for i in 1...amount {
            for coin in coins {
                if i >= coin {
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                }
            }
        }
        
        return dp[amount] == amount + 1 ? -1 : dp[amount]
    }
}
