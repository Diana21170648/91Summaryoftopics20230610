【Day 72 】2023-08-20 - 78. 子集 #74
Open
azl397985856 opened this issue 19 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 19 hours ago
78. 子集
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/subsets/

前置知识
位运算
回溯
题目描述
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

@Diana21170648
Diana21170648 commented 16 minutes ago
思路
用位运算决定每一个元素去还是不取

代码
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans,end=[],1<<len(nums)
        for i in range(end):
            subset=[]
            for j in range(len(nums)):
                if  ((1<<j)&i)!=0:
                    subset.append(nums[j])
            ans.append(subset)
        return ans   
复杂度分析

时间复杂度：O(N*2^N)，其中 N 为数组长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added 位运算 回溯 72 labels 19 hours ago
@Alexno1no2
Alexno1no2 commented 2 hours ago
class Solution:
    
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    # 主函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    # 回溯算法核心函数，遍历子集问题的回溯树
    def backtrack(self, nums: List[int], start: int) -> None:
        
        # 前序位置，每个节点的值都是一个子集
        self.res.append(self.track[:])
        
        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i])
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(nums, i + 1)
            # 撤销选择
            self.track.pop()
