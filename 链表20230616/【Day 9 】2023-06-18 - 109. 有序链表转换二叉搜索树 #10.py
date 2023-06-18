【Day 9 】2023-06-18 - 109. 有序链表转换二叉搜索树 #10
Open
azl397985856 opened this issue 18 hours ago · 10 comments
Open
【Day 9 】2023-06-18 - 109. 有序链表转换二叉搜索树
#10
azl397985856 opened this issue 18 hours ago · 10 comments
Comments
@azl397985856
azl397985856 commented 18 hours ago
109. 有序链表转换二叉搜索树
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

前置知识
递归
二叉搜索树的任意一个节点，当前节点的值必然大于所有左子树节点的值。同理,当前节点的值必然小于所有右子树节点的值
题目描述
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

    0
   / \
 -3   9
 /   /
-10  5
@azl397985856 azl397985856 added 链表 二叉搜索树 9 labels 18 hours ago

@Diana21170648
Diana21170648 commented now
思路
用双指针解题

代码
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        pre,slow,fast=None,head,head
        while fast and fast.next:
            fast=fast.next.next
            pre=slow
            slow=slow.next
        if pre:
            pre.next=None
        node=TreeNode(slow.val)
        if slow==fast:
            return node
        node.left=self.sortedListToBST(head)
        node.right=self.sortedListToBST(slow.next)
        return node
复杂度分析

时间复杂度：O(nlogn)，其中 n为每一层的操作数，logn为二叉树的深度。
空间复杂度：O(logn)，logn为二叉树的深度


@Fuku-L
Fuku-L commented 15 hours ago
代码
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
    public TreeNode sortedListToBST(ListNode head) {
        // 递归+快慢指针
        return buildTree(head, null);
    }

    public TreeNode buildTree(ListNode left, ListNode right){
        if(left == right){
            return null;
        }
        ListNode mid = getMedian(left, right);
        TreeNode root = new TreeNode(mid.val);
        root.left = buildTree(left, mid);
        root.right = buildTree(mid.next, right);
        return root;
    }

    public ListNode getMedian(ListNode left, ListNode right){
        ListNode fast = left;
        ListNode slow = left;
        while(fast != right && fast.next != right){
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}
@Alexno1no2
Alexno1no2 commented 14 hours ago
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        slow , fast = head ,head
        pre = ListNode(-1)
        # newhead = TreeNode(-1)
        while slow and fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        newhead = TreeNode(slow.val)
        if pre:
            pre.next = None
        if slow == fast:
            return newhead
        newhead.left = self.sortedListToBST(head)
        newhead.right = self.sortedListToBST(slow.next)


        return newhead
@bi9potato
bi9potato commented 10 hours ago • 
Approach
Fast n slow pointers to get the middle node, then use BFS recursively.

Code
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
    public TreeNode sortedListToBST(ListNode head) {

        return dfs(head, null);
        
    }

    private TreeNode dfs(ListNode head, ListNode tail) {

        if (head == tail) {
            return null;
        }

        ListNode fast = head;
        ListNode slow = head;
        while (fast != tail && fast.next != tail) {
            fast = fast.next.next;
            slow = slow.next;
        }

        TreeNode root = new TreeNode(slow.val);
        root.left = dfs(head, slow);
        root.right = dfs(slow.next, tail);

        return root;

    }
}
Complexity Analysis
Time 
Spce 
@zhaoygcq
zhaoygcq commented 8 hours ago
思路
确定如何正确的定位中间节点： 快慢指针是一种办法，如果快指针一次走两步、慢指针一次走一步，
那快指针指向链表末尾时，慢指针正好在中间.

代码
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
function sortedListToBST (head) {
    if(!head) return head;
    let slow = fast = head;
    let slowPrev = null;
    while(fast && fast.next) {
        slowPrev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }

    let root = new TreeNode(slow.val);
    if(slowPrev) {
        slowPrev.next = null;
        root.left = sortedListToBST(head);
    }
    root.right = sortedListToBST(slow.next);
    return root;
};
复杂度分析

时间复杂度：O(logN)，其中 N 为数组长度。
空间复杂度：O(NlogN)
@acy925
acy925 commented 6 hours ago
代码
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        pre, slow, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if pre:
            pre.next = None
        node = TreeNode(slow.val)
        if slow == fast:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node

@wzbwzt
wzbwzt commented 2 hours ago
/*
思路：
快慢指针
前提：链表已经升序排序
根据高度平衡的二叉树原则，可以先选取中间节点作为根节点,左边的都为左节点，右边的都为右节点
对左右子链表再找中间节点,以此重复；
通过快慢指针找到中间节点

复杂度：
空间复杂度：空间复杂度为 O(logn)
时间复杂度：递归树的深度为 logn,每一层的基本操作数为 n,因此总的时间复杂度为O(nlogn)

*/

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedListToBST(head *ListNode) *TreeNode {
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return &TreeNode{Val: head.Val}
	}
	if head.Next.Next == nil {
		return &TreeNode{Val: head.Next.Val, Left: &TreeNode{Val: head.Val}}
	}

	var pre *ListNode
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		pre = slow
		slow = slow.Next
		fast = fast.Next.Next
	}
	root := &TreeNode{Val: slow.Val}
	root.Right = sortedListToBST(slow.Next)

	pre.Next = nil
	root.Left = sortedListToBST(head)

	return root

}
@GuitarYs
GuitarYs commented 2 hours ago
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # 寻找链表中点
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 将链表断开，分别构建左子树和右子树
        mid = slow.next
        slow.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root


# 示例
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

solution = Solution()
root = solution.sortedListToBST(head)

def printTree(root):
    if not root:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

printTree(root)
@catkathy
catkathy commented 1 hour ago
思路
快慢指针

Code
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head or not head.next:
            return TreeNode(head.val) if head else None
        
        dummy = ListNode(0)
        dummy.next = head
        slow, fast, prev = head, head, dummy

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        new_head = slow.next
        prev.next = None  
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(new_head)

        return root
复杂度分析：
Time: O(n)
Space: O(n)
@hengistchan
hengistchan commented 18 minutes ago
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
    public TreeNode sortedListToBST(ListNode head) {
        // 递归+快慢指针
        return buildTree(head, null);
    }

    public TreeNode buildTree(ListNode left, ListNode right){
        if(left == right){
            return null;
        }
        ListNode mid = getMedian(left, right);
        TreeNode root = new TreeNode(mid.val);
        root.left = buildTree(left, mid);
        root.right = buildTree(mid.next, right);
        return root;
    }

    public ListNode getMedian(ListNode left, ListNode right){
        ListNode fast = left;
        ListNode slow = left;
        while(fast != right && fast.next != right){
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}
