【Day 17 】2023-06-26 - 297. 二叉树的序列化与反序列化 #18
Open
azl397985856 opened this issue 15 hours ago · 10 comments
Comments
@azl397985856
azl397985856 commented 15 hours ago
297. 二叉树的序列化与反序列化
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

前置知识
暂无

题目描述
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

  1
 / \
2   3
   / \
  4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

@Diana21170648
Diana21170648 commented now
思路
序列化就是遍历，把遍历的结果变成字符串，反序列化的时候，需要考虑序列化的顺序，以便更好地进行确定跟和各个节点的值

dfs和bfs都能做，实现的过程有差别

代码
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if not root:
                return "null,"
            return str(root.val)+","+preorder(root.left)+preorder(root.right)
        return preorder(root)[:-1]#对字符串切片，最后一个字符后不加逗号
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        nodes=data.split(",")
        def preorder(i):
            if i>=len(nodes) or nodes[i]=="null":
                return i,None
            root=TreeNode(nodes[i])
            j,root.left=preorder(i+1)
            k,root.right=preorder(j+1)
            return k,root
        return preorder(0)[1]
复杂度分析

时间复杂度：O(N)，其中 N 为节点数目。
空间复杂度：O(h)，h为树的高度



@azl397985856 azl397985856 added BFS DFS 树 17 labels 15 hours ago
@bi9potato
bi9potato commented 11 hours ago
Approach
Preorder traverse

Code
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    StringBuilder sb;

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        sb = new StringBuilder();

        serializeTraverse(root);

        sb.insert(0, '[');
        sb.setCharAt(sb.length()-1, ']');

        return sb.toString();
    }

    private void serializeTraverse(TreeNode root) {

        if (root == null) {
            sb.append('*').append(',');
            return;
        }

        sb.append(root.val).append(',');

        serializeTraverse(root.left);
        serializeTraverse(root.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {

        String[] vals = data.substring(1, data.length()-1).split(",");

        Queue<String> q = new LinkedList<>();
        for (String val : vals) {
            q.offer(val);
        }

        return deserializeTraverse(q);
    }

    private TreeNode deserializeTraverse(Queue<String> q) {

        if (q.isEmpty() ) return null;
        if (q.peek().equals("*")) {
            q.poll();
            return null;
        }

        int num = Integer.parseInt(q.poll());

        TreeNode node = new TreeNode(num);

        node.left = deserializeTraverse(q);
        node.right = deserializeTraverse(q);

        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
Complexity Analysis
Time 
Space 
@zhaoygcq
zhaoygcq commented 7 hours ago
思路
使用bfs进行层序遍历，并记录每一层的数据信息(需要记录到叶子节点的子节点(用于反序列化时判断是否需要创建子节点))
借用一个队列，通过bfs实现反序列化： 队列维护当前已构建树的节点信息；从序列化的内容中每次取两个值，这两个值就是当前树节点的左右子节点。
代码
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    let res = [];
    if(!root) return 'x';
    let queue = [root];
    while(queue.length) {
        let len = queue.length;
        while(len--) {
            let top = queue.shift();
            res.push(top ? top.val : 'x');
            if(top) {
                queue.push(top.left);
            }
            if(top) {
                queue.push(top.right);
            }
        }
    }
    return res.join(",");
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    let arr = data.split(",");
    if(arr[0] == 'x') return null;
    let root = new TreeNode(arr[0]);
    let cursor = 1;
    let queue = [root];
    while(cursor < arr.length) {
        let curr = queue.shift();

        let left = arr[cursor];
        let right = arr[cursor+1];

        if(left != 'x') {
            let leftNode = new TreeNode(left);
            curr.left = leftNode;
            queue.push(leftNode);
        }

        if(right != 'x') {
            let rightNode = new TreeNode(right);
            curr.right = rightNode;
            queue.push(rightNode);
        }

        cursor += 2;
    }
    return root;
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@mo660
mo660 commented 5 hours ago
思路
评论区大哥用istringstream的方法。。。

代码
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (nullptr == root)
            return "#";
        return to_string(root->val) + " " + serialize(root->left) + " " + serialize(root->right);
    }

    TreeNode* mydeserialize(istringstream &ss ){
        string tmp;
        ss >> tmp;
        if (tmp == "#")
            return nullptr;
        TreeNode* node = new TreeNode(stoi(tmp));
        node->left = mydeserialize(ss);
        node->right = mydeserialize(ss);
        return node;
    }
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream ss(data);
        return mydeserialize(ss);
    }
};
@jackgaoyuan
jackgaoyuan commented 5 hours ago
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return "#"
	}
	return strconv.Itoa(root.Val) + "," + this.serialize(root.Left) + "," + this.serialize(root.Right)
}


func dfs(valsPtr *[]string) *TreeNode {
	val := (*valsPtr)[0]
	*valsPtr = (*valsPtr)[1:]
	if val == "#" {
		return nil
	}
	valInt, _ := strconv.Atoi(val)
	node := &TreeNode{Val: valInt}
	node.Left = dfs(valsPtr)
	node.Right = dfs(valsPtr)
	return node
}

func (this *Codec) deserialize(data string) *TreeNode {
	vals := strings.Split(data, ",")
	return dfs(&vals)
}
@Alexno1no2
Alexno1no2 commented 2 hours ago
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(dataList):
            val = dataList.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = dfs(dataList)
            root.right = dfs(dataList)
            return root

        dataList = data.split(',')
        return dfs(dataList)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
@zcytm3000
zcytm3000 commented 1 hour ago
class Codec:

def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return 'None'
    return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
    
def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    def dfs(dataList):
        val = dataList.pop(0)
        if val == 'None':
            return None
        root = TreeNode(int(val))
        root.left = dfs(dataList)
        root.right = dfs(dataList)
        return root

    dataList = data.split(',')
    return dfs(dataList)
@catkathy
catkathy commented 34 minutes ago
Code
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(dataList):
            val = dataList.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = dfs(dataList)
            root.right = dfs(dataList)
            return root

        dataList = data.split(',')
        return dfs(dataList)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
@cyk1337
cyk1337 commented 22 minutes ago
def serialize(self, root):
"""Encodes a tree to a single string.

:type root: TreeNode
:rtype: str
"""
if not root:
    return 'None'
return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
def deserialize(self, data):
"""Decodes your encoded data to tree.

:type data: str
:rtype: TreeNode
"""
def dfs(dataList):
    val = dataList.pop(0)
    if val == 'None':
        return None
    root = TreeNode(int(val))
    root.left = dfs(dataList)
    root.right = dfs(dataList)
    return root

dataList = data.split(',')
return dfs(dataList)
@GuitarYs
GuitarYs commented 21 minutes ago
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        # 使用preorder遍历序列化二叉树
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append('null')
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        # 将序列化结果解析成列表
        vals = data.split(',')
        # 使用DFS递归构建二叉树
        def dfs():
            val = vals.pop(0)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# 测试样例
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
s = codec.serialize(root)
print(s)  # 序列化结果: "1,2,null,null,3,4,null,null,5,null,null,"
new_root = codec.deserialize(s)
print(new_root.val)  # 重构后的根节点值: 1
print(new_root.left.val)  # 重构后的左子树根节点值: 2
print(new_root.right.val)  # 重构后的右子树根节点值: 3
print(new_root.right.left.val)  # 重构后的右子树的左子树根节点值: 4
print(new_root.right.right.val)  # 重构后的右子树的右子树根节点值: 5
