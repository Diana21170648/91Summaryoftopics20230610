【Day 81 】2023-08-29 - 40 组合总数 II #83
Open
azl397985856 opened this issue 11 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
40 组合总数 II
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/combination-sum-ii/

前置知识
剪枝
数组
回溯
题目描述
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
[1, 7],
[1, 2, 5],
[2, 6],
[1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
[1,2,2],
[5]
]
@azl397985856 azl397985856 added 剪枝 回溯 81 labels 11 hours ago
@Diana21170648
Diana21170648 commented now
思路
回溯忘记pop了，老报错

代码
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        if n==0:
            return []
        candidates.sort()
        temp=[]
        ans=[]
        def backtrack(curcandidates,target,n,curSum,indBgein,temp,ans):
            if curSum==target:
                ans.append(temp.copy())
            for i in range(indBgein,n):
                nextSum=curSum+curcandidates[i]
                if nextSum>target:
                    break
                if i>indBgein and  curcandidates[i-1]==curcandidates[i]:
                    continue
                temp.append(curcandidates[i])
                backtrack(curcandidates,target,n,nextSum,i+1,temp,ans)
                temp.pop()
        backtrack(candidates,target,n,0,0,temp,ans)
        return ans

复杂度分析

时间复杂度：O(N*2^n)，其中 N 为数组长度。
空间复杂度：O(Target/N)，递归调用栈深度和记录路径的长度

@freesan44
freesan44 commented 1 hour ago
class Solution {
    func combinationSum2(_ candidates: [Int], _ target: Int) -> [[Int]] {
        let lenCan = candidates.count
        if lenCan == 0 {
            return []
        }
        let sortedCandidates = candidates.sorted()
        var path = [Int]()
        var res = [[Int]]()
        backtrack(sortedCandidates, target, lenCan, 0, 0, &path, &res)
        return res
    }
    
    func backtrack(_ curCandidates: [Int], _ target: Int, _ lenCan: Int, _ curSum: Int, _ indBegin: Int, _ path: inout [Int], _ res: inout [[Int]]) {
        if curSum == target {
            res.append(path)
        }
        var index = indBegin
        while index < lenCan {
            let nextSum = curSum + curCandidates[index]
            if nextSum > target {
                break
            }
            if index > indBegin && curCandidates[index-1] == curCandidates[index] {
                index += 1
                continue
            }
            path.append(curCandidates[index])
            backtrack(curCandidates, target, lenCan, nextSum, index+1, &path, &res)
            path.removeLast()
            index += 1
        }
    }
}

