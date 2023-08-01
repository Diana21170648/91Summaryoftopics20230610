【Day 53 】2023-08-01 - Top-View-of-a-Tree #55
Open
azl397985856 opened this issue 11 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
Top-View-of-a-Tree
入选理由
暂无

题目地址
https://binarysearch.com/problems/Top-View-of-a-Tree

前置知识
暂无

题目描述
Given a binary tree root, return the top view of the tree, sorted left-to-right.

Constraints

n ≤ 100,000 where n is the number of nodes in root


@Diana21170648
Diana21170648 commented 1 minute ago
思路
BFS双端队列插入删除方便
哈希表存储未被占用的值

代码
from collections import deque
class Solution:
    def solve(self,root):
        queue=collections.deque([root,0])
        seen={}
        while queue:
            cur,pos=queue.popleft()
            if pos not in seen:
                seen(pos)=cur.value
            if cur.left:
                queue.append(cur.left,pos-1)
            if cur.right:
                queue.append(cur,right,pos+1)
        return list(map(lambda x:x[1],sorted(seen.items(),key=lambda x:x[0])))#按键值排序的value值
复杂度分析

时间复杂度：O(NlogN)，其中 N 为二叉树节点个数，使用了排序。
空间复杂度：O(N)，使用了哈希表

@azl397985856 azl397985856 added BFS 哈希表 树 53 labels 11 hours ago
@HuiyingC
HuiyingC commented 15 minutes ago
思路

Tag: #Tree, #BFS
in-order遍历tree
tree 映射至 x 轴 >> 坐标记录左右信息
要什么样的view都可✅
Code
def solve(self, root):
    q = collections.deque([(root, 0)])
    d = {}
    while q:  #BFS
        node, pos = q.popleft()
        if pos not in d:
            d[pos] = node.val
        if node.left:
            q.append((node.left, pos - 1))
        if node.right:
            q.append((node.right, pos + 1))

    return list(map(lambda x:x[1], sorted(d.items(), key=lambda x: x[0]))) #以 node pos、入队顺序依次排序
Complexity
Time : O(nlgn) << sorted()
Space: O(n)


