【Day 11 】2023-06-20 - 142. 环形链表 II #12
Open
azl397985856 opened this issue 16 hours ago · 9 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
142. 环形链表 II
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/linked-list-cycle-ii/

前置知识
暂无

题目描述
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？
@azl397985856 azl397985856 added 双指针 链表 11 labels 16 hours ago
@bi9potato

@Diana21170648
Diana21170648 commented now
思路
法一遍历链表，用哈希表存节点，第一次遍历两次的节点就是环的入口
法二用双指针，快走两步，慢走一步，如果慢=快，证明有环，慢从头开始，快从相遇点开始，下次相遇点即为环的入口
以下内容使用法二

代码
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        x=None
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                x=fast
                break
        if not x:
            return None
        slow=head
        while slow !=x:
            slow=slow.next
            x=x.next
        return slow
复杂度分析

时间复杂度：O(N)，其中 N 为链表的长度。
空间复杂度：O(1)，使用快慢指针，未占用其它空间

bi9potato commented 14 hours ago
Approach
Fast and Slow Pointers

Code
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {

        ListNode pSlow = head;
        ListNode pFast = head;

        while (pFast != null && pFast.next != null ) {
            pSlow = pSlow.next;
            pFast = pFast.next.next;

            if (pFast == pSlow) break;
        }

        if (pFast == null || pFast.next == null) {
            return null;
        }

        pSlow = head;
        while (pSlow != pFast) {
            pSlow = pSlow.next;
            pFast = pFast.next;
        }

        return pSlow;
        
    }
}
Complexity Analysis
Time 
Spce 
@zhaoygcq
zhaoygcq commented 7 hours ago
思路
使用一个Map来记录已经遍历过的节点，如果在遍历过程中，又遇到了之前遍历的节点，那就认为该节点为环形链表的头节点。

代码
var detectCycle = function(head) {
    let map = new WeakMap();
    let curr = head;
    while(curr) {
        if(!map.has(curr)) {
            map.set(curr, 1);
        } else {
            return curr;
        }
        curr = curr.next;
    }
    return null;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@hengistchan
hengistchan commented 4 hours ago
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        while(head) {
            if(!less<ListNode *>()(head, head->next)) {
                return head->next;
            }
            head = head->next;
        }
        return nullptr;
    }
};
@RocJeMaintiendrai
RocJeMaintiendrai commented 3 hours ago
public class Solution {
public ListNode detectCycle(ListNode head) {
ListNode slow = head, fast = head;
while(fast != null && fast.next != null) {
slow = slow.next;
fast = fast.next.next;
if(slow == fast) break;
}
if(fast == null || fast.next == null) {
return null;
}
while(head != slow) {
head = head.next;
slow = slow.next;
}
return head;
}
}

@RanDong22
RanDong22 commented 2 hours ago
typescript

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function detectCycle(head: ListNode | null): ListNode | null {
  const retNode = new ListNode();
  retNode.next = head;
  let front = retNode,
    end = retNode;
  while (end && end.next) {
    front = front.next!;
    end = end.next?.next!;
    if (front === end) {
      break;
    }
  }
  if (!end || !end.next) {
    return null;
  }
  front = retNode;
  while (front !== end) {
    front = front.next!;
    end = end.next!;
  }
  return end;
}
@catkathy
catkathy commented 44 minutes ago
思路
快慢指针

Code
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        # find the meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if found, break the loop
            if slow == fast:
                break
            # if not, return null
        else:
            return None


        # Find the node where the cycle begins
        # Move the slow pointer to the head of the linked list
        slow = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast # or return slow (starting point)

        # Move both pointers at the same pace until they meet again
@GuitarYs
GuitarYs commented 25 minutes ago
···python
class Solution(object):
def detectCycle(self, head):
"""
:type head: ListNode
:rtype: ListNode
"""
if not head or not head.next:
return None

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if not fast or not fast.next:
        return None
    
    ptr1, ptr2 = head, fast
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1
···

@zcytm3000
zcytm3000 commented 8 minutes ago
class Solution(object):
def detectCycle(self, head):
fast, slow = head, head
while True:
if not (fast and fast.next): return
fast, slow = fast.next.next, slow.next
if fast == slow: break
fast = head
while fast != slow:
fast, slow = fast.next, slow.next
return fast

