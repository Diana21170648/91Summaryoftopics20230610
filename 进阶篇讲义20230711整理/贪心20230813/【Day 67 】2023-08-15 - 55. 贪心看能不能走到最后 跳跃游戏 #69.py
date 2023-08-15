【Day 67 】2023-08-15 - 55. 跳跃游戏 #69
Open
azl397985856 opened this issue yesterday · 3 comments
Comments
@azl397985856
azl397985856 commented yesterday
55. 跳跃游戏
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/jump-game/

前置知识
贪心
题目描述
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
具体就是用一个变量记录当前能够到达的最大的索引

代码
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m_max=0
        n=len(nums)
        for i in range(n-1):
            if m_max<i:
                return Fslse
            m_max=max(m_max,nums[i]+i)
            if m_max>=n-1:
                return True
        return m_max>=n-1
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 贪心 67 labels yesterday
@GuitarYs
GuitarYs commented 20 hours ago
class JumpGame:
    def canJump(self, nums):
        position = 0
        for i in range(len(nums)):
            if position >= len(nums) - 1:
                return True
            if nums[position] == 0:
                return False
            max_jump = nums[position]
            position = position + max_jump
        return False
@freesan44
freesan44 commented 14 hours ago
class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        var maxIndex = 0
        let length = nums.count
        
        for i in 0..<(length - 1) {
            if maxIndex < i {
                return false
            }
            maxIndex = max(maxIndex, nums[i] + i)
            
            if maxIndex >= length - 1 {
                return true
            }
        }
        
        return maxIndex >= length - 1

    }
}
