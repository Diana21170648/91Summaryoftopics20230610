【Day 16 】2023-06-25 - 513. 找树左下角的值 #17
Open
azl397985856 opened this issue 12 hours ago · 7 comments
Comments
@azl397985856
azl397985856 commented 12 hours ago
513. 找树左下角的值
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/find-bottom-left-tree-value/

前置知识
暂无

题目描述
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

  2
 / \
1   3

输出:
1
 

示例 2:

输入:

      1
     / \
    2   3
   /   / \
  4   5   6
     /
    7

输出:
7
 

@Diana21170648
Diana21170648 commented now
思路
bfs找最后一层第一个元素，一共queue
dfs找最深层最后一个元素

代码
import collections
class Solution(object):
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=collections.deque()
        queue.append(root)
        while queue:
            length=len(queue)
            res=queue[0].val#队列最左边的值，即为结果
            for _ in range(length):#处理当前层的所有节点
                cur=queue.popleft()#如果本层不为空，则队列第一个值弹出，为本层腾地方
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
复杂度分析

时间复杂度：O(N)，其中 N 为节点数。
空间复杂度：O(q)，q为队列的长度，最坏情况下为完全二叉树，此时，q=n


@azl397985856 azl397985856 added BFS DFS 树 16 labels 12 hours ago
@bi9potato
bi9potato commented 9 hours ago
Approach
DFS, inorder traversal.

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

    int maxDepth = 0;
    int currDepth = 0;

    int res;

    public int findBottomLeftValue(TreeNode root) {

        dfs(root);

        return res;
        
    }

    private void dfs(TreeNode root) {

        if (root== null) return;

        currDepth++;

    
        dfs(root.left);
        if (root.left == null && root.right == null) {
            if (currDepth > maxDepth) {
                maxDepth = currDepth;
                res = root.val;
            }
            
        }
        
        
        

        dfs(root.right);

        currDepth--;

        

    }


}
Complexity Analysis
Time 
Space 
@SoSo1105
SoSo1105 commented 5 hours ago
思路
找到树的最后一行，找到那一行的第一个节点

代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append(root)
        while queue:
            length = len(queue)
            res = queue[0].val
            for _ in range(length):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@Beanza
Beanza commented 4 hours ago
思路

二叉树先序遍历
用数组存储所有二叉树路径的字符串，最后转换为整数后求和

代码

Definition for a binary tree node.
class TreeNode:
def init(self, val=0, left=None, right=None):
self.val = val
self.left = left
self.right = right
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

@freesan44
freesan44 commented 3 hours ago
代码
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
    func findBottomLeftValue(_ root: TreeNode?) -> Int {
        var queue = [TreeNode?]()
        queue.append(root)
        var res = 0
        while !queue.isEmpty {
            let length = queue.count
            res = queue[0]?.val ?? 0
            for _ in 0..<length {
                let cur = queue.removeFirst()
                if let left = cur?.left {
                    queue.append(left)
                }
                if let right = cur?.right {
                    queue.append(right)
                }
            }
        }
        return res
    }
}
@zhaoygcq
zhaoygcq commented 3 hours ago
思路
使用bfs进行层序遍历，并记录每一层的数据信息
取记录数组的最后一项的第一个值
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
var findBottomLeftValue = function(root) {
    let res = [];
    if(!root) return root;
    const queue = [root];
    while(queue.length) {
        let len = queue.length;
        let temp = [];
        while(len--) {
            const top = queue.shift();
            temp.push(top.val);
            if(top.left) {
                queue.push(top.left);
            }
            if(top.right) {
                queue.push(top.right);
            }
        }
        res.push(temp);
    }
    return res.pop().shift()
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@mo660
mo660 commented 2 hours ago
思路
使用dfs遍历树，记录深度，如果当前深度大于最大深度，就舍弃之前的深度

代码
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int res;
    int maxHeight;
    void dfs(TreeNode* root, int height)
    {
        if (nullptr == root)
            return;
        height++;
        dfs(root->left, height);
        dfs(root->right, height);
        if (height > maxHeight)
        {
            res = root->val;
            maxHeight = height;
        }
    }
    int findBottomLeftValue(TreeNode* root) {
        res = root->val;
        dfs(root, 0);
        return res;
    }
};
