【Day 33 】2023-07-12 - 1834. 单线程 CPU #35
Open
azl397985856 opened this issue 11 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
1834. 单线程 CPU
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/single-threaded-cpu/

前置知识
模拟
堆
题目描述
给你一个二维数组 tasks ，用于表示 n​​​​​​ 项从 0 到 n - 1 编号的任务。其中 tasks[i] = [enqueueTimei, processingTimei] 意味着第 i​​​​​​​​​​ 项任务将会于 enqueueTimei 时进入任务队列，需要 processingTimei 的时长完成执行。

现有一个单线程 CPU ，同一时间只能执行 最多一项 任务，该 CPU 将会按照下述方式运行：

如果 CPU 空闲，且任务队列中没有需要执行的任务，则 CPU 保持空闲状态。
如果 CPU 空闲，但任务队列中有需要执行的任务，则 CPU 将会选择 执行时间最短 的任务开始执行。如果多个任务具有同样的最短执行时间，则选择下标最小的任务开始执行。
一旦某项任务开始执行，CPU 在 执行完整个任务 前都不会停止。
CPU 可以在完成一项任务后，立即开始执行一项新任务。

返回 CPU 处理任务的顺序。

 

示例 1：

输入：tasks = [[1,2],[2,4],[3,2],[4,1]]
输出：[0,2,3,1]
解释：事件按下述流程运行：
- time = 1 ，任务 0 进入任务队列，可执行任务项 = {0}
- 同样在 time = 1 ，空闲状态的 CPU 开始执行任务 0 ，可执行任务项 = {}
- time = 2 ，任务 1 进入任务队列，可执行任务项 = {1}
- time = 3 ，任务 2 进入任务队列，可执行任务项 = {1, 2}
- 同样在 time = 3 ，CPU 完成任务 0 并开始执行队列中用时最短的任务 2 ，可执行任务项 = {1}
- time = 4 ，任务 3 进入任务队列，可执行任务项 = {1, 3}
- time = 5 ，CPU 完成任务 2 并开始执行队列中用时最短的任务 3 ，可执行任务项 = {1}
- time = 6 ，CPU 完成任务 3 并开始执行任务 1 ，可执行任务项 = {}
- time = 10 ，CPU 完成任务 1 并进入空闲状态


示例 2：

输入：tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
输出：[4,3,2,0,1]
解释：事件按下述流程运行：
- time = 7 ，所有任务同时进入任务队列，可执行任务项  = {0,1,2,3,4}
- 同样在 time = 7 ，空闲状态的 CPU 开始执行任务 4 ，可执行任务项 = {0,1,2,3}
- time = 9 ，CPU 完成任务 4 并开始执行任务 3 ，可执行任务项 = {0,1,2}
- time = 13 ，CPU 完成任务 3 并开始执行任务 2 ，可执行任务项 = {0,1}
- time = 18 ，CPU 完成任务 2 并开始执行任务 0 ，可执行任务项 = {1}
- time = 28 ，CPU 完成任务 0 并开始执行任务 1 ，可执行任务项 = {}
- time = 40 ，CPU 完成任务 1 并进入空闲状态

 

提示：

tasks.length == n
1 <= n <= 105
1 <= enqueueTimei, processingTimei <= 109

@Diana21170648
Diana21170648 commented now
思路
使用堆，每一个位置存储一个元组，然后使用小顶堆，然后根据任务所花时长决定谁先进入cpu被处理，如果任务执行时间一样，则小的下标具有高的优先级,还需要注意一个开始时间

代码
from typing import  List
import heapq
def getorder(tasks:List[List[int]])->List[int]:
    #为了不破坏原始索引，需要先对task做一个处理，加入索引
    tasks=[(task[0],i,task[1])for i ,task in enumerate(tasks)]
    tasks.sort()
    A=[]#CPU运行的任务,队列
    time=0
    ans=[]
    position=0
    for _ in tasks:
        if not A :
            time=max(time,tasks[position][0])#没有运行的任务，那么时间直接跳到需要开始任务的时间
        while position<len(tasks) and tasks[position][0]<=time:#当任务没结束且时间没开始，则将任务添加进堆中，也就是准备进行处理的队列把所有后续开始的任务加入堆中
            heapq.heappush(A,(tasks[position][2],tasks[position][1]))
            position+=1
        d,j=heapq.heappop(A)#从堆中中取出一个任务，并将其加入到ans中
        time+=d#d是任务开始的时间
        ans.append(j) #j是  任务所需要花的时长
    return ans

        
tasks=[[1,2],[2,4],[3,2],[4,1]]
print(getorder(tasks))   
复杂度分析

时间复杂度：O(NlogN)，其中 N 为数组长度。
空间复杂度：O(N),用了堆

@azl397985856 azl397985856 added 堆 模拟 33 labels 11 hours ago
@bi9potato
bi9potato commented 10 hours ago • edited 
class Solution {
    public int[] getOrder(int[][] tasks) {
        int n = tasks.length;
        int[] ans = new int[n];
        int[][] extTasks = new int[n][3];
        for(int i = 0; i < n; i++) {
            extTasks[i][0] = i;
            extTasks[i][1] = tasks[i][0];
            extTasks[i][2] = tasks[i][1];
        }
        Arrays.sort(extTasks, (a,b)->a[1] - b[1]);
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) -> a[2] == b[2] ? a[0] - b[0] : a[2] - b[2]);
        int time = 0;
        int ai = 0;
        int ti = 0;
        while(ai < n) {
            while(ti < n && extTasks[ti][1] <= time) {
                pq.offer(extTasks[ti++]);
                
            }
            if(pq.isEmpty()) {
                time = extTasks[ti][1];
                continue;
            }
            int[] bestFit = pq.poll();
            ans[ai++] = bestFit[0];
            time += bestFit[2];
        }
        return ans;
    }
    
}
