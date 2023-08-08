【Day 60 】2023-08-08 - 464. 我能赢么 #62
Open
azl397985856 opened this issue 10 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 10 hours ago
464. 我能赢么
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/can-i-win/

前置知识
暂无

题目描述
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？

你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

示例：

输入：
maxChoosableInteger = 10
desiredTotal = 11

输出：
false

解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。


@Diana21170648
Diana21170648 commented 2 minutes ago
思路
动态规划

代码
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        @lru_cache(None)
        def dp(picked, acc):
            if acc >= desiredTotal:
                return False
            if picked == (1 << (maxChoosableInteger + 1)) - 1:
                return False
            for n in range(1, maxChoosableInteger + 1):
                if picked & 1 << n == 0:
                    if not dp(picked | 1 << n, acc + n):
                        return True
            return False

        return dp(0, 0)
复杂度分析

时间复杂度：O(2^m)
空间复杂度：O(2^m)

@azl397985856 azl397985856 added 动态规划 60 labels 10 hours ago
@freesan44
freesan44 commented 2 hours ago
class Solution {
    func canIWin(_ maxChoosableInteger: Int, _ desiredTotal: Int) -> Bool {
        if desiredTotal <= maxChoosableInteger {
            return true
        }
        if (1...maxChoosableInteger).reduce(0, +) < desiredTotal {
            return false
        }
        
        var memo: [Int: Bool] = [:]
        
        func dp(_ picked: Int, _ acc: Int) -> Bool {
            if acc >= desiredTotal {
                return false
            }
            if picked == (1 << (maxChoosableInteger + 1)) - 1 {
                return false
            }
            if let result = memo[picked] {
                return result
            }
            
            for n in 1...maxChoosableInteger {
                if picked & (1 << n) == 0 {
                    if !dp(picked | (1 << n), acc + n) {
                        memo[picked] = true
                        return true
                    }
                }
            }
            memo[picked] = false
            return false
        }
        
        return dp(0, 0)
    }
}
