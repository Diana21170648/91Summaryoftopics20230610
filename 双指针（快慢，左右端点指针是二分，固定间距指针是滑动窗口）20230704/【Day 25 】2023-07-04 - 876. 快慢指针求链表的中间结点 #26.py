【Day 25 】2023-07-04 - 876. 链表的中间结点 #26
Open
azl397985856 opened this issue 11 hours ago · 7 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
876. 链表的中间结点
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/middle-of-the-linked-list/

前置知识
暂无

题目描述
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

 

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
 

提示：

给定链表的结点数介于 1 和 100 之间。

@Diana21170648
Diana21170648 commented now
思路
需要输出中间节点后面所有的内容，所以用快慢指针，一个走一步，一个走两步，如果要输出中间节点就可以用左右端点指针，一个指向头，一个指向尾

代码
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #n=len(head)
        left=right=head
        #right=tail
        while right and right.next:
            left=left.next
            right=right.next.next
        return left
复杂度分析

时间复杂度：O(N)，其中 N 为链表长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 双指针 链表 25 labels 11 hours ago
@GuitarYs
GuitarYs commented 9 hours ago
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# 测试样例
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = middleNode(head)
while result:
    print(result.val)
    result = result.next
@freesan44
freesan44 commented 3 hours ago
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func middleNode(_ head: ListNode?) -> ListNode? {
        var slow = head
        var fast = head
        
        while fast != nil && fast?.next != nil {
            fast = fast?.next?.next
            slow = slow?.next
        }
        
        return slow
    }
}
@zhaoygcq
zhaoygcq commented 1 hour ago
思路
快慢指针：
快指针一次走两步
慢指针一次走一步

代码
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    if(!head) return head;
    let slow = fast = head;
    while(fast && fast.next) {
        fast = fast.next.next;
        slow = slow.next;
    }
    return slow;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
@SoSo1105
SoSo1105 commented 38 minutes ago
思路
定义快慢指针，同时从头结点开始向后遍历，快指针每次走两步，慢指针每次走一步，当快指针走到末尾结点时，慢指针恰好走到中间结点。

代码
class Solution:
    def middleNode(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
复杂度分析

时间复杂度：O(N)
空间复杂度：O(1)
@954545647
954545647 commented 14 minutes ago
easy!

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function (head) {
  if (!head) return head
  let slow = fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
};
@jackgaoyuan
jackgaoyuan commented 10 minutes ago
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }
    return slow
}
