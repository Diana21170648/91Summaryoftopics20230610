【Day 13 】2023-06-22 - 104. 二叉树的最大深度 #14
Open
azl397985856 opened this issue yesterday · 13 comments
Comments
@azl397985856
azl397985856 commented yesterday
104. 二叉树的最大深度
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree

前置知识
递归
题目描述
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

  3
 / \
9  20
  /  \
 15   7
返回它的最大深度 3 。

@Diana21170648
Diana21170648 commented 1 minute ago • 
思路
遇到二叉树，就考虑dfs
也可用层序遍历BFS

代码
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
复杂度分析

时间复杂度：O(N)，其中 N 为节点数。
空间复杂度：O(h)，h为树的深度，最坏情况下h=N，这时候树转化为链表


@azl397985856 azl397985856 added DFS 树 13 labels yesterday
@bi9potato
bi9potato commented yesterday
Approach
recursion, depth = max(left_depth, right_depth) + 1

Code
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {

        if (root == null) {
            return 0;
        }

        int left_depth = maxDepth(root.left);
        int right_depth = maxDepth(root.right);

        return Math.max(left_depth, right_depth ) + 1;
        
    }
}
Complexity Analysis
Time 
Space 
@SoSo1105
SoSo1105 commented 15 hours ago
思路
递归去计算左右子树的最大深度，当遇到叶子节点时，退出递归。

代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_tree_depth = self.maxDepth(root.left)
        right_tree_depth = self.maxDepth(root.right)

        return max(left_tree_depth, right_tree_depth) + 1
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@zhaoygcq
zhaoygcq commented 13 hours ago
思路
使用递归实现： 节点最大高度 = max(左子节点最大高度， 右子节点最大高度) + 1；
确定边界条件：
if(!root) return 0;

代码
var maxDepth = function(root) {
    if(!root) return 0;
    let left = maxDepth(root.left);
    let right = maxDepth(root.right);

    return Math.max(left, right) + 1;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
@RocJeMaintiendrai
RocJeMaintiendrai commented 9 hours ago
Recursion
class Solution {
public int maxDepth(TreeNode root) {
if(root == null) {
return 0;
}
int left = maxDepth(root.left);
int right = maxDepth(root.right);
return Math.max(left, right) + 1;
}
}

// Iteration
class Solution {
public int maxDepth(TreeNode root) {
if(root == null) return 0;
int max = 1;
Stack nodes = new Stack<>();
Stack depths = new Stack<>();
nodes.push(root);
depths.push(1);
while(!nodes.empty()) {
TreeNode cur = nodes.pop();
int depth = depths.pop();
if(cur.left == null && cur.right == null) {
max = Math.max(max, depth);
}
if(cur.right != null) {
nodes.push(cur.right);
depths.push(depth + 1);
}
if(cur.left != null) {
nodes.push(cur.left);
depths.push(depth + 1);
}
}
return max;
}
}

@freesan44
freesan44 commented 8 hours ago
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    }
}
@RanDong22
RanDong22 commented 8 hours ago
/**

Definition for a binary tree node.
function TreeNode(val) {
this.val = val;
this.left = this.right = null;
}
/
/*
@param {TreeNode} root
@return {number}
*/
var maxDepth = function(root) {
if(!root) {
return 0;
} else {
const left = maxDepth(root.left);
const right = maxDepth(root.right);
return Math.max(left, right) + 1;
}
};
@hengistchan
hengistchan commented 7 hours ago
function maxDepth(root: TreeNode | null): number {
  if(!root) return 0;
  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
};
@catkathy
catkathy commented 5 hours ago
Code
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
@Alexno1no2
Alexno1no2 commented 1 hour ago
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 节点为空，高度为 0
        if root == None:
            return 0

        # 递归计算左子树的最大深度
        leftHeight = self.maxDepth(root.left)
        # 递归计算右子树的最大深度
        rightHeight = self.maxDepth(root.right)

        # 二叉树的最大深度 = 子树的最大深度 + 1（1 是根节点）
        return max(leftHeight, rightHeight) + 1
@snmyj
snmyj commented 1 hour ago
int maxDepth(struct TreeNode* root){
   if(root==NULL)
   return 0;
   else{
       int m=maxDepth(root->left);
       int n=maxDepth(root->right);
       if(m>n)
       return m+1;
       else
       return n+1;
   }
}

@Beanza
Beanza commented 32 minutes ago
int maxDepth(struct TreeNode* root){
if(root==NULL)
return 0;
else{
int m=maxDepth(root->left);
int n=maxDepth(root->right);
if(m>n)
return m+1;
else
return n+1;
}
}

@joemonkeylee
joemonkeylee commented 2 minutes ago
function maxDepth(root: TreeNode | null): number {
    if (!root) return 0;
    let leftHeight = maxDepth(root.left);
    let rightHeight = maxDepth(root.right);
    let height = 1 + Math.max(leftHeight, rightHeight);
    return height;
};
