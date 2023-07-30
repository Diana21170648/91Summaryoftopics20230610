【Day 51 】2023-07-30 - 1162. 地图分析 #53
Open
azl397985856 opened this issue 20 hours ago · 4 comments
Comments
@azl397985856
azl397985856 commented 20 hours ago
1162. 地图分析
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/as-far-from-land-as-possible/

前置知识
暂无

题目描述
你现在手里有一份大小为 N x N 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。
其中 0 代表海洋，1 代表陆地，请你找出一个海洋单元格，
这个海洋单元格到离它最近的陆地单元格的距离是最大的。

我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：
(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。

如果网格上只有陆地或者海洋，请返回 -1。

 

示例 1：
image



输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释：
海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。
示例 2：

image


输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释：
海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。
 

提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1

@Diana21170648
Diana21170648 commented now
思路
bfs+队列，陆地入队

代码
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        steps=-1
        queue=collections.deque([(i,j)for i in range(n) for j in range(n) if grid[i][j]==1])
        if len(queue)==0 or len(queue)==n**2:
            return steps
        while len(queue)>0:
            for _ in range(len(queue)):
                x,y=queue.popleft()
                for xi,yj in (x+1,y),(x-1,y),(x,y+1),(x,y-1):#遍历上下左右
                    if xi>=0 and xi<n and yj>=0 and yj<n and grid[xi][yj]==0:#判断在格子范围内
                        queue.append((xi,yj))
                        grid[xi][yj]=-1#遍历过之后置为-1，表示已经处理过了，避免重复计算
            steps+=1
        return steps
复杂度分析

时间复杂度：O(N*N)，其中 N 为数组长度。
空间复杂度：O(N*N)

@azl397985856 azl397985856 added BFS 51 labels 20 hours ago
@GuitarYs
GuitarYs commented 3 hours ago
class Solution:
    def maxDistance(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        ocean_queue = []
        land_queue = []

   
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    ocean_queue.append((i, j))
                else:
                    land_queue.append((i, j))

        if len(ocean_queue) == 0 or len(land_queue) == 0:
            return -1

        max_distance = -1

   
        while ocean_queue:
            ocean_cell = ocean_queue.pop(0)

         
            x0, y0 = ocean_cell
            for land_cell in land_queue:
  
                x1, y1 = land_cell
                distance = abs(x0 - x1) + abs(y0 - y1)
                max_distance = max(max_distance, distance)
        return max_distance
@HuiyingC
HuiyingC commented 3 hours ago
class Solution(object):
    # BFS
    # 从land开始(入队)BFS搜索water, water入队step+1
    # key1: 初始land入队
    # key2: is_valid() return True if water
    # O(n^2), O(n^2)
    def maxDistance(self, grid):
        DIRECTIONS = [(0, 1), (1,0), (0,-1), (-1,0)]
        q = collections.deque()
        visited = set()
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    q.append((i, j))
                    visited.add((i, j))

        step = -1
        while q:
            step += 1
            queue_size = len(q)
            for _ in range(queue_size):
                x, y = q.popleft()
                for xi, yi in DIRECTIONS:
                    new_x, new_y = x+xi, y+yi
                    if (not self.is_valid(new_x, new_y, grid) 
                        or (new_x, new_y) in visited):
                        continue
                    q.append((new_x, new_y))
                    visited.add((new_x, new_y))
        
        return -1 if step == 0 else step

    def is_valid(self, x, y, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
            
        return grid[x][y] == 0  # key: return True if water
@zhaoygcq
zhaoygcq commented 2 hours ago
思路
多源BFS;从陆地往外扩展，直到所有的海洋变为陆地，记录需要的次数

代码
/**
 * @param {number[][]} grid
 * @return {number}
 */
/**
 * @param {number[][]} grid
 * @return {number}
 */
function maxDistance(grid) {
    const n = grid.length;
    const queue = [];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            // 将所有陆地加入队列，而不是海洋，陆地不断扩展到海洋
            if (grid[i][j] == 1) {
                queue.push([i, j]);
            }
        }
    }

    let ans = -1;
    // 都是海洋 或 都是陆地
    if (queue.length === 0 || queue.length === n * n) {
        return ans;
    }

    // 方向数组
    const locations = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
    ];

    while (queue.length != 0) {
        const len = queue.length;

        // 对每个陆地4个方向搜索
        for (let k = 0; k < len; k++) {
            const [x, y] = queue.shift();
            // 向该点的4个方向进行搜索
            for (const location of locations) {
                const nextI = x + location[0];
                const nextJ = y + location[1];

                // 合法 且 是海洋
                if (
                    nextI >= 0 &&
                    nextI < n &&
                    nextJ >= 0 &&
                    nextJ < n &&
                    grid[nextI][nextJ] == 0
                ) {
                    grid[nextI][nextJ] = 1; // 变为陆地
                    queue.push([nextI, nextJ]);
                }
            }
        }
        ans++;
    }
    return ans;
}
复杂度分析

时间复杂度：O(N2)，其中 N 为数组行数的长度， M为数组列数。
空间复杂度：O(1)
