【Day 15 】2023-06-24 - 129. 求根到叶子节点数字之和 #16
Open
azl397985856 opened this issue 17 hours ago · 11 comments
Comments
@azl397985856
azl397985856 commented 17 hours ago
129. 求根到叶子节点数字之和
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

前置知识
DFS
BFS
前序遍历
题目描述
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
  1
 / \
2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
  4
 / \
9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.

@Diana21170648
Diana21170648 commented now
思路
dfs或bfs，求树的路径

代码
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,cur):
            if not root:
                return 0
            if not root.left and not root.right:
                return cur*10+root.val
            return dfs(root.left,cur*10+root.val)+ dfs(root.right,cur*10+root.val)
        return dfs(root,0)
复杂度分析

时间复杂度：O(N)，其中 N 为节点数目。
空间复杂度：O(h)，h为二叉树的深度


@azl397985856 azl397985856 added BFS DFS 树 15 labels 17 hours ago
@bi9potato
bi9potato commented 15 hours ago
Approach
DFS

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

    int res = 0;
    StringBuilder num = new StringBuilder();

    public int sumNumbers(TreeNode root) {

        dfs(root);

        return res;
        
    }

    private void dfs(TreeNode root) {

        if (root == null) return;
        num.append(root.val);
        if (root.left == null && root.right == null) res += Integer.parseInt(num.toString());

        dfs(root.left);
        dfs(root.right);

        num.deleteCharAt(num.length() - 1);

    }
}
Complexity Analysis
Time 
Space 
@SoSo1105
SoSo1105 commented 11 hours ago
思路
二叉树先序遍历
用数组存储所有二叉树路径的字符串，最后转换为整数后求和

代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        path = ''
        result = []
        
        self.helper(root, path, result)
        
        return sum([int(path) for path in result])
    
    def helper(self, root, path, result):
        if not root:
            return 
        
        path += str(root.val)
        
        if not root.left and not root.right:
            result.append(path)
            
        self.helper(root.left, path, result)
        self.helper(root.right, path, result)
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@RestlessBreeze
RestlessBreeze commented 6 hours ago
code
class Solution {
public:
    int res;

    void traversal(TreeNode* root, int prev)
    {
        if (!root)
            return;
        if (!root->left && !root->right)
        {
            res += prev * 10 + root->val;
            return;
        }
        traversal(root->left, prev * 10 + root->val);
        traversal(root->right, prev * 10 + root->val);
    }

    int sumNumbers(TreeNode* root) {
        res = 0;
        traversal(root, 0);
        return res;
    }
};
@jennyjgao
jennyjgao commented 5 hours ago
class Solution {
    int res = 0;
    public int sumNumbers(TreeNode root) {
        dfs(root,0);
        return res;
    }
    public void dfs(TreeNode root, int pre){
        if(root == null) return;
        pre = pre*10 + root.val;
        if(root.left == null && root.right == null){
            res += pre;
            return;
        }
        if(root.left !=null){
            dfs(root.left, pre);
        }

        if(root.right != null){
            dfs(root.right, pre);
        }
    }
}
@hengistchan
hengistchan commented 3 hours ago
function sumNumbers(root: TreeNode | null, sum = 0): number {
  const isLeaf = (node: TreeNode) => !node?.left && !node?.right
  if (!root || isLeaf(root)) {
    return sum * 10 + root?.val || 0
  }
  return sumNumbers(root.left, sum * 10 + root.val) + sumNumbers(root.right, sum * 10 + root.val)
};
@zhangyu1131
zhangyu1131 commented 3 hours ago
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if (!root)
        {
            return 0;
        }
        int tmp = 0;
        long long sum = 0;
        preOrder(root, tmp, sum);
        return (int) sum;
    }

private:
    void preOrder(TreeNode* root, int& tmp, long long& sum)
    {
        if (!root->left && !root->right)
        {
            tmp = 10 * tmp + root->val;
            sum += tmp;
            tmp = tmp / 10;
            return;
        }

        tmp = 10 * tmp + root->val;
        if (root->left)
        {
            preOrder(root->left, tmp, sum);
        }
        if (root->right)
        {
            preOrder(root->right, tmp, sum);
        }
        tmp = tmp / 10;
    }
};
@GuitarYs
GuitarYs commented 3 hours ago
class TreeNode:
def init(self, val=0, left=None, right=None):
self.val = val
self.left = left
self.right = right

def sumNumbers(root: TreeNode) -> int:
if not root:
return 0

def dfs(node, num):
    if not node:
        return 0
    
    num = num * 10 + node.val
    if not node.left and not node.right:
        return num
    
    return dfs(node.left, num) + dfs(node.right, num)

return dfs(root, 0)
@snmyj
snmyj commented 1 hour ago
class Solution {
public:
    
    int dfs(TreeNode* root,int num){
        if(root==nullptr) return 0;
        int sum=10*num+root->val;
        if(root->right==nullptr&&root->left==nullptr) return sum;
    
       
        else return dfs(root->left,sum)+dfs(root->right,sum);
        
    }
    int sumNumbers(TreeNode* root) {
        return dfs(root,0);
    }
};

@zhaoygcq
zhaoygcq commented 1 hour ago
思路
收集所有的路径(根节点到叶子节点)
在叶子节点处，计算当前路径的数值
代码
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumNumbers = function(root) {
    let res = 0;
    if(!root) return res;
    const dfs = (root, arr = []) => {
        arr.push(root.val);
        if(!root.left && !root.right) {
            res += Number([...arr].join(""));
            return;
        }
        if(root.left) {
            dfs(root.left, arr);
            arr.pop();
        }
        if(root.right) {
            dfs(root.right, arr);
            arr.pop();
        }
    }
    dfs(root, []);
    
    return res;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
@catkathy
catkathy commented 51 minutes ago
Code
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, current_sum: int) -> int:
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            left_sum = dfs(node.left, current_sum)
            right_sum = dfs(node.right, current_sum)

            return left_sum + right_sum

        return dfs(root, 0)
