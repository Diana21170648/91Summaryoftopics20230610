【Day 76 】2023-08-24 - 547. 省份数量 #78
Open
azl397985856 opened this issue 12 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 12 hours ago
547. 省份数量
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/number-of-provinces/

前置知识
暂无

题目描述
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

示例 1：



输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
示例 2：


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
 

提示：

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

@Diana21170648
Diana21170648 commented 1 minute ago
思路
DFS
BFS
并查集

代码
class UF:
    def __init__(self,n)->None:
        self.parent={i: i for i in range(n)}
        self.size=n
    
    def find(self,i):
        if self.parent[i] !=i:
            self.parent[i]=self.find(self.parent[i])
        return self.parent[i]
    
    def connect(self,i,j):#如果同一个子集相连，并查集数量不变，如果属于不同的自己相连，那么数量需要减一
        root_i,root_j=self.find(i),self.find(j)
        if root_i !=root_j:
            self.size-=1
            self.parent[root_i]=root_j

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        uf=UF(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.connect(i,j)
        return uf.size
复杂度分析

时间复杂度：O(NlogN)，其中 N 为矩阵M的大小。
空间复杂度：O(N)

@azl397985856 azl397985856 added 并查集 76 labels 12 hours ago
@freesan44
freesan44 commented 3 hours ago
class Solution {
    func findCircleNum(_ isConnected: [[Int]]) -> Int {
        var visited = Set<Int>()
        var provinces = 0
        
        func dfs(_ i: Int) {
            visited.insert(i)
            for j in 0..<isConnected[i].count {
                if !visited.contains(j) && isConnected[i][j] == 1 {
                    dfs(j)
                }
            }
        }
        
        for i in 0..<isConnected.count {
            if !visited.contains(i) {
                dfs(i)
                provinces += 1
            }
        }
        
        return provinces
    }
}
@GuitarYs
GuitarYs commented 2 hours ago
class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for city in range(n):
            if not visited[city]:
                dfs(city)
                count += 1

        return count
