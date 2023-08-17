【Day 69 】2023-08-17 - 23. 合并 K 个排序链表 #71
Open
azl397985856 opened this issue 13 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 13 hours ago
23. 合并 K 个排序链表
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/merge-k-sorted-lists/

前置知识
链表
归并排序
题目描述

合并  k  个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6


@Diana21170648
Diana21170648 commented 1 minute ago
思路
先合并两个，两两合并最后再合到一起

代码
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)

        # basic cases
        if n == 0: return None
        if n == 1: return lists[0]
        if n == 2: return self.mergeTwoLists(lists[0], lists[1])

        # divide and conqure if not basic cases
        mid = n // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:n]))


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        c1, c2, c3 = l1, l2, res
        while c1 or c2:
            if c1 and c2:
                if c1.val < c2.val:
                    c3.next = ListNode(c1.val)
                    c1 = c1.next
                else:
                    c3.next = ListNode(c2.val)
                    c2 = c2.next
                c3 = c3.next
            elif c1:
                c3.next = c1
                break
            else:
                c3.next = c2
                break

        return res.next
复杂度分析

时间复杂度：O(knlogk)，其中 N 为数组长度。
空间复杂度：O(logk)

@azl397985856 azl397985856 added 分治 69 labels 13 hours ago
@Beanza
Beanza commented 3 hours ago
function mergeTwoLists(l1, l2) {
const dummyHead = {};
let current = dummyHead;
// l1: 1 -> 3 -> 5
// l2: 2 -> 4 -> 6
while (l1 !== null && l2 !== null) {
if (l1.val < l2.val) {
current.next = l1; // 把小的添加到结果链表
current = current.next; // 移动结果链表的指针
l1 = l1.next; // 移动小的那个链表的指针
} else {
current.next = l2;
current = current.next;
l2 = l2.next;
}
}

if (l1 === null) {
current.next = l2;
} else {
current.next = l1;
}
return dummyHead.next;
}

