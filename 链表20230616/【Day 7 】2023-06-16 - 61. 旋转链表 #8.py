【Day 7 】2023-06-16 - 61. 旋转链表 #8
Open
azl397985856 opened this issue 20 hours ago · 15 comments
Open
【Day 7 】2023-06-16 - 61. 旋转链表
#8
azl397985856 opened this issue 20 hours ago · 15 comments
Comments
@azl397985856
azl397985856 commented 20 hours ago
61. 旋转链表
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/rotate-list/

前置知识
求单链表的倒数第 N 个节点
题目描述
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

@Diana21170648
Diana21170648 commented 1 minute ago
思路
思考：如果是个环的话就好办了，用next()指针,需要考虑当k大于链表长度的时候移出链表尾的情况，所以先对k2移动做了处理

代码
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:#判断链表是否为空
            k1=head
            k2=head
            count=1#记录链表长度
            num=0#记录已经旋转的节点数
            while num<k:
                if k2.next:#如果k2没有到结尾，则继续后移
                #需要现将count+1，再移动k2，否则count少一位
                    count+=1
                    k2=k2.next
                else:
                    k=k%count#如果k的值大于链表的长度count,那么我们只需要将链表旋转count次就可以实现相同的效果
                    num=-1#末尾的索引
                    k2=head
            #一个循环结束，继续下一个循环
                num+=1
            while k2.next:#k1和k2同事移动，直到k2到链表尾部
                k1=k1.next
                k2=k2.next
            #如果k1和k2没有连着，那k2到达尾部时，k1之后还有元素，则将k1和之后的元素断开，此时k1就是链表尾部，然后保存下一个节点为cur
            if k1.next:
                cur=k1.next
            else:
                return head
            #k2指向原链表的头部，把k1断开后保存的cur当做新的链表头
            k1.next=None
            k2.next=head
            return cur
复杂度分析

时间复杂度：O(N)，其中 N 为链表长度。
空间复杂度：O(1)，没有占用其余空间，O（1）复杂度

@azl397985856 azl397985856 added 链表 7 labels 20 hours ago
@bi9potato
bi9potato commented 18 hours ago
Approach
Rotate the last k nodes (len of linked list is k) to the front.

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
    public ListNode rotateRight(ListNode head, int k) {

        if (head == null) return head;

        ListNode old_tail = head;
        int len = 1;
        while (old_tail.next != null) {
            len++;
            old_tail = old_tail.next;
        }
        // System.out.println(len);


        ListNode new_tail = head;
        int idx = len - k % len;
        // System.out.println(idx);
        for (int i = 1; i < idx; i++) {
            new_tail = new_tail.next;
        }
        // System.out.println(new_tail.val);

        old_tail.next = head;
        head = new_tail.next;
        new_tail.next = null;

        return head;

        
    }
}
Complexity Analysis
Time 
Spce 
@snmyj
snmyj commented 13 hours ago
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
         ListNode *cur=head,*rear,*newh;
         if(head==nullptr||k==0||head->next==nullptr) return head;

         int cnt=0;
         while(cur!=nullptr){
             cnt++;
            
             cur=cur->next;
         }
         cur=head;
         k=k%cnt;
         if(k==0) return head;
         int t=0;
         while(1){
             t++;
             if(t==cnt-k){
                 newh=cur->next;
                 rear=cur;
                 cur=cur->next;
                 rear->next=nullptr;
                 continue;
            }
             if(t==cnt){
                 cur->next=head;
                 break;
             }
             cur=cur->next;
         }
         

         return newh;
    }
};

t：o(n);
@SoSo1105
SoSo1105 commented 13 hours ago
思路
1.用快慢指针确定旋转后链表的头节点
若链表的长度为n，让快指针先走k%n步，然后快慢指针同时向前走，直到快指针的next为空，此时慢指针的next为旋转后链表的头节点
2.移花接木
快指针的next指向原链表的头节点head
head指向慢指针的next，作为新链表的头节点返回
断掉慢指针和head之间的链，否则会形成环

代码
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fast, slow = head, head
        # 找到fast的起始节点
        def findStart(fast, k):
            length = 0
            while k>0:
                k -= 1
                length += 1
                fast = fast.next
                if not fast:
                    fast = head                                    
                    k = k % length                    
                    return findStart(fast, k)
            return fast
                   
        fast = findStart(fast, k)
         
        while fast and fast.next:           
            fast = fast.next
            slow = slow.next
   
        fast.next = head
        head = slow.next
        slow.next = None
        return head
复杂度分析

时间复杂度：O(N)
空间复杂度：O(1)
@freesan44
freesan44 commented 12 hours ago
思路
快慢指针

代码
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
    func rotateRight(_ head: ListNode?, _ k: Int) -> ListNode? {
        guard let head = head else { return nil }
        var p1: ListNode? = head
        var p2: ListNode? = head
        var count = 1
        var i = 0
        var k = k

        while i < k {
            if let next = p2?.next {
                count += 1
                p2 = next
            } else {
                k = k % count
                i = -1
                p2 = head
            }
            i += 1
        }

        while p2?.next != nil {
            p1 = p1?.next
            p2 = p2?.next
        }

        if let next = p1?.next {
            let tmp = next
            p1?.next = nil
            p2?.next = head
            return tmp
        } else {
            return head
        }
    }
}
@zhaoygcq
zhaoygcq commented 11 hours ago
思路
旋转链表，将每个节点向右移动k个位置 => 将链表的后len - k个节点当作链表的起始节点：
[1,2,3,4,5] k = 2;
=>
[1,2,3] -> [4,5]
=>
[4,5] -> [1,2,3]
为了实现上面的效果，有以下步骤：

获取当前链表长度(循环) len
判断当前是否需要移动，如果 k % len === 0;那就不需要移动
使用指针到 len - (k % len) - 1的位置，即示例中值为3的节点位置。
取出需要放到起始位置的节点[4,5],并将原有的头节点添加到节点值为5的节点之后。
代码
var rotateRight = function(head, k) {
    let len = 0;
    let curr = head;
    if(!head || !k) return head;
    while(curr) {
        len++;
        curr = curr.next;
    }
    let dis = k % len;
    if(!dis) return head;
    let runLen = len - dis - 1;
    let end = head;
    while(runLen > 0) {
        end = end.next;
        runLen--;
    }
    let newHead = end.next;
    let next = newHead;
    end.next = null;
    while(next.next) {
        next = next.next;
    }
    next.next = head;
    return newHead;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
@GuitarYs
GuitarYs commented 6 hours ago
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: ListNode, k: int) -> ListNode:
    # 处理特殊情况
    if head is None or head.next is None or k == 0:
        return head

    # 计算链表长度，同时将链表首尾相连
    n, tail = 1, head
    while tail.next:
        n += 1
        tail = tail.next
    tail.next = head

    # 计算实际要移动的步数
    k %= n

    # 找到新的头结点和尾结点
    new_tail = head
    for _ in range(n - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # 断开链表，返回新的头结点
    new_tail.next = None
    return new_head


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

k1 = 2
print("输入：", end="")
p1 = head1
while p1:
    print(p1.val, "->", end=" ")
    p1 = p1.next
print("NULL, k =", k1)

new_head1 = rotateRight(head1, k1)

print("输出：", end="")
p1 = new_head1
while p1:
    print(p1.val, "->", end=" ")
    p1 = p1.next
print("NULL")
print()

head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)

k2 = 4
print("输入：", end="")
p2 = head2
while p2:
    print(p2.val, "->", end=" ")
    p2 = p2.next
print("NULL, k =", k2)

new_head2 = rotateRight(head2, k2)

print("输出：", end="")
p2 = new_head2
while p2:
    print(p2.val, "->", end=" ")
    p2 = p2.next
@wzbwzt
wzbwzt commented 6 hours ago
/*
思路：
快慢指针
eg. A -> B -> C -> D -> E 右移 2 位 D-E-A-B-C
原则：不管移动多少，节点之间的相对位置是不变的
规则：移动k位，倒数第k位会移动到首位,即D会移动到head，倒数第K+1位会移动到last
注意：移动k位和移动k%len效果等同
过程：通过快慢指针回去倒数第K+1个节点

复杂度：
时间复杂度：节点最多只遍历两遍，时间复杂度为 O(n)
空间复杂度：未使用额外的空间，空间复杂度 O(1)
*/

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return nil
	}
	length := 0
	c := head
	for c != nil {
		length++
		c = c.Next
	}
	k = k % length
	if k == 0 {
		return head
	}
	var slow, fast = head, head
	for i := 0; i < k+1; i++ {
		fast = fast.Next
	}
	for fast != nil {
		fast = fast.Next
		slow = slow.Next
	}
	next := slow.Next
	slow.Next = nil
	out := next
	for next.Next != nil {
		next = next.Next
	}
	next.Next = head

	return out
}
@954545647
954545647 commented 5 hours ago
var rotateRight = function (head, k) {
  if (k === 0 || !head || !head.next) return head
  let len = 1;
  let temp = head;
  while (temp && temp.next) {
    temp = temp.next;
    len++
  }
  temp.next = head; // 将链表形成环
  temp = head;
  // 找到最后一个节点断开即可
  let last = len - k % len - 1;
  while (last) {
    temp = temp.next;
    last--;
  }
  const first = temp.next;
  temp.next = null;
  return first
};
@qiaojunch
qiaojunch commented 4 hours ago • 
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        #connect tail to head
        cur= head
        length =1
        while cur.next:
            cur = cur.next
            length+=1 
        cur.next = head

        #move to new head
        k= length - (k%length)
        while k>0:
            cur=cur.next
            k-=1

        #disconnect and return new head
        newhead = cur.next
        cur.next=None
        return newhead
analyze
Time: o(n)
Space: o(1)

@qiaojunch
qiaojunch commented 4 hours ago
update

@huizsh
huizsh commented 4 hours ago • 
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null) return head;
        int count = 0;
        ListNode now = head;
        while(now != null){
            now = now.next;
            count++;
        }
        k = k % count;
        ListNode slow = head, fast = head;
        while(fast.next != null){
            if(k-- <= 0){
                slow = slow.next;
            }
            fast = fast.next;
        }
        fast.next = head;
        ListNode res = slow.next;
        slow.next = null;
        return res;
    }
}
@catkathy
catkathy commented 3 hours ago
Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
    

        num_nodes = 0
        node = head
        while node is not None:
            num_nodes += 1
            node = node.next
        
        # Step 2: Calculate effective rotation
        k = k % num_nodes
        
        # Step 3: Check if rotation is unnecessary
        if k == 0:
            return head
        
        # Step 4: Find the (k+1)-th node from the end
        fast = head
        slow = head
        for _ in range(k):
            fast = fast.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        dummy = slow.next
        slow.next = None
        fast.next = head
        
        return dummy
@mo660
mo660 commented 3 hours ago
思路
先遍历链表，求出size，并记录尾指针。找到链表断开的位置n = size - (k % size);断开链表，头部接到尾部后面

代码
class Solution
{
public:
    ListNode *rotateRight(ListNode *head, int k)
    {
        if (nullptr == head)
            return nullptr;
        int size = 0;
        ListNode *tail = NULL;
        for (ListNode *next = head; next != NULL; next = next->next)
        {
            size++;
            if (next->next == nullptr)
                tail = next;
        }
        int n = size - (k % size);
        if (n == size)
            return head;
        ListNode *res = head;
        int count = 1;
        while (count != n)
        {
            res = res->next;
            count++;
        }
        ListNode *tmp = res;
        res = res->next;
        tmp->next = nullptr;
        tail->next = head;
        return res;
    }
};
@Alexno1no2
Alexno1no2 commented 11 minutes ago
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next: 
            return head
        # 求链表长度
        _len = 0
        cur = head
        while cur:
            _len += 1
            cur = cur.next
        # 对长度取模
        k %= _len
        if k == 0: 
            return head
        # 快慢指针 让 fast 先向后走 k 步
        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1
        # 继续往后走
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 新链表的头newHead，也就是倒数第 k 个节点
        newHead = slow.next
        # 将倒数第 k + 1 个节点 和 倒数第 k 个节点断开
        slow.next = None
        # 让最后一个节点指向原始链表的头
        fast.next = head
        return newHead
