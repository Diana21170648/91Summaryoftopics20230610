【Day 87 】2023-09-04 - 23.合并 K 个排序链表 #89
Open
azl397985856 opened this issue 11 hours ago · 1 comment
Comments
@azl397985856
azl397985856 commented 11 hours ago
23.合并 K 个排序链表
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/merge-k-sorted-lists/

前置知识
堆
链表
分而治之
题目描述
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
1->4->5,
1->3->4,
2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
@azl397985856 azl397985856 added 链表 87 labels 11 hours ago
@Diana21170648
Diana21170648 commented 48 minutes ago
思路
归并排序

代码
#先合并两个，两两合并最后再合到一起
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

时间复杂度：O(Nlogk)，其中 N 为链表所有节点的个数，logk为归并排序的层数。
空间复杂度：O(logk)

思路
堆（优先队列）

代码
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#头元素入优先队列，然后比较最小值进入链表，并取min.next入优先队列，重复直到优先队列为空，得到的链表即为排序后的结果

from queue import PriorityQueue
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def mergeKLists(self,lists):
        queue=PriorityQueue()
        #创建一个虚拟头结点，避免重复操作
        fakeHead=ListNode(0)
        temp=fakeHead#结果链表
        count=0

        for head in lists:
            if head:
                queue.put((head.val,count,head))
                count+=1
        
        #优先队列不为空，需要持续执行
        while not queue.empty():
            val,_,cur=queue.get()
            if cur.next:
                queue.put((cur.next.val,count,cur.next))
                count+=1
            temp.next=cur
            temp=temp.next
        return fakeHead.next
            
复杂度分析

时间复杂度：O(Nlogk)，其中 N 为链表节点总数，logk为堆（优先队列插入删除）的复杂度。
空间复杂度：O(k)，k是链表个数

作者：Diana21170648
链接：https://leetcode.cn/problems/merge-k-sorted-lists/solutions/2425435/23dui-gui-bing-pai-xu-he-bing-kge-pai-xu-7qcl/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
