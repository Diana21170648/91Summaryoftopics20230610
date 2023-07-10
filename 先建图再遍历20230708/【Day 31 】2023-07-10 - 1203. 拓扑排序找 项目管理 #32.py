【Day 31 】2023-07-10 - 1203. 项目管理 #32
Open
azl397985856 opened this issue 16 hours ago · 6 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
1203. 项目管理
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies/

前置知识
图论
拓扑排序
BFS & DFS
题目描述

公司共有 n 个项目和  m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。

group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的）小组可能存在没有接手任何项目的情况。

请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：

同一小组的项目，排序后在列表中彼此相邻。
项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。

 

示例 1：


输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
输出：[6,3,4,1,5,2,0,7]
示例 2：

输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
输出：[]
解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
 

提示：

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] 不含重复元素

@Diana21170648
Diana21170648 commented 1 minute ago
思路
拓扑排序

代码
class Solution:
    # 拓扑排序
    def tp_sort(self, items, indegree, neighbors):
        q = collections.deque([])
        ans = []
        for item in items:
            if not indegree[item]:
                q.append(item)
        while q:
            cur = q.popleft()
            ans.append(cur)

            for neighbor in neighbors[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    q.append(neighbor)

        return ans

    def sortItems(self, n: int, m: int, group: List[int], pres: List[List[int]]) -> List[int]:
        max_group_id = m
        for project in range(n):
            if group[project] == -1:
                group[project] = max_group_id
                max_group_id += 1

        project_indegree = collections.defaultdict(int)
        group_indegree = collections.defaultdict(int)
        project_neighbors = collections.defaultdict(list)
        group_neighbors = collections.defaultdict(list)
        group_projects = collections.defaultdict(list)

        for project in range(n):
            group_projects[group[project]].append(project)

            for pre in pres[project]:
                if group[pre] != group[project]:
                    # 小组关系图
                    group_indegree[group[project]] += 1
                    group_neighbors[group[pre]].append(group[project])
                else:
                    # 项目关系图
                    project_indegree[project] += 1
                    project_neighbors[pre].append(project)

        ans = []
        # 先对组进行拓扑排序
        group_queue = self.tp_sort([i for i in range(max_group_id)], group_indegree, group_neighbors)

        if len(group_queue) != max_group_id:
            return []

        for group_id in group_queue:
            # 对小组中的项目进行拓扑排序
            project_queue = self.tp_sort(group_projects[group_id], project_indegree, project_neighbors)

            if len(project_queue) != len(group_projects[group_id]):
                return []
            ans += project_queue

        return ans
复杂度分析

时间复杂度：O(M+N)，其中 N 为数组长度。
空间复杂度：O(M+N)

@azl397985856 azl397985856 added 图 31 labels 16 hours ago
@bi9potato
bi9potato commented 4 hours ago • edited 
class Solution {
    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        int totalGroups = m;
        Map<Integer, List<Integer>> indexGroupMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                group[i] = totalGroups;
                indexGroupMap.put(totalGroups, new ArrayList<>());
                indexGroupMap.get(totalGroups).add(i);
                totalGroups++;
            } else {
                indexGroupMap.putIfAbsent(group[i], new ArrayList<>());
                indexGroupMap.get(group[i]).add(i);
            }
        }

        int[] externalInMap = new int[totalGroups];
        int[] internalInMap = new int[n];
        Map<Integer, List<Integer>> externalGraph = new HashMap<>();
        Map<Integer, List<Integer>> internalGraph = new HashMap<>();
        for (int i = 0; i < beforeItems.size(); i++) {
            if (beforeItems.get(i).size() > 0) {
                int groupNumber = group[i];
                for (int j = 0; j < beforeItems.get(i).size(); j++) {
                    int prevItem = beforeItems.get(i).get(j);
                    int prevGroupNumber = group[prevItem];
                    if (groupNumber == prevGroupNumber) {
                        internalGraph.putIfAbsent(prevItem, new ArrayList<>());
                        internalGraph.get(prevItem).add(i);
                        internalInMap[i]++;
                    } else {
                        externalGraph.putIfAbsent(prevGroupNumber, new ArrayList<>());
                        externalGraph.get(prevGroupNumber).add(groupNumber);
                        externalInMap[groupNumber]++;
                    }
                }
            }
        }

        Queue<Integer> externalQueue = new LinkedList<>();
        for (int i = 0; i < totalGroups; i++) {
            if (externalInMap[i] == 0) {
                externalQueue.offer(i);
            }
        }

        int[] res = new int[n];
        int resIndex = 0;

        while (!externalQueue.isEmpty()) {
            int curGroup = externalQueue.poll();
            Queue<Integer> internalQueue = new LinkedList<>();
            if (indexGroupMap.containsKey(curGroup)) {
                for (int item : indexGroupMap.get(curGroup)) {
                    if (internalInMap[item] == 0) {
                        internalQueue.offer(item);
                    }
                }
            }
            while (!internalQueue.isEmpty()) {
                int curItem = internalQueue.poll();
                res[resIndex] = curItem;
                resIndex++;
                if (internalGraph.containsKey(curItem)) {
                    for (int nextItemInGroup : internalGraph.get(curItem)) {
                        internalInMap[nextItemInGroup]--;
                        if (internalInMap[nextItemInGroup] == 0) {
                            internalQueue.offer(nextItemInGroup);
                        }
                    }
                }
            }

            if (externalGraph.containsKey(curGroup)) {
                for (int nextGroup : externalGraph.get(curGroup)) {
                    externalInMap[nextGroup]--;
                    if (externalInMap[nextGroup] == 0) {
                        externalQueue.offer(nextGroup);
                    }
                }
            }

        }
        return resIndex == n ? res : new int[]{};
    }
}
@snmyj
snmyj commented 2 hours ago
class Solution {
public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        for(int i = 0; i < n; i++)
        {
            if(group[i] == -1)
                group[i] = m++;
        }
        vector<vector<int>> itemgraph(n);
        vector<vector<int>> groupgraph(m);
        vector<int> itemIndegree(n, 0);
        vector<int> groupIndegree(m, 0);
        for(int i = 0; i < n; i++)
        {
            for(auto j : beforeItems[i])
            {
                itemgraph[j].push_back(i);
                itemIndegree[i]++;
                if(group[i] != group[j]) 
                {	
                    groupgraph[group[j]].push_back(group[i]);
                    groupIndegree[group[i]]++;
                }
            }
        }
        vector<vector<int>> g_items(m);
        
        queue<int> q;
        for(int i = 0; i < n; i++)
            if(itemIndegree[i] == 0)
                q.push(i);
        int countItem = 0;
        while(!q.empty())
        {
            int i = q.front();
            q.pop();
            countItem++;
            g_items[group[i]].push_back(i);
             for(auto j : itemgraph[i])
            {
                if(--itemIndegree[j]==0)
                    q.push(j);
            }
        }
        if(countItem != n)
            return {};
        vector<int> g_order;
        for(int i = 0; i < m; i++)
            if(groupIndegree[i] == 0)
                q.push(i);
        int countgroup = 0;
        while(!q.empty())
        {
            int g = q.front();
            q.pop();
            countgroup++;
            g_order.push_back(g);
            for(auto j : groupgraph[g])
            {
                if(--groupIndegree[j]==0)
                    q.push(j);
            }
        }
        if(countgroup != m)
            return {};
        vector<int> ans(n);
        int idx = 0;
        for(auto g : g_order)
        {
            for(auto i : g_items[g])
                ans[idx++] = i;
        }
        return ans;
    }
};
@Master-guang
Master-guang commented 1 hour ago
// 题目有点难了，对于没怎么学过图论的我，还得继续补知识
const topSort = (deg, graph, items) => {
    const Q = [];
    for (const item of items) {
        if (deg[item] === 0) {
            Q.push(item);
        }
    }
    const res = [];
    while (Q.length) {
        const u = Q.shift(); 
        res.push(u);
        for (let i = 0; i < graph[u].length; ++i) {
            const v = graph[u][i];
            if (--deg[v] === 0) {
                Q.push(v);
            }
        }
    }
    return res.length == items.length ? res : [];
}

var sortItems = function(n, m, group, beforeItems) {
    const groupItem = new Array(n + m).fill(0).map(() => []);

    // 组间和组内依赖图
    const groupGraph = new Array(n + m).fill(0).map(() => []);
    const itemGraph = new Array(n).fill(0).map(() => []);

    // 组间和组内入度数组
    const groupDegree = new Array(n + m).fill(0);
    const itemDegree = new Array(n).fill(0);
    
    const id = new Array(n + m).fill(0).map((v, index) => index);

    let leftId = m;
    // 给未分配的 item 分配一个 groupId
    for (let i = 0; i < n; ++i) {
        if (group[i] === -1) {
            group[i] = leftId;
            leftId += 1;
        }
        groupItem[group[i]].push(i);
    }
    // 依赖关系建图
    for (let i = 0; i < n; ++i) {
        const curGroupId = group[i];
        for (const item of beforeItems[i]) {
            const beforeGroupId = group[item];
            if (beforeGroupId === curGroupId) {
                itemDegree[i] += 1;
                itemGraph[item].push(i);   
            } else {
                groupDegree[curGroupId] += 1;
                groupGraph[beforeGroupId].push(curGroupId);
            }
        }
    }

    // 组间拓扑关系排序
    const groupTopSort = topSort(groupDegree, groupGraph, id); 
    if (groupTopSort.length == 0) {
        return [];
    } 
    const ans = [];
    // 组内拓扑关系排序
    for (const curGroupId of groupTopSort) {
        const size = groupItem[curGroupId].length;
        if (size == 0) {
            continue;
        }
        const res = topSort(itemDegree, itemGraph, groupItem[curGroupId]);
        if (res.length === 0) {
            return [];
        }
        for (const item of res) {
            ans.push(item);
        }
    }
    return ans;
};
@zhaoygcq
zhaoygcq commented 51 minutes ago
思路
二分图

构建图
遍历图
代码
/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} group
 * @param {number[][]} beforeItems
 * @return {number[]}
 */
 var sortItems = function(n, m, group, beforeItems) {
    const grahG = [], degG = new Uint16Array(n + m), idsG = [], 
          grahI = [], degI = new Uint16Array(n), idsI = [], r = []
    for (let i = 0; i < n; i++) {
        if (group[i] === -1) {
            idsG[m] = m // 从组数起分配，避免重复
            group[i] = m++
        } else idsG[group[i]] = group[i]
        if (!idsI[group[i]]) idsI[group[i]] = [] // 同组项目，放入到一起
        idsI[group[i]].push(i)
    }
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < beforeItems[i].length; j++) {
            const itemI = beforeItems[i][j]
            if (group[i] === group[itemI]) {// 同组，收集 项目 依赖
                degI[i]++
                if (!grahI[itemI]) grahI[itemI] = []
                grahI[itemI].push(i)
            } else {// 不同组，收集 组 依赖
                degG[group[i]]++
                if (!grahG[group[itemI]]) grahG[group[itemI]] = []
                grahG[group[itemI]].push(group[i])
            }
        }
    }
    const idsGS = sort(idsG.filter(v => v !== void 0), grahG, degG) // 组排序
    if (idsGS.length === 0) return []
    for (let i = 0; i < idsGS.length; i++) {// 组有序，组内项目排序
        if (!idsI[idsGS[i]]) continue
        const idsIS = sort(idsI[idsGS[i]], grahI, degI)
        if (idsIS.length === 0) return []
        r.push(...idsIS)
    }
    return r
};
const sort = (ids, grah, deg) => {// 拓扑排序：id列表，图，入度
    const q = [], r = []
    let start = 0
    for (let i = 0; i < ids.length; i++) if (deg[ids[i]] === 0) q.push(ids[i])
    while (start < q.length) {
        const n = q[start++]
        r.push(n)
        if (!grah[n]) continue
        for (let i = 0; i < grah[n].length; i++) if (--deg[grah[n][i]] === 0) q.push(grah[n][i])
    }
    return r.length === ids.length ? r : []
}
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@catkathy
catkathy commented 15 minutes ago
Code
class Solution:
    def sortItems(self, n, m, group, beforeItems):
        def get_top_order(graph, indegree):
            top_order = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                v = stack.pop()
                top_order.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        stack.append(u)
            return top_order if len(top_order) == len(graph) else []

        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m += 1

        graph_items = [[] for _ in range(n)]
        indegree_items = [0] * n
        graph_groups = [[] for _ in range(m)]
        indegree_groups = [0] * m
        for u in range(n):
            for v in beforeItems[u]:
                graph_items[v].append(u)
                indegree_items[u] += 1
                if group[u] != group[v]:
                    graph_groups[group[v]].append(group[u])
                    indegree_groups[group[u]] += 1

        item_order = get_top_order(graph_items, indegree_items)
        group_order = get_top_order(graph_groups, indegree_groups)
        if not item_order or not group_order:
            return []

        order_within_group = collections.defaultdict(list)
        for v in item_order:
            order_within_group[group[v]].append(v)

        res = []
        for group in group_order:
            res += order_within_group[group]
        return res
