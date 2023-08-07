【Day 59 】2023-08-07 - 688. “马”在棋盘上的概率 #61
Open
azl397985856 opened this issue 12 hours ago · 3 comments
Open
【Day 59 】2023-08-07 - 688. “马”在棋盘上的概率
#61
azl397985856 opened this issue 12 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 12 hours ago
688. “马”在棋盘上的概率
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/knight-probability-in-chessboard/

前置知识
动态规划
数组
题目描述
已知一个 NxN 的国际象棋棋盘，棋盘的行号和列号都是从 0 开始。即最左上角的格子记为 (0, 0)，最右下角的记为 (N-1, N-1)。 

现有一个 “马”（也译作 “骑士”）位于 (r, c) ，并打算进行 K 次移动。 

如下图所示，国际象棋的 “马” 每一步先沿水平或垂直方向移动 2 个格子，然后向与之相垂直的方向再移动 1 个格子，共有 8 个可选的位置。


现在 “马” 每一步都从可选的位置（包括棋盘外部的）中独立随机地选择一个进行移动，直到移动了 K 次或跳到了棋盘外面。

求移动结束后，“马” 仍留在棋盘上的概率。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
动态规划先确定八个方向，再分贝求概率，再得出结果

代码
class Solution:
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        directions=[[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1]]
        dp=[[0.0]*n for _ in range(n)]
        dp[row][col]=1.0
        for step in range(1,k+1):
            dp_temp=[[0.0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for direction in directions:
                        old_row=i-direction[0]
                        old_col=j-direction[1]
                        if 0<=old_row<n and 0<=old_col<n:
                            dp_temp[i][j]+=dp[old_row][old_col]*0.125
            dp=dp_temp
        res=0.0
        for i in range(n):
            for j in range(n):
                res+=dp[i][j]
        return res

复杂度分析

时间复杂度：O(k*N^2)，其中 N 为数组长度。
空间复杂度：O(N^2)


@azl397985856 azl397985856 added 动态规划 59 labels 12 hours ago
@freesan44
freesan44 commented 4 hours ago
class Solution {
    private let dir = [[-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1]]

    func knightProbability(_ N: Int, _ K: Int, _ r: Int, _ c: Int) -> Double {
        var dp = Array(repeating: Array(repeating: 0.0, count: N), count: N)
        dp[r][c] = 1

        for step in 1...K {

            var dpTemp = Array(repeating: Array(repeating: 0.0, count: N), count: N)

            for i in 0..<N {
                for j in 0..<N {
                    for direction in dir {

                        let lastR = i - direction[0]
                        let lastC = j - direction[1]
                        if lastR >= 0 && lastR < N && lastC >= 0 && lastC < N {
                            dpTemp[i][j] += dp[lastR][lastC] * 0.125
                        }
                    }
                }
            }

            dp = dpTemp
        }

        var res = 0.0

        for i in 0..<N {
            for j in 0..<N {
                res += dp[i][j]
            }
        }

        return res
    }
}
@GuitarYs
GuitarYs commented 2 hours ago
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1

        for _ in range(K):
            temp = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for d in directions:
                        nr, nc = i + d[0], j + d[1]
                        if 0 <= nr < N and 0 <= nc < N:
                            temp[nr][nc] += dp[i][j] / 8.0
            dp = temp
        prob = 0
        for i in range(N):
            for j in range(N):
                prob += dp[i][j]
        return prob
