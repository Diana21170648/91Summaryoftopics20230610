【Day 44 】2023-07-23 - 837. 滑动窗口+动态规划找 新 21 点 #46
Open
azl397985856 opened this issue yesterday · 7 comments
Comments
@azl397985856
azl397985856 commented yesterday
837. 新 21 点
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/new-21-game

前置知识
暂无

题目描述
爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：

爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。

当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？

 

示例 1：

输入：N = 10, K = 1, W = 10
输出：1.00000
说明：爱丽丝得到一张卡，然后停止。
示例 2：

输入：N = 6, K = 1, W = 10
输出：0.60000
说明：爱丽丝得到一张卡，然后停止。
在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。
示例 3：

输入：N = 21, K = 17, W = 10
输出：0.73278
 

提示：

0 <= K <= N <= 10000
1 <= W <= 10000
如果答案与正确答案的误差不超过 10^-5，则该答案将被视为正确答案通过。
此问题的判断限制时间已经减少。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
滑动窗口+动态规划

代码
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp=[0]*(k+maxPts)#动态规划
        sum=0#滑动窗口
        for i in range(k,k+maxPts):
            if i<=n:
                dp[i]=1
            sum+=dp[i]
        for i in range(k-1,-1,-1):
            dp[i]=sum/maxPts
            sum+=dp[i]-dp[i+maxPts]
        return dp[0]
复杂度分析

时间复杂度：T=O(K+maxPts)，其中 N 为数组长度。
空间复杂度：S=O(K+maxPts)

@azl397985856 azl397985856 added 二分 滑动窗口 44 labels yesterday
@hengistchan
hengistchan commented 20 hours ago
class Solution {
    public double new21Game(int n, int k, int maxPts) {
        if (k == 0) {
            return 1.0;
        }
        double[] dp = new double[k + maxPts];
        for (int i = k; i <= n && i < k + maxPts; i++) {
            dp[i] = 1.0;
        }
        for (int i = k - 1; i >= 0; i--) {
            for (int j = 1; j <= maxPts; j++) {
                dp[i] += dp[i + j] / maxPts;
            }
        }
        return dp[0];
    }
}
@GuitarYs
GuitarYs commented 19 hours ago
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # 创建动态规划数组
        dp = [0.0] * (K + W)
        
        # 计算累积概率
        for i in range(K, N + 1):
            dp[i] = 1.0
        
        # 计算剩余的概率
        for i in range(K - 1, -1, -1):
            for j in range(1, W + 1):
                dp[i] += dp[i + j] / W
        
        return dp[0]

# 创建示例对象并调用方法
solution = Solution()
result = solution.new21Game(N=10, K=1, W=10)
print("输出：{:.5f}".format(result))

result = solution.new21Game(N=6, K=1, W=10)
print("输出：{:.5f}".format(result))

result = solution.new21Game(N=21, K=17, W=10)
print("输出：{:.5f}".format(result))
@dorian-byte
dorian-byte commented 5 hours ago
def new_21_game_prob(n, k, maxPts):
    if k == 0 or n >= k + maxPts:
        return 1.0

    dp = [0.0] * (k + maxPts)
    for i in range(k, min(n, k + maxPts)):
        dp[i] = 1.0

    dp[k - 1] = float(min(n - k + 1, maxPts)) / maxPts

    for i in range(k - 2, -1, -1):
        dp[i] = dp[i + 1] - (dp[i + maxPts + 1] - dp[i + 1]) / maxPts

    return dp[0]
@catkathy
catkathy commented 4 hours ago
class Solution:
    def new21Game(self, N, K, maxPts):
        if K == 0:
            return 1.0
        if N >= K - 1 + maxPts:
            return 1.0

        dp = [0.0] * (N + 1)

        probability = 0.0  
        windowSum = 1.0 
        dp[0] = 1.0

        for i in range(1, N + 1):
            dp[i] = windowSum / maxPts

            if i < K:
                windowSum += dp[i]
            else:
                probability += dp[i]

            if i >= maxPts:
                windowSum -= dp[i - maxPts]

        return probability
@Fuku-L
Fuku-L commented 2 hours ago
代码
class Solution {
    public double new21Game(int n, int k, int maxPts) {
            if (k == 0) {
                return 1.0;
            }
            double[] dp = new double[k + maxPts];
            for (int i = k; i <= n && i < k + maxPts; i++) {
                dp[i] = 1.0;
            }
            dp[k - 1] = 1.0 * Math.min(n-k+1, maxPts) / maxPts;
            for (int i = k - 2; i >= 0; i--) {
                dp[i] = dp[i + 1] - (dp[i+maxPts+1] - dp[i + 1]) / maxPts;
            }
            return dp[0];
    }
}
@Beanza
Beanza commented 8 minutes ago
class Solution {
public double new21Game(int n, int k, int maxPts) {
if (k == 0) {
return 1.0;
}
double[] dp = new double[k + maxPts];
for (int i = k; i <= n && i < k + maxPts; i++) {
dp[i] = 1.0;
}
for (int i = k - 1; i >= 0; i--) {
for (int j = 1; j <= maxPts; j++) {
dp[i] += dp[i + j] / maxPts;
}
}
return dp[0];
}
}

