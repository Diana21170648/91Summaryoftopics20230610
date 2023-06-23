【Day 14 】2023-06-23 - 100. 相同的树 #15
Open
azl397985856 opened this issue yesterday · 13 comments
Comments
@azl397985856
azl397985856 commented yesterday
100. 相同的树
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/same-tree/

前置知识
递归
层序遍历
前中序确定一棵树
题目描述
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
        / \       / \
       2   3     2   3

      [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
        /           \
       2             2

      [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
        / \       / \
       2   1     1   2

      [1,2,1],   [1,1,2]

输出: false

@Diana21170648
Diana21170648 commented now
思路
法一用递归，法二用队列创建BFS实现层序遍历，法三用前序和中序遍历判断树的结构是否相同,以下程序用法二BFS

代码
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not q and not p:
            return True
        if not q or not q:
            return False
        q1 = collections.deque([p])
        q2 = collections.deque([q])
        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1 is None and node2 is None:#判断node.val时需要判断是否为空，否则力扣代码提交会报错
                continue  # 继续下一次循环
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                q1.append(left1)
            if right1:
                q1.append(right1)
            if left2:
                q2.append(left2)
            if right2:
                q2.append(right2)
        return not q1 and not q2
复杂度分析

时间复杂度：O(N)，其中 N 为节点个数。
空间复杂度：O(Q)，最长队列的长度

@azl397985856 azl397985856 added DFS 树 BFS 14 labels yesterday
@hengistchan
hengistchan commented 20 hours ago
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean{
  if (p == null && q === null) return true;
  if (!p && q || !q && p) return false;
  if (p.val !== q.val) return false;
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
@joemonkeylee
joemonkeylee commented 18 hours ago
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    if (p === null && q === null) {
        return true;
    }
    if (p === null || q === null) {
        return false;
    }
    if (p.val !== q.val) {
        return false;
    }
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
@bi9potato
bi9potato commented 18 hours ago
Approach
DFS. Note the base case, only q == p == null means the traverse is completed and return true then.

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
    public boolean isSameTree(TreeNode p, TreeNode q) {

        if (p == null) {
            if (q == null) return true; // traverse completed
            else return false;
        } else { // p != null
            if (q == null || p.val != q.val) return false;
        }

        boolean isLeftSame = isSameTree(p.left, q.left);
        boolean isRightSame = isSameTree(p.right, q.right);

        return isLeftSame &&  isRightSame;
        
    }
}
Complexity Analysis
Time 
Space 
@SoSo1105
SoSo1105 commented 15 hours ago
思路
通过分别遍历两棵树来获取它们的遍历序列（前序遍历、中序遍历和后序遍历均可），然后判断序列是否相同即可。

代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None: return True
        if p == None or q == None: return False

        r1, r2 = [], []
        def inorder(root, index):
            if root == None:
                if index == 1: r1.append(-1)
                else: r2.append(-1)
                return None

            if index == 1: r1.append(root.val)
            else: r2.append(root.val)
            inorder(root.left, index)
            inorder(root.right, index)

        inorder(p, 1)
        inorder(q, 2)
        
        return r1 == r2 
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@RanDong22
RanDong22 commented 14 hours ago
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if(p == null && q == null) 
        return true;
    if(p == null || q == null) 
        return false;
    if(p.val != q.val) 
        return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
@RestlessBreeze
RestlessBreeze commented 9 hours ago
code
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q)
            return true;
        if (!p && q)
            return false;
        if (p && !q)
            return false;
        if (p->val != q->val)
            return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
@catkathy
catkathy commented 6 hours ago
Code
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.extend([
                    (p.left,  q.left),
                    (p.right, q.right)
                ])
            elif p or q:
                return False
        return True
@snmyj
snmyj commented 3 hours ago
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
       if(p==nullptr&&q==nullptr) return true;
       if(p==nullptr||q==nullptr) return false;
       
       return (p->val==q->val)&&isSameTree(p->left,q->left)&&isSameTree(p->right,q->right);
    }
};

@huizsh
huizsh commented 2 hours ago
class Solution:
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
if not p and not q:
return True
if not p or not q:
return False
return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

@zhaoygcq
zhaoygcq commented 2 hours ago
思路
使用递归实现
确定边界条件：

两个节点都为null时，返回true
如果只有一个节点为null，返回false
判断两个都不为null节点的值是否相等，若相等，进一步判断其子节点是否相等(左子节点、右子节点)
反之，直接返回false
代码
var isSameTree = function(p, q) {
    if(!p && !q) return true;
    if((p && !q) || (!p && q)) return false;
    if(p.val === q.val) {
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    } else {
        return false;
    }
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
@Hughlin07
Hughlin07 commented 1 hour ago
class Solution {

public boolean isSameTree(TreeNode p, TreeNode q) {
    if (p == null && q == null) return true;
    if (p == null || q == null) return false;
    if (p.val != q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
}

@Fuku-L
Fuku-L commented 1 hour ago
代码
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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null || q == null) return p == q;
        if(p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
