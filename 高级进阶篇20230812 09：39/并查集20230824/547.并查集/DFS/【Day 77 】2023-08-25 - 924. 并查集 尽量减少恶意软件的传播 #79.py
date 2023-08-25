【Day 77 】2023-08-25 - 924. 尽量减少恶意软件的传播 #79
Open
azl397985856 opened this issue 17 hours ago · 1 comment
Comments
@azl397985856
azl397985856 commented 17 hours ago
924. 尽量减少恶意软件的传播
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/minimize-malware-spread

前置知识
暂无

题目描述
在节点网络中，只有当 graph[i][j] = 1 时，每个节点 i 能够直接连接到另一个节点 j。

一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。

假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。

我们可以从初始列表中删除一个节点。如果移除这一节点将最小化 M(initial)， 则返回该节点。如果有多个节点满足条件，就返回索引最小的节点。

请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后可能仍然因恶意软件传播而受到感染。


示例 1：

输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
输出：0
示例 2：

输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
输出：0
示例 3：

输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
输出：1


提示：

1 < graph.length = graph[0].length <= 300
0 <= graph[i][j] == graph[j][i] <= 1
graph[i][i] == 1
1 <= initial.length < graph.length
0 <= initial[i] < graph.length
@azl397985856 azl397985856 added DFS 并查集 77 labels 17 hours ago
@Diana21170648
Diana21170648 commented now
思路
并查集
dfs

代码
class UF: 
    def __init__ (self):
        self.father={}
        self.size={}
    def find(self,x):
        self.father.setdefault(x,x)
        if x !=self.father[x]:
            self.father[x]=self.find(self.father[x])
        return self.father[x]
    def connect(self,x,y):
        fx,fy=self.find(x),self.find(y)
        if self.size.setdefault(fx,1)<self.size.setdefault(fy,1):
            self.father[fx]=fy
            self.size[fy]+=self.size[fx]
        elif fx!=fy:
            self.father[fy]=fx
            self.size[fx] +=self.size[fy]
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        uf=UF()
        for i in range(len(graph)):
            for j in range(i,len(graph)):
                if graph[i][j]:
                    uf.connect(i,j)
        initial.sort()
        max_size,index,fi=0,-1,[]
        cnt=collections.defaultdict(int)
        for init in initial:
            fi.append(uf.find(init))
            cnt[fi[-1]]+=1
        for i in range(len(initial)):
            if cnt[fi[i]]>1:
                continue
            if uf.size[fi[i]]>max_size:
                max_size=uf.size[fi[i]]
                index=initial[i]
        return index if index !=-1 else initial[0]


复杂度分析

时间复杂度：O(N*alpha（n）)，其中 N 为矩阵长度长度，n为按秩合并的次数。
空间复杂度：O(N)
