【Day 80 】2023-08-28 - 39 组合总和 #82
Open
azl397985856 opened this issue 10 hours ago · 4 comments
Comments
@azl397985856
azl397985856 commented 10 hours ago
39 组合总和
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/combination-sum/

前置知识
剪枝
回溯
题目描述
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
[7],
[2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
[2,2,2,2],
[2,3,3],
[3,5]
]


提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

@Diana21170648
Diana21170648 commented now
思路
回溯
剪枝

代码
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(ans,temp,candidates,tar,start):
            if tar<0:
                return
            elif tar==0:
                return ans.append(temp.copy())
            for i in range(start,len(candidates)):
                temp.append(candidates[i])
                backtrack(ans,temp,candidates,tar-candidates[i],i)#代表数字可以重复使用
                temp.pop()
        ans=[]
        backtrack(ans,[],candidates,target,0)
        return ans
复杂度分析

时间复杂度：O(N^H)，其中 N 为数组长度,H为递归栈的最大深度。
空间复杂度：O(H)，H为递归栈的最大深度.


@azl397985856 azl397985856 added 剪枝 回溯 80 labels 10 hours ago
@Beanza
Beanza commented 10 hours ago
*/
class Solution {
public TreeNode pruneTree(TreeNode root) {
if(root == null){
return null;
}
root.left = pruneTree(root.left);
root.right = pruneTree(root.right);
if(root.left == null && root.right == null && root.val == 0){
return null;
}
return root;
}
}

@GuitarYs
GuitarYs commented 7 hours ago
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        def backtrack(start, curr_list, curr_sum):
            if curr_sum == target:
                result.append(curr_list[:])
                return
            if curr_sum > target:
                return
            for i in range(start, len(candidates)):
                curr_list.append(candidates[i]) 
                curr_sum += candidates[i] 
                backtrack(i, curr_list, curr_sum)
                curr_list.pop()  
                curr_sum -= candidates[i]  
        backtrack(0, [], 0)

        return result
@freesan44
freesan44 commented 2 hours ago
class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var ans = [[Int]]()
        
        func backtrack(_ list: inout [[Int]], _ tempList: inout [Int], _ nums: [Int], _ remain: Int, _ start: Int) {
            if remain < 0 {
                return
            } else if remain == 0 {
                list.append(tempList)
                return
            }
            for i in start..<nums.count {
                tempList.append(nums[i])
                backtrack(&list, &tempList, nums, remain - nums[i], i)
                tempList.removeLast()
            }
        }
        
        var tempList = [Int]()
        backtrack(&ans, &tempList, candidates.sorted(), target, 0)
        return ans
    }
}
