【Day 29 】2023-07-08 - 997. 找到小镇的法官 #30
Open
azl397985856 opened this issue 17 hours ago · 8 comments
Comments
@azl397985856
azl397985856 commented 17 hours ago
997. 找到小镇的法官
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/find-the-town-judge/

前置知识
图
题目描述
在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足条件 1 和条件 2 。

给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。

 

示例 1：

输入：n = 2, trust = [[1,2]]
输出：2


示例 2：

输入：n = 3, trust = [[1,3],[2,3]]
输出：3


示例 3：

输入：n = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1


示例 4：

输入：n = 3, trust = [[1,2],[2,3]]
输出：-1


示例 5：

输入：n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
输出：3

 

提示：

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
trust[i] 互不相同
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= n

@Diana21170648
Diana21170648 commented now
思路
邻接矩阵，有向图，用两个数组，一个表示出度，一个表示入度，找入度为n-1且出度为0的索引，即是小镇法官

代码
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree=[0]*(n+1)
        out_degree=[0]*(n+1)
        for i,j in trust:
            in_degree[j]+=1
            out_degree[i]+=1
        for a in range(1,n+1):
            if in_degree[a]==n-1 and out_degree[a]==0:
                return a
        return -1
        
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added 图 29 labels 17 hours ago
@bi9potato
bi9potato commented 13 hours ago
Approach
Absracting it as graph. The judge has in-degree of 
 and out-degree of 
.

Code
class Solution {
    public int findJudge(int n, int[][] trust) {

        int[] in_degree = new int[n+1];
        int[] out_degree = new int[n+1];

        for (int i = 0; i < trust.length; i++) {
            out_degree[trust[i][0]] += 1;
            in_degree[trust[i][1]] += 1;
        }

        for (int i = 1; i < n+1; i++) {
            if (in_degree[i] == n-1 && out_degree[i] == 0) {
                return i;
            }
        }

        return -1;
        
    }
}
Complexity Analysis
Time 
Space 
@joemonkeylee
joemonkeylee commented 13 hours ago
function findJudge(n: number, trust: number[][]): number {
    if (n === 1) return 1
    const map: Map<number, number> = new Map()
    for (let z = 1; z <= n; z++) map.set(z, 0)
    for (let z of trust) {
        map.delete(z[0])
        if (map.get(z[1]) || map.get(z[1]) === 0) map.set(z[1], map.get(z[1]) + 1)
    }
    for (let z of map.entries()) if (z[1] === n - 1) return z[0]
    return -1
};
@SoSo1105
SoSo1105 commented 8 hours ago
思路
根据条件进行遍历

代码
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 如果存在n-1个人，代表符合条件2
        res = set(x for x,_ in trust)
        if len(res) != n-1:
            return -1
        for i in range(1,n+1):
            if i not in res:
                break
        num = 0
        # 遍历统计信任疑似法官的人数
        for _,y in trust:
            if y == i:
                num += 1
        return i if num == n-1 else -1
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@mo660
mo660 commented 6 hours ago
代码
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> inDo(n+1);
        vector<int> outDo(n+1);
        for(auto &it : trust){
            inDo[it[1]]++;
            outDo[it[0]]++;
        }
        for (int i = 1; i <= n; i++)
        {
            if(inDo[i] == n-1 && outDo[i] == 0)
                return i;
        }
        return -1;
    }
};
@zhaoygcq
zhaoygcq commented 5 hours ago • 
思路
本质上是一个图的问题：
计算图中每一个节点的入度和出度；当一个节点的入度为n-1(n-1个人都信任)；出度为0(不信任任何人) => 则当前节点为法官

代码
var findJudge = function(n, trust) {
    const inDegrees = new Array(n + 1).fill(0);
    const outDegrees = new Array(n + 1).fill(0);
    for (const edge of trust) {
        const x = edge[0], y = edge[1];
        ++inDegrees[y];
        ++outDegrees[x];
    }
    for (let i = 1; i <= n; ++i) {
        if (inDegrees[i] === n - 1 && outDegrees[i] === 0) {
            return i;
        }
    }
    return -1;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@snmyj
snmyj commented 2 hours ago
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
            unordered_map<int,int> hashs,hashs_judge;
            vector<int> res;
            if(trust.size()==0){ 
                if(n==1){ 
                    return 1;
                }
                return -1;
            }
            for(int i=0;i<trust.size();i++){
                hashs[trust[i][0]]++;
                hashs_judge[trust[i][1]]++;
            }
            for(auto x:hashs){
               
                    res.push_back(x.first);
                
            }
            sort(res.begin(),res.end());
            for(int i=0;i<res.size();i++){
                
                if(res[i]!=i+1) {
                    if(hashs_judge[i+1]==n-1)
                    return i+1;
                    else return -1;
                }
                if(i==res.size()-1&&!hashs.count(n)) {
                      if(hashs_judge[n]==n-1) return n;
                      else return -1;
                    }
            }
            return -1;
    }
};

@catkathy
catkathy commented 40 minutes ago
Code
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degrees = [0] * (n+1)
        out_degrees = [0] * (n+1)

        for a, b in trust:
            graph[a].append(b)
            out_degrees[a] += 1
            in_degrees[b] += 1

        for i in range(1, n+1):
            if out_degrees[i] == 0 and in_degrees[i] == n-1:
                return i

        return -1
