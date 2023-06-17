【Day 8 】2023-06-17 - 24. 两两交换链表中的节点 #9
Open
azl397985856 opened this issue 18 hours ago · 8 comments
Open
【Day 8 】2023-06-17 - 24. 两两交换链表中的节点
#9
azl397985856 opened this issue 18 hours ago · 8 comments
Comments
@azl397985856
azl397985856 commented 18 hours ago
24. 两两交换链表中的节点
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/swap-nodes-in-pairs/

前置知识
链表的基本知识
题目描述
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1：
image

输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
 

提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
@azl397985856 azl397985856 added 链表 8 labels 18 hours ago
@yzhyzhyzh123

@Diana21170648
Diana21170648 commented 1 minute ago
思路
递归

代码
Python3 Code:

class Solution:
   def swapPairs(self, head: ListNode) -> ListNode:
       if not head or not head.next: return head

       next = head.next
       head.next = self.swapPairs(next.next)
       next.next = head

       return next
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)

yzhyzhyzh123 commented 17 hours ago
代码
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode pre = new ListNode(0);
        pre.next = head;
        ListNode temp = pre;
        while(temp.next != null && temp.next.next != null) {
            ListNode start = temp.next;
            ListNode end = temp.next.next;
            temp.next = end;
            start.next = end.next;
            end.next = start;
            temp = start;
        }
        return pre.next;
    }
}
复杂度
时间复杂度O(n)

@bi9potato
bi9potato commented 16 hours ago
Approach
dummy node

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
class Solution {
    public ListNode swapPairs(ListNode head) {

        ListNode dummy = new ListNode();
        dummy.next = head;

        ListNode node = dummy;
        while (node != null && node.next != null && node.next.next != null) {

            ListNode tmp = node.next;

            node.next = tmp.next;
            tmp.next = node.next.next;
            node.next.next = tmp;

            node = node.next.next;

        }

        return dummy.next;
        
    }
}
Complexity Analysis
Time 
Spce 
@zhaoygcq
zhaoygcq commented 8 hours ago
思路
每两两交换，使用两个指针；遍历链表，通过记录一个当前遍历的索引值是否为偶数，决定是否进行交换。
这种需要记录当前索引位置链表题，建议添加一个空头节点
注意点：

确定需要交换的两个节点
确定有哪些节点的指向关系
如：
1->2->3->4
dummy -> 1->2->3->4
交换1,2时:
2 -> 1
1 -> 3
dummy -> 2
所以，我们的两个指针的间隔需要为2；不然我们没办法完成第三步。
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
var swapPairs = function(head) {
    let dummy = new ListNode();
    dummy.next = head;
    let prev = dummy;
    let curr = dummy.next;
    if(!curr) return head;
    curr = curr.next;
    let count = 0;
    while(curr) {
        if(count % 2 === 0) {
            let next = curr.next;
            let prevOne = prev.next;
            prevOne.next = next;
            curr.next = prevOne;
            prev.next = curr;
            [curr, prevOne] = [prevOne, curr];
        }
        curr = curr.next;
        prev = prev.next;
        count++;
    }
    return dummy.next;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
@snmyj
snmyj commented 7 hours ago
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
         if(head==nullptr||head->next==nullptr) return head;
         int cnt;
         ListNode *pre=new ListNode(-1),*cur=pre,*ptr1,*ptr2,*ptrnext;
         pre->next=head;
         while(cur->next!=nullptr&&cur->next->next!=nullptr){
           ptr1=cur->next;
           ptr2=cur->next->next;
           if(ptr2->next!=nullptr) {ptrnext=ptr2->next;
           cur->next=ptr2;
            ptr1->next=ptrnext;
           ptr2->next=ptr1;
          
           cur=ptr1;  }
           else{
             cur->next=ptr2;
             ptr2->next=ptr1;
             ptr1->next=nullptr;
             break;
           }
           
         }
        return pre->next;

    }
};
@freesan44
freesan44 commented 2 hours ago
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
    func swapPairs(_ head: ListNode?) -> ListNode? {
        guard let head = head, let next = head.next else {
        return head
    }

    let dummy = ListNode(-1, head)
    var prev: ListNode? = dummy
    var cur: ListNode? = prev?.next

    while cur != nil && cur?.next != nil {
        let nextNode = cur?.next
        cur?.next = nextNode?.next
        nextNode?.next = cur
        prev?.next = nextNode

        prev = cur
        cur = cur?.next
    }

    return dummy.next
    }
}
@catkathy
catkathy commented 1 hour ago
Code
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
    
        while prev.next is not None and prev.next.next is not None:
            temp = head.next.next
            prev.next = head.next
            head.next.next = head
            head.next = temp
            prev = head
            head = head.next
    
        return dummy.next
复杂度分析
Time: O(n)
Space: O(1)
@wzbwzt
wzbwzt commented 1 hour ago
/*
思路：
A->B->C->D
注意：对于一个head node可能改变的链表，可以通过虚拟一个空节点来指代；
两两交换时涉及到四个节点，prehead->A->B->C

交换步骤：

prehead->A->C
B->A
prehaed->B
迭代交换

复杂度：
时间复杂度: O(n)
空间复杂度：O(1)

*/

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	prehead := &ListNode{}
	prehead.Next = head

	pre := prehead
	cur := head
	for cur != nil && cur.Next != nil {
		next := cur.Next
		cur.Next = next.Next
		next.Next = cur
		pre.Next = next

		pre = cur
		cur = cur.Next
	}

	return prehead.Next
}

