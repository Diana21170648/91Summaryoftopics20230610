【Day 50 】2023-07-29 - 695. 岛屿的最大面积 #52
Open
azl397985856 opened this issue 11 hours ago · 1 comment
Comments
@azl397985856
azl397985856 commented 11 hours ago
695. 岛屿的最大面积
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/max-area-of-island/

前置知识
暂无

题目描述
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 （代表土地） 构成的组合，
这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。（如果没有岛屿，则返回面积为 0 。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵，返回 0。

 
注意：给定的矩阵 grid 的长度和宽度都不超过 50
@azl397985856 azl397985856 added BFS DFS 50 labels 11 hours ago
@Diana21170648
Diana21170648 commented now
思路
BFS

代码
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        ans=0
        n=len(grid[0])
        fangxiang=[(1,0),(-1,0),(0,1),(0,-1)]#表示上下左右
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:#如果当前是陆地，开始bfs
                    queue=deque([(i,j)])#当做元组添加进去
                    grid[i][j]=0#标记为已访问，下一步开始岛屿面积加一
                    area=1

                    while queue:#队列不为空，就证明bfs还没有遍历结束
                        x,y=queue.popleft()
                        for fxx,fxy in fangxiang:
                            newx,newy=x+fxx,y+fxy
                            if 0<=newx<m and 0<=newy<n and grid[newx][newy]==1:
                                queue.append((newx,newy))
                                grid[newx][newy]=0
                                area+=1
                    ans=max(ans,area)
        return ans
复杂度分析

时间复杂度：O(M*N)
空间复杂度：O(M*N)
