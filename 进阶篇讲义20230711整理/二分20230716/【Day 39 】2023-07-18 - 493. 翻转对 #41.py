【Day 39 】2023-07-18 - 493. 翻转对 #41
Open
azl397985856 opened this issue 11 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
493. 翻转对
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/reverse-pairs

前置知识
二分法
题目描述
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。
@Diana21170648
Diana21170648 commented now • edited 
思路
二分

代码
from sortedcontainers import SortedList
class Solution:
    #def reversePairs(self, nums: List[int]) -> int:
    def reversePairs(self,A):
        d=SortedList()
        cnt=0
        for a in A:
            i=d.bisect_right(a*2)
            cnt+=len(d)-i
            d.add(a)
        return cnt

复杂度分析

时间复杂度：O(NlogN)，其中 N 为数组长度。
空间复杂度：O(N)


@azl397985856 azl397985856 added 二分 39 labels 11 hours ago
@freesan44
freesan44 commented 3 hours ago
class Solution {
    func reversePairs(_ A: [Int]) -> Int {
        var ans = 0
        
        for i in 0..<A.count {
            for j in (i+1)..<A.count {
                if A[i] > A[j] * 2 {
                    ans += 1
                }
            }
        }
        
        return ans
    }
}

