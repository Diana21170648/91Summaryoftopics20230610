【Day 42 】2023-07-21 - 778. 水位上升的泳池中游泳 #44
Open
azl397985856 opened this issue yesterday · 7 comments
Comments
@azl397985856
azl397985856 commented yesterday
778. 水位上升的泳池中游泳
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/swim-in-rising-water

前置知识
暂无

题目描述
在一个 N x N 的坐标方格  grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为  t  时，此时雨水导致水池中任意位置的水位为  t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台  (N-1, N-1)？

示例 1:

输入: [[0,2],[1,3]]
输出: 3
解释:
时间为 0 时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
示例 2:

输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释:
0 1 2 3 4
24 23 22 21 5
12 13 14 15 16
11 17 18 19 20
10 9 8 7 6

最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的

提示:

2 <= N <= 50.
grid[i][j] 位于区间 [0, ..., N*N - 1] 内。

@Diana21170648
Diana21170648 commented now
思路
二分找左边界

代码
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        l, r = 0, max([max(vec) for vec in grid])
        seen = set()

        def test(mid, x, y):
            if x > len(grid) - 1 or x < 0 or y > len(grid[0]) - 1 or y < 0:
                return False
            if grid[x][y] > mid:
                return False
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return True
            if (x, y) in seen:
                return False
            seen.add((x, y))
            ans = test(mid, x + 1, y) or test(mid, x - 1,
                                              y) or test(mid, x, y + 1) or test(mid, x, y - 1)
            return ans
        while l <= r:
            mid = (l + r) // 2
            if test(mid, 0, 0):
                r = mid - 1
            else:
                l = mid + 1
            seen = set()
        return l
复杂度分析

时间复杂度：O(NlogM)，其中 N 为grid长度，M为grid最大值。
空间复杂度：O(N)

@azl397985856 azl397985856 added 二分 42 labels yesterday
@freesan44
freesan44 commented 15 hours ago
class Solution {
    func swimInWater(_ grid: [[Int]]) -> Int {
         var l = 0
        var r = grid.flatMap { $0 }.max() ?? 0
        var seen = Set<(Int, Int)>()

        func test(_ mid: Int, _ x: Int, _ y: Int) -> Bool {
            if x > grid.count - 1 || x < 0 || y > grid[0].count - 1 || y < 0 {
                return false
            }
            if grid[x][y] > mid {
                return false
            }
            if (x, y) == (grid.count - 1, grid[0].count - 1) {
                return true
            }
            if seen.contains((x, y)) {
                return false
            }
            seen.insert((x, y))
            let ans = test(mid, x + 1, y) || test(mid, x - 1, y) || test(mid, x, y + 1) || test(mid, x, y - 1)
            return ans
        }
        
        while l <= r {
            let mid = (l + r) / 2
            if test(mid, 0, 0) {
                r = mid - 1
            } else {
                l = mid + 1
            }
            seen = Set<(Int, Int)>()
        }
        
        return l
    }
}
@acy925
acy925 commented 12 hours ago
代码
class Solution:
    def swimInWater(self, grid: List[List[int]]):
        neighbors = {0:(0,0)}
        seen = set()
        time = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while True:
            if time not in neighbors.keys():
                time += 1
                continue
            (row,col) = neighbors[time]
            if self.flood(grid,time,row,col,directions,seen,neighbors):
                return time
            time += 1
        return 1
    
    def flood(self,grid,time,row,col,directions,seen,neighbors):
        if (row,col) in seen:
            return False
        if grid[row][col] > time:
            neighbors[grid[row][col]] = (row,col)
            return False
        if (row,col) == (len(grid)-1,len(grid)-1):
            return True
        seen.add((row,col))
        for (r,c) in directions:
            if row+r < 0 or row+r == len(grid) or col+c < 0 or col+c == len(grid):
                continue
            if self.flood(grid,time,row+r,col+c,directions,seen,neighbors):
                return True
        return False

@GuitarYs
GuitarYs commented 9 hours ago
from collections import deque
class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        queue = deque([(0, 0, grid[0][0])])  
        while queue:
            x, y, height = queue.popleft()
            if x == n-1 and y == n-1:  
                return height

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    next_height = max(height, grid[nx][ny])
                    if next_height <= height:  
                        queue.append((nx, ny, next_height))
        return -1  
@mo660
mo660 commented 3 hours ago
class Solution {
public:
    bool check(vector<vector<int>>& grid, int threshold) {
        if (grid[0][0] > threshold) {
            return false;
        }
        int n = grid.size();
        vector<vector<int>> visited(n, vector<int>(n, 0));
        visited[0][0] = 1;
        queue<pair<int, int>> q;
        q.push(make_pair(0, 0));

        vector<pair<int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!q.empty()) {
            auto [i, j] = q.front();
            q.pop();

            for (const auto [di, dj]: directions) {
                int ni = i + di, nj = j + dj;
                if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                    if (visited[ni][nj] == 0 && grid[ni][nj] <= threshold) {
                        q.push(make_pair(ni, nj));
                        visited[ni][nj] = 1;
                    }
                }
            }
        }
        return visited[n - 1][n - 1] == 1;
    }

    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        int left = 0, right = n * n - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (check(grid, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        } 
        return left;
    }
};
@SoSo1105
SoSo1105 commented 1 hour ago
思路
优先队列
在搜索的同时将周围的水位加入优先队列
每次选择最低的水位移动

并查集
将两个相邻的方块看作两个结点, 权为两者水位较高值

代码
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        d, m, n, result, q = [(0, 1), (0, -1), (1, 0), (-1, 0)], len(grid), len(grid[0]), 0, [[grid[0][0], 0, 0]]
        visited = [[False] * n for _ in range(m)]
        while q:
            h, x, y = heapq.heappop(q)
            result = max(result, h)
            if x == m - 1 and y == n - 1:
                break
            for dx, dy in d:
                next_x, next_y = x + dx, y + dy
                if -1 < next_x < m and -1 < next_y < n and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    heapq.heappush(q, [grid[next_x][next_y], next_x, next_y])
        return result
复杂度分析

时间复杂度：O(n ^ 2lgn)
空间复杂度：O(n ^ 2)
@Fuku-L
Fuku-L commented 34 minutes ago
代码
public class Solution {

    private int N;

    public static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int swimInWater(int[][] grid) {
        this.N = grid.length;

        int len = N * N;
        // 下标：方格的高度，值：对应在方格中的坐标
        int[] index = new int[len];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                index[grid[i][j]] = getIndex(i, j);
            }
        }

        UnionFind unionFind = new UnionFind(len);
        for (int i = 0; i < len; i++) {
            int x = index[i] / N;
            int y = index[i] % N;

            for (int[] direction : DIRECTIONS) {
                int newX = x + direction[0];
                int newY = y + direction[1];
                if (inArea(newX, newY) && grid[newX][newY] <= i) {
                    unionFind.union(index[i], getIndex(newX, newY));
                }

                if (unionFind.isConnected(0, len - 1)) {
                    return i;
                }
            }
        }
        return -1;
    }

    private int getIndex(int x, int y) {
        return x * N + y;
    }

    private boolean inArea(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    private class UnionFind {

        private int[] parent;

        public UnionFind(int n) {
            this.parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        public int root(int x) {
            while (x != parent[x]) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public boolean isConnected(int x, int y) {
            return root(x) == root(y);
        }

        public void union(int p, int q) {
            if (isConnected(p, q)) {
                return;
            }
            parent[root(p)] = root(q);
        }
    }
}
