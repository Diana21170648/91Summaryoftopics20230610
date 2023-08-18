【Day 70 】2023-08-18 - 932. 漂亮数组 #72
Open
azl397985856 opened this issue 11 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
932. 漂亮数组
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/beautiful-array/

前置知识
分治
题目描述
对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：

对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。

那么数组 A 是漂亮数组。

 

给定 N，返回任意漂亮数组 A（保证存在一个）。

 

示例 1：

输入：4
输出：[2,1,4,3]


示例 2：

输入：5
输出：[3,1,2,5,4]

 

提示：

1 <= N <= 1000
@Diana21170648
Diana21170648 commented now
思路
问题分解为子问题，递归解决，注意需要分为奇数和偶数

代码
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        @lru_cache(None)
        def dp(n):#递归调用
            if n==1:
                return [1]
            ans=[]
            for i in dp(n-n//2):
                ans+=[i*2-1]
            for j in dp(n//2):
                ans+=[j*2]
            return ans
        return dp(N)
复杂度分析

时间复杂度：O(2^N)，其中 N 为数组长度。
空间复杂度：O(N)
 
@azl397985856 azl397985856 added 分治 70 labels 11 hours ago
@freesan44
freesan44 commented 3 hours ago
class Solution {
    func beautifulArray(_ N: Int) -> [Int] {
        var cache = [Int: [Int]]()

        func dp(_ n: Int) -> [Int] {
            if n == 1 {
                return [1]
            }

            if let cachedResult = cache[n] {
                return cachedResult
            }

            var ans = [Int]()
            for a in dp(n - n / 2) {
                ans.append(a * 2 - 1)
            }
            for b in dp(n / 2) {
                ans.append(b * 2)
            }

            cache[n] = ans
            return ans
        }

        return dp(N)
    }
}

