【Day 79 】2023-08-27 - 814 二叉树剪枝 #81
Open
azl397985856 opened this issue 17 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 17 hours ago
814 二叉树剪枝
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/binary-tree-pruning

前置知识
二叉树
递归
题目描述
给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

返回移除了所有不包含 1 的子树的原二叉树。

( 节点 X 的子树为 X 本身，以及所有 X 的后代。)

示例1:
输入: [1,null,0,0,1]
输出: [1,null,0,null,1]

示例2:
输入: [1,0,1,0,0,0,1]
输出: [1,null,1,null,1]

示例3:
输入: [1,1,0,1,1,0,1,0]
输出: [1,1,0,1,1,null,1]

说明:

给定的二叉树最多有 100 个节点。
每个节点的值只会为 0 或 1

@Diana21170648
Diana21170648 commented 3 minutes ago
思路
二叉树剪枝

代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        A={}
        def minTree(node):
            if not node:
                return None
            if node in A:
                return A[node]
            left=minTree(node.left)
            right=minTree(node.right)
            if not left:
                node.left=None
            if not right:
                node.right=None
            ans=node.val==1 or left or right
            return ans
        return root if minTree(root) else None
复杂度分析

时间复杂度：O(H)，其中 H为二叉树的高度。
空间复杂度：O(N)，最坏的结果是剪掉所有的枝


@azl397985856 azl397985856 added 剪枝 79 labels 17 hours ago
@GuitarYs
GuitarYs commented 7 hours ago
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        else:
            return root
