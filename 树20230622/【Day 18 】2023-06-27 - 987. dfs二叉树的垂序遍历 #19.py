【Day 18 】2023-06-27 - 987. 二叉树的垂序遍历 #19
Open
azl397985856 opened this issue 11 hours ago · 7 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
987. 二叉树的垂序遍历
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree

前置知识
DFS
排序
题目描述
给定二叉树，按垂序遍历返回其结点值。

对位于 (X, Y) 的每个结点而言，其左右子结点分别位于 (X-1, Y-1) 和 (X+1, Y-1)。

把一条垂线从 X = -infinity 移动到 X = +infinity ，每当该垂线与结点接触时，我们按从上到下的顺序报告结点的值（Y 坐标递减）。

如果两个结点位置相同，则首先报告的结点值较小。

按 X 坐标顺序返回非空报告的列表。每个报告都有一个结点值列表。



示例 1：



输入：[3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
解释：
在不丧失其普遍性的情况下，我们可以假设根结点位于 (0, 0)：
然后，值为 9 的结点出现在 (-1, -1)；
值为 3 和 15 的两个结点分别出现在 (0, 0) 和 (0, -2)；
值为 20 的结点出现在 (1, -1)；
值为 7 的结点出现在 (2, -2)。
示例 2：



输入：[1,2,3,4,5,6,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
根据给定的方案，值为 5 和 6 的两个结点出现在同一位置。
然而，在报告 "[1,5,6]" 中，结点值 5 排在前面，因为 5 小于 6。


提示：

树的结点数介于 1 和 1000 之间。
每个结点值介于 0 和 1000 之间。

@Diana21170648
Diana21170648 commented 6 minutes ago
思路
三层排序，x排序哪一列，y排序哪一层，值排序满足同一列同位置元素递增

代码
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #用哈希表存储遍历的元素
        seen=collections.defaultdict(lambda:collections.defaultdict(list))
        def dfs(root,x=0,y=0):
            if not root:
                return
            seen[x][y].append(root.val)
            dfs(root.left,x-1,y+1)
            dfs(root.right,x+1,y+1)
        dfs(root)
        ans=[]
        #开始三层排序
        for x in sorted(seen):
            level=[]
            for y in sorted(seen[x]):
                level+=sorted(value for value in seen[x][y])
            ans.append(level)
        return ans
复杂度分析

时间复杂度：O(NlogN)，其中 N 为节点数。
空间复杂度：O(N)

@azl397985856 azl397985856 added 哈希表 树 排序 18 labels 11 hours ago
@hengistchan
hengistchan commented 8 hours ago • 
使用 map + dfs 结合 js 的函数式编程

function verticalTraversal(root: TreeNode | null): number[][] {
  if (!root) return []

  const map = { '0': [[1, root.val]] }

  const dfs = (node: TreeNode | null, cur: number, level: number) => {
    if (!node) return
    if (!map[cur]) {
      map[cur] = []
    }
    map[cur].push([level, node.val])
    dfs(node.left, cur - 1, level + 1)
    dfs(node.right, cur + 1, level + 1)
  }
  
  dfs(root.left, -1, 2)
  dfs(root.right, 1, 2)

  return Object.keys(map).map(key => parseInt(key)).sort((a, b) => a - b).map(key => map[key].sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]).map(item => item[1]))
};
@SoSo1105
SoSo1105 commented 3 hours ago
思路
DFS，BFS

代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        seen = collections.defaultdict(
            lambda: collections.defaultdict(list))

        def dfs(root, x=0, y=0):
            if not root:
                return
            seen[x][y].append(root.val)
            dfs(root.left, x-1, y+1)
            dfs(root.right, x+1, y+1)

        dfs(root)
        ans = []
        # x 排序、
        for x in sorted(seen):
            level = []
            # y 排序
            for y in sorted(seen[x]):
                # 值排序
                level += sorted(v for v in seen[x][y])
            ans.append(level)

        return ans
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@freesan44
freesan44 commented 3 hours ago
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
    func verticalTraversal(_ root: TreeNode?) -> [[Int]] {
        var seen: [Int: [Int: [Int]]] = [:]
    
    func dfs(_ root: TreeNode?, _ x: Int = 0, _ y: Int = 0) {
        guard let root = root else {
            return
        }
        seen[x, default: [:]][y, default: []].append(root.val)
        dfs(root.left, x - 1, y + 1)
        dfs(root.right, x + 1, y + 1)
    }
    
    dfs(root)
    var ans: [[Int]] = []
    for x in seen.keys.sorted() {
        var level: [Int] = []
        for y in seen[x]!.keys.sorted() {
            level.append(contentsOf: seen[x]![y]!.sorted())
        }
        ans.append(level)
    }
    return ans
    }
}
@zhaoygcq
zhaoygcq commented 2 hours ago
思路
使用dfs遍历树，并通过数组记录每一个节点的col、row、val；之后对该数组进行排序，合并

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
 * @return {number[][]}
 */
var verticalTraversal = function(root) {
    let res = [];
    if(!root) return root;
    function dfs(root, row, col) {
        if(!root) return;
        dfs(root.left, row+1, col - 1);
        dfs(root.right, row+1, col + 1);
        res.push({col, row, val: [root.val]});
    }
    dfs(root, 0, 0)

    res.sort((a, b) => {
        if(a.col !== b.col) {
            return a.col - b.col
        } else if(a.row != b.row) {
            return a.row - b.row;
        } else {
            return a.val[0] - b.val[0];
        }
    })
    for(let i = res.length - 1; i > 0; i--) {
        if(res[i].col === res[i-1].col) {
            res[i-1].val.push(...res[i].val);
            res.splice(i, 1);
        }
    }
    return res.map(item => item.val);
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@bi9potato
bi9potato commented 29 minutes ago
Approach
Pre-order traversal to get coordinates of each node, then sort the nodes by their column and row.

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

    class CoordinateMappedNode {
        public int row, col;
        public TreeNode node;

        public CoordinateMappedNode(TreeNode node, int row, int col) {
            this.row = row;
            this.col = col;
            this.node = node;
        }
    }

    List<CoordinateMappedNode> list = new LinkedList<>();

    public List<List<Integer>> verticalTraversal(TreeNode root) {

        traverse(root, 0, 0);
        
        Collections.sort(list, 
            (CoordinateMappedNode node1, CoordinateMappedNode node2) -> {
                if (node1.row == node2.row && node1.col == node2.col) {
                    return node1.node.val - node2.node.val;
                } else if (node1.col == node2.col) {
                    return node1.row - node2.row;
                } else {
                    return node1.col - node2.col;
                }
            }
        );
        
        int currCol = Integer.MIN_VALUE;
        List<List<Integer>> res = new LinkedList<>();
        for (int i = 0; i < list.size(); i++) {
            CoordinateMappedNode node = list.get(i);
            if (node.col > currCol) {
                res.add(new LinkedList<>());
                currCol = node.col;
            }
            res.get(res.size()-1).add(node.node.val);

        }

        return res;


    }

    private void traverse(TreeNode root, int row, int col) {

        if (root == null) return;

        list.add(new CoordinateMappedNode(root, row, col));

        traverse(root.left, row+1, col-1);
        traverse(root.right, row+1, col+1);
    }
}
Complexity Analysis
Time 
 as time complexity of Collections.sort is 
.
Space 
