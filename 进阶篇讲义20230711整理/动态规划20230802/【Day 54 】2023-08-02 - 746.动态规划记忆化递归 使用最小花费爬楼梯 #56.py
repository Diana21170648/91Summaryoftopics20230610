【Day 54 】2023-08-02 - 746.使用最小花费爬楼梯 #56
Open
azl397985856 opened this issue 18 hours ago · 5 comments
Comments
@azl397985856
azl397985856 commented 18 hours ago
746.使用最小花费爬楼梯
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/min-cost-climbing-stairs/

前置知识
动态规划
题目描述
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

 

示例 1：

输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
 示例 2：

输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出：6
解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
 

提示：

cost 的长度范围是 [2, 1000]。
cost[i] 将会是一个整型数据，范围为 [0, 999] 。
@Diana21170648
Diana21170648 commented now
思路
动态规划

代码
#20230802 第121(54)天 11：18
#T=O(n)
#S=O(1)，滚动数组优化

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = cost[0], cost[1]
        for i in range(2, len(cost)+1):
            next = min(prev, curr) + (cost[i] if i != len(cost) else 0)
            prev, curr = curr, next
        return curr
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 动态规划 54 labels 18 hours ago
@Fuku-L
Fuku-L commented 17 hours ago
代码
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n+1];
        dp[0] = dp[1] = 0;
        for(int i = 2; i<=n; i++){
            dp[i] = Math.min(dp[i-1]+cost[i-1], dp[i-2] + cost[i-2]);
        }
        return dp[n];
    }
}
@dorian-byte
dorian-byte commented 11 hours ago
思路：

这个问题可以通过动态规划来解决。我们可以从顶部开始向下爬楼梯，对于每一步，我们都计算到达这一步的最小成本。这个成本是当前步骤的成本加上到达下一步或下下一步的最小成本。最后，我们返回到达第0步或第1步的最小成本，因为我们可以从这两步开始爬楼梯。

代码：

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[n-1] = cost[n-1]

        for i in range(n-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])
复杂度分析：

时间复杂度：O(n)
空间复杂度：O(n)

@freesan44
freesan44 commented 10 hours ago
class Solution {
    func minCostClimbingStairs(_ cost: [Int]) -> Int {
        if cost.isEmpty {
        return 0
    }
    
    var dp = Array(repeating: 0, count: cost.count + 1)
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in 2...cost.count {
        dp[i] = min(dp[i - 1], dp[i - 2]) + (i == cost.count ? 0 : cost[i])
    }
    
    return dp[cost.count]
    }
}
@acy925
acy925 commented 5 hours ago
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimum_cost = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i - 1] + cost[i - 1]
            take_two_steps = minimum_cost[i - 2] + cost[i - 2]
            minimum_cost[i] = min(take_one_step, take_two_steps)
        return minimum_cost[-1]
