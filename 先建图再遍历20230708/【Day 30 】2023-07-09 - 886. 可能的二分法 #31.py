【Day 30 】2023-07-09 - 886. 可能的二分法 #31
Open
azl397985856 opened this issue 17 hours ago · 8 comments
Comments
@azl397985856
azl397985856 commented 17 hours ago
886. 可能的二分法
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/possible-bipartition/

前置知识
图的遍历
DFS
题目描述
给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。

每个人都可能不喜欢其他人，那么他们不应该属于同一组。

形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。

当可以用这种方法将每个人分进两组时，返回 true；否则返回 false。

 

示例 1：

输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]
示例 2：

输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
示例 3：

输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false
 

提示：

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
对于dislikes[i] == dislikes[j] 不存在 i != j

@Diana21170648
Diana21170648 commented 13 minutes ago
思路
用邻接矩阵建图，表示的是无向图，建议一个颜色数组，-1和1分别表示分组，0表示未进行着色分组，然后用dfs遍历，如果能将不喜欢的人二分分组，那么未true，如果不能分开，则返回false

代码
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        #建图
        graph=[[0]*n for _ in range(n)]
        colors=[0]*n
        for a,b in dislikes:
            graph[a-1][b-1]=1#a不喜欢b
            graph[b-1][a-1]=1#表示b不喜欢a
        #对着色的节点进行循环
        for i in range(n):
            #如果i没着色，且着色后还是不能二分，则表示不能分开
            if colors[i]==0 and not self.dfs(graph,colors,i,1,n):
                return False
        return True#排除所有不能二分分情况，那么最后能二分就是True
    def dfs(self,graph,colors,i,color,n):
        colors[i]=color
        for j in range(n):#-1*color,乘以-1保证不会栈溢出
            if graph[i][j]==1:
                if colors[j]==color:
                    return False
                if colors[j]==0 and not self.dfs(graph,colors,j,-1*color,n):
                    return False
        return True
        
复杂度分析

时间复杂度：O(V+E)，其中 v是点数，e是边数。
空间复杂度：O(V^2),邻接矩阵建图

@azl397985856 azl397985856 added 图 30 labels 17 hours ago
@bi9potato
bi9potato commented 9 hours ago
Approach
Use DFS to traverse the graph.

Code
class Solution {


    private boolean[] group;
    private boolean[] visited;
    private boolean res;

    public boolean possibleBipartition(int n, int[][] dislikes) {

        List<Integer>[] graph = new LinkedList[n+1];

        for (int i = 1; i < n+1; i++) {
            graph[i] = new LinkedList<>();
        }

        for (int[] edge : dislikes) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        group = new boolean[n+1];
        visited = new boolean[n+1];
        res = true;

        for (int node = 1; node < n+1; node++) {
            dfs(graph, node);
        }

        return res;
        
    }

    private void dfs(List<Integer>[] graph, int node) {

        if (!res) {
            return;
        }

        visited[node] = true;

        for (int nbr : graph[node]) {
            if (visited[nbr]) {
                if (group[nbr] == group[node]) {
                    res = false;
                    return;
                }
            } else {
                group[nbr] = !group[node];
                dfs(graph, nbr);
            }
        }

        return;

    }
}
Complexity Analysis
Time 
, where 
 is # of nodes and 
 is # of edge (dislikes).
Space 
@SoSo1105
SoSo1105 commented 7 hours ago
思路
bfs二分法

代码
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for a,b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        color=[0]*n
        stk=[]
   
        for i in range(n):
            if color[i]==0:
                color[i]=1
                stk.append(i)
            while len(stk)>0:
                p=stk.pop(0)
                for j in graph[p]:
                    if color[j]==0:
                        color[j]=3-color[p]
                        stk.append(j)
                    elif color[j]==color[p]:
                        return False
                    else:
                        continue
        return True
                
复杂度分析

时间复杂度：O(M+N)
空间复杂度：O(N)
@Master-guang
Master-guang commented 6 hours ago
/**
 * @param {number} n
 * @param {number[][]} dislikes
 * @return {boolean}
 */
var possibleBipartition = function(n, dislikes) {
    let ok = true;
    let color = new Array(n + 1);
    let visited = new Array(n + 1);
    let graph = buildGraph(n, dislikes);
    // 建图函数
    function buildGraph(n, dislikes) {
        // 图节点编号为 1...n
        let graph = new Array(n + 1);
        for (let i = 1; i <= n; i++) {
            graph[i] = new Array();
        }
        for (let i = 0; i < dislikes.length; i++) {
            let v = dislikes[i][0];
            let w = dislikes[i][1];
            // 「无向图」相当于「双向图」
            // v -> w
            graph[v].push(w);
            // w -> v
            graph[w].push(v);
        }
        return graph;
    }
    // 和之前判定二分图的 traverse 函数完全相同
    function traverse(graph, v) {
        if (!ok) return;
        visited[v] = true;
        for (let i = 0; i < graph[v].length; i++) {
            let w = graph[v][i];
            if (!visited[w]) {
                color[w] = !color[v];
                traverse(graph, w);
            } else {
                if (color[w] == color[v]) {
                    ok = false;
                }
            }
        }
    }
    for (let v = 1; v <= n; v++) {
        if (!visited[v]) {
            traverse(graph, v);
        }
    }
    return ok;
};
@954545647
954545647 commented 3 hours ago
const possibleBipartition = (N, dislikes) => {
  let graph = [...Array(N + 1)].map(() => Array()), // 动态创建二维数组
    colors = Array(N + 1).fill(-1);

  // build the undirected graph
  for (const d of dislikes) {
    graph[d[0]].push(d[1]);
    graph[d[1]].push(d[0]);
  }

  const dfs = (cur, color = 0) => {
    colors[cur] = color;
    for (const nxt of graph[cur]) {
      if (colors[nxt] !== -1 && colors[nxt] === color) return false; // conflict
      if (colors[nxt] === -1 && !dfs(nxt, color ^ 1)) return false;
    }
    return true;
  };

  for (let i = 0; i < N; ++i) if (colors[i] === -1 && !dfs(i, 0)) return false;

  return true;
};
@Fuku-L
Fuku-L commented 2 hours ago
代码
class Solution {
    ArrayList<Integer>[] graph;
    Map<Integer, Integer> color;

    public boolean possibleBipartition(int n, int[][] dislikes) {
        // 遍历图，生成邻接矩阵（图）
        graph = new ArrayList[n+1];
        for(int i = 1; i<=n; i++){
            graph[i] = new ArrayList();
        }
        for(int[] edge: dislikes){
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        // 分组：
        // 0: 未分组 1：组一 -1：组二
        color = new HashMap();
        for(int node = 1; node <= n; node++){
            if(!color.containsKey(node) && !dfs(node, 0)){
                return false;
            }
        } 
        return true;
    }


    private boolean dfs(int node, int c){
        if(color.containsKey(node)){
            return color.get(node) == c;
        }
        color.put(node, c);
        for(int next: graph[node]){
            if(!dfs(next, c^1)) { 
                return false;
            }
        }
        return true;
    }
}
@catkathy
catkathy commented 2 hours ago
思路
BFS

Code
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        colors = [0] * (n + 1)

        for i in range(1, n + 1):
            if colors[i] == 0:
                colors[i] = 1
                queue = deque([i])

                while queue:
                    person = queue.popleft()
                    for disliked_person in graph[person]:
                        if colors[disliked_person] == colors[person]:
                            return False  
                        if colors[disliked_person] == 0:
                            colors[disliked_person] = -colors[person]
                            queue.append(disliked_person)

        return True
@GuitarYs
GuitarYs commented 1 hour ago
class Solution:
    def possible_bi_partition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # 构建邻接表形式的图
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        colors = [-1] * (N + 1)

        def dfs(node, color):
            colors[node] = color

            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == -1 and not dfs(neighbor, 1 - color):
                    return False

            return True

        for i in range(1, N + 1):
            if colors[i] == -1 and not dfs(i, 0):
                return False

        return True
