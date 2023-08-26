【Day 78 】2023-08-26 - 1319. 连通网络的操作次数 #80
Open
azl397985856 opened this issue 16 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
1319. 连通网络的操作次数
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/

前置知识
暂无

题目描述
用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。



示例 1：



输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
示例 2：



输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
输出：2
示例 3：

输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
输出：-1
解释：线缆数量不足。
示例 4：

输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
输出：0


提示：

1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
没有重复的连接。
两台计算机不会通过多条线缆连接。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
并查集/dfs

代码
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        root=[i for i in range(n)]
        def find(p):
            while p !=root[p]:
                root[p]=root[root[p]]#路径压缩
                p=root[p]#便于下一次循环操作
            return p
        def union(p,q):
            root[find(p)]=find(q)
        
        rongyu=0
        for connec in connections:
            a,b=connec
            if find(a) !=find(b):
                union(a,b)
            else:
                rongyu+=1#a和b处于一个集合，那么冗余的线就多一根

        diff_root=set()
        for i in range(n):
            diff_root.add(find(i))
        return len(diff_root)-1 if rongyu>=len(diff_root)-1 else -1
        #缺线缆则返回-1   
复杂度分析

时间复杂度：O(logx)，其中 x 为查找的次数，O(logy)，y为连接的次数。
空间复杂度：O(n),n为计算机的个数

@azl397985856 azl397985856 added 并查集 78 labels 16 hours ago
@Beanza
Beanza commented 15 hours ago
class Solution:
def makeConnected(self, n: int, connections: List[List[int]]) -> int:
root = [i for i in range(n)]

    def find(p):
        while p != root[p]:
            root[p] = root[root[p]]
            p = root[p]

        return p

    def union(p, q):
        root[find(p)] = find(q)

    have = 0
    for connec in connections:
        a, b = connec
        if find(a) != find(b):
            union(a, b)
        else:
            have += 1

    diff_root = set()
    for i in range(n):
        diff_root.add(find(i))
@GuitarYs
GuitarYs commented 3 hours ago
class Solution:
    def makeConnected(self, n: int, connections):
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        count = n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            nonlocal count
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                count -= 1
        for connection in connections:
            union(connection[0], connection[1])
        return count - 1

