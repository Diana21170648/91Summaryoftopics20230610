【Day 10 】2023-06-19 - 160. 相交链表 #11
Open
azl397985856 opened this issue 12 hours ago · 11 comments
Open
【Day 10 】2023-06-19 - 160. 相交链表
#11
azl397985856 opened this issue 12 hours ago · 11 comments
Comments
@azl397985856
azl397985856 commented 12 hours ago
160. 相交链表
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

前置知识
链表
双指针
题目描述
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：



题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

 

示例 1：




输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：




输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
 

提示：

listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]
 

进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？

@azl397985856 azl397985856 added 链表 双指针 10 labels 12 hours ago

@Diana21170648
Diana21170648 commented now
思路
法一用哈希表存储a，检查b是否在里面可以
法二用双指针

代码
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a,b=headA,headB
        while a !=b:
            if a:
                a=a.next
            else:
                a=headB
            if b:
                b=b.next
            else:
                b=headA
        return a
复杂度分析

时间复杂度：O(N)，其中 N 为链表长度。
空间复杂度：O(1)

@GuitarYs
GuitarYs commented 9 hours ago
# 链表节点的定义
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 计算链表A和链表B的长度
        lenA, lenB = 0, 0
        pA, pB = headA, headB
        while pA:
            lenA += 1
            pA = pA.next
        while pB:
            lenB += 1
            pB = pB.next

        # 让较长的链表先移动n-m步
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next

        # 同时移动两个指针，直到找到交点或达到链表尾部
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        # 没有交点，返回null
        return None


# 输入数据
intersectVal = 8
listA = ListNode(4)
listA.next = ListNode(1)
listA.next.next = ListNode(8)
listA.next.next.next = ListNode(4)
listA.next.next.next.next = ListNode(5)

listB = ListNode(5)
listB.next = ListNode(6)
listB.next.next = ListNode(1)
listB.next.next.next = listA.next.next

skipA = 2
skipB = 3

# 输出结果
solution = Solution()
intersection_node = solution.getIntersectionNode(listA, listB)
if intersection_node:
    print("Intersected at '{}'".format(intersection_node.val))
else:
    print("null")
@bi9potato
bi9potato commented 9 hours ago
Approach
Double pointer

Traverse original linkedlist first, then traverse the other linkedlist.

Code
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        ListNode pA = headA;
        ListNode pB = headB;

        while (pA != pB) {

            if (pA == null) {
                pA = headB;
            } else {
                pA = pA.next;
            }

            

            if (pB == null) {
                pB = headA;
            } else {
                pB = pB.next;
            }

            

        }

        return pA;
        
    }
}
Complexity Analysis
Time 
Spce 
@YizheWill
YizheWill commented 5 hours ago
def getIntersectionNode(headA, headB)
    a, b = headA, headB
    while a != b
        a = a ? a.next : headB
        b = b ? b.next : headA
    end
    return a
end
@SoSo1105
SoSo1105 commented 4 hours ago
思路
双指针

代码
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a!=b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
复杂度分析

时间复杂度：O(N)
空间复杂度：O(1)
@freesan44
freesan44 commented 3 hours ago
思路
双指针

代码
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func getIntersectionNode(_ headA: ListNode?, _ headB: ListNode?) -> ListNode? {
         var a = headA
    var b = headB
    
    while a !== b {
        a = a != nil ? a!.next : headB
        b = b != nil ? b!.next : headA
    }
    
    return a
    }
}
@zhaoygcq
zhaoygcq commented 3 hours ago
思路
首先根据链表的长度，确定两个链表需要进行比较的起点位置。之后各个节点依次比较

代码
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    let lenA = getLen(headA);
    let lenB = getLen(headB);

    if(lenA < lenB) {
        [headA, headB] = [headB, headA];
        [lenB, lenA] = [lenA, lenB];
    }

    let dis = lenA - lenB;
    let currA = headA;
    let currB = headB;
    while(dis--) {
        currA = currA.next;
    }

    while(currA && currB) {
        if(currB === currA) {
            return currB;
        }
        currA = currA.next;
        currB = currB.next;
    }
    return null;
};

function getLen(head) {
    let count = 0;
    let curr = head;
    while(curr) {
        curr = curr.next;
        count++;
    }
    return count;
}
复杂度分析

时间复杂度：O(logN)，其中 N 为数组长度。
空间复杂度：O(1)
@chang-you
chang-you commented 1 hour ago • 
"""
无限长度的问题应该可以这样来解决：
两个链表同时做反向操作，也就是reverse linked list。那么会遇到有以下两种情况：

两个链表不相交部分一样长，那么他们会在某一刻访问到同一个node，那么这个node之后就全一致。
    1.1 如果要恢复链表结构，再reverse一次即可
两个链表不想教部分不一样长，那么其中一个指针it_a会跑到另一个链表头部。此时, 让it_a做reverse list操作直到回到Head(A)，用it_b再次做reverse操作，it_a正常访问next，it_a和it_b指向同一个节点时候，就是交点。此时，链表也正好恢复了原始结构。
更数学化一点语言应该是这样：
假设两个list A，B不想交部分长度分别为M，N，满足M >= N, but we don't know the exact value of M or N.
if M == N，after M reverse op, there will be it_A == it_b and the common node is found;
if M > N, after N reverse op, it_b will be on common list. And after M+N reverse op, it_a will be at Head(B). And it_b will be M steps away from the common Node.
Now let it_a execute reverse op for M+N times and it_a will be back at Head(A), which is also M steps away from the common Node.
Now let it_b doing a reverse list op and it_a to visit the list. The two will meet at the common Node and the structure will be restored at this moment.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
@hjy-u
hjy-u commented 1 hour ago
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        if pA == None or pB == None:
            return None
        while (pA != pB):
            pA = pA.next if pA is not None else headB
            pB = pB.next if pB is not None else headA
        return pA
time: O(N)
space: O(1)

@hengistchan
hengistchan commented 1 hour ago
function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
  let a = headA, b = headB
  while(a != b) {
    a = a ? a.next : null
    b = b ? b.next : null
    if(a == null && b == null) return null
    if(a == null) {
      a = headB
    } 
    if(b == null) {
      b = headA
    }
  }
  return a
};
@wzbwzt
wzbwzt commented 7 minutes ago • 
/*
思路：
双指针
listA listB 从head开始遍历;因为长度可能不一样，所以首先需要消除长度差,可以listA 遍历完后，指针指向listB的head
同理B一样，那么双指针走过的路程也就相同,速度一样，路程一样，那么一定会同时到达终点，
此外如果相交的话，也就是存在后半程路程相同，那么AB指针相遇时，就是相交的点

类型环形跑道，一个在内侧，一个在外侧，总距离都是1000米，起点不同，但是最后冲刺的直线跑道是相同的

复杂度：
时间复杂度：O(n)
空间复杂度：O(1)
*/

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}

	pA := headA
	pB := headB

	for pA != pB {
		if pA == nil {
			pA = headB
		} else {
			pA = pA.Next
		}

		if pB == nil {
			pB = headA
		} else {
			pB = pB.Next
		}
	}
	return pA
}
