【Day 52 】2023-07-31 - 1298. 你能从盒子里获得的最大糖果数 #54
Open
azl397985856 opened this issue 15 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 15 hours ago
1298. 你能从盒子里获得的最大糖果数
入选理由
暂无

题目地址
https://leetcode.cn/problems/maximum-candies-you-can-get-from-boxes/

前置知识
BFS
题目描述

给你 n 个盒子，每个盒子的格式为 [status, candies, keys, containedBoxes] ，其中：

状态字 status[i]：整数，如果 box[i] 是开的，那么是 1 ，否则是 0 。
糖果数 candies[i]: 整数，表示 box[i] 中糖果的数目。
钥匙 keys[i]：数组，表示你打开 box[i] 后，可以得到一些盒子的钥匙，每个元素分别为该钥匙对应盒子的下标。
内含的盒子 containedBoxes[i]：整数，表示放在 box[i] 里的盒子所对应的下标。
给你一个 initialBoxes 数组，表示你现在得到的盒子，你可以获得里面的糖果，也可以用盒子里的钥匙打开新的盒子，还可以继续探索从这个盒子里找到的其他盒子。

请你按照上述规则，返回可以获得糖果的 最大数目 。

 

示例 1：

输入：status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
输出：16
解释：
一开始你有盒子 0 。你将获得它里面的 7 个糖果和盒子 1 和 2。
盒子 1 目前状态是关闭的，而且你还没有对应它的钥匙。所以你将会打开盒子 2 ，并得到里面的 4 个糖果和盒子 1 的钥匙。
在盒子 1 中，你会获得 5 个糖果和盒子 3 ，但是你没法获得盒子 3 的钥匙所以盒子 3 会保持关闭状态。
你总共可以获得的糖果数目 = 7 + 4 + 5 = 16 个。
示例 2：

输入：status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
输出：6
解释：
你一开始拥有盒子 0 。打开它你可以找到盒子 1,2,3,4,5 和它们对应的钥匙。
打开这些盒子，你将获得所有盒子的糖果，所以总糖果数为 6 个。
示例 3：

输入：status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]
输出：1
示例 4：

输入：status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = []
输出：0
示例 5：

输入：status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]
输出：7
 

提示：

1 <= status.length <= 1000
status.length == candies.length == keys.length == containedBoxes.length == n
status[i] 要么是 0 要么是 1 。
1 <= candies[i] <= 1000
0 <= keys[i].length <= status.length
0 <= keys[i][j] < status.length
keys[i] 中的值都是互不相同的。
0 <= containedBoxes[i].length <= status.length
0 <= containedBoxes[i][j] < status.length
containedBoxes[i] 中的值都是互不相同的。
每个盒子最多被一个盒子包含。
0 <= initialBoxes.length <= status.length
0 <= initialBoxes[i] < status.length

@Diana21170648
Diana21170648 commented 1 minute ago
思路
思路：把所有的开着的盒子和所有能找到钥匙的没开着的盒子添加进队列，然后找队列里面所有的糖果数即可，因为是树结构，所以能用BFS

代码
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes=set(initialBoxes)
        queue=collections.deque([i for i in boxes if status[i]])
        for i in queue:
            for j in containedBoxes[i]:
                boxes.add(j)
                if status[j]:
                    queue.append(j)
            for j in keys[i]:
                if status[j]==0 and j in boxes:
                    queue.append(j)
                status[j]=1
        return sum(candies[i] for i in queue)
复杂度分析

时间复杂度：O(N+K)，其中 N 为数组长度，K为钥匙数。
空间复杂度：O(N)

@azl397985856 azl397985856 added BFS 52 labels 15 hours ago
@HuiyingC
HuiyingC commented 9 hours ago
def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
    # BFS
    # 没有上锁的盒子入队列做 BFS
        # 遇到盒子， 就将没有上锁的盒子入队列
        # 遇到钥匙，就将对应的盒子解锁（修改 status 数组），当然前提是我们已经找到了对应的盒子
    # key: 当前没有盒子的钥匙，后面找到了钥匙后再回头开这个盒子
    # O(n+k) << boxes+keys
    # O(n)

    boxes = set(initialBoxes) #set去重
    q = [i for i in boxes if status[i]] #没有上锁的盒子入队
    for i in q:
        for j in containedBoxes[i]:
            boxes.add(j)
            if status[j]:
                q.append(j)
        for j in keys[i]:
            if status[j] == 0 and j in boxes: #有钥匙+已找到=可开
                q.append(j)
            status[j] = 1 #更新状态
    return sum(candies[i] for i in q)
@freesan44
freesan44 commented 7 hours ago
class Solution {
    func maxCandies(_ status: [Int], _ candies: [Int], _ keys: [[Int]], _ containedBoxes: [[Int]], _ initialBoxes: [Int]) -> Int {
        var boxes = Set(initialBoxes)
    var queue = initialBoxes.filter { status[$0] }
    var totalCandies = 0
    
    while !queue.isEmpty {
        let box = queue.removeFirst()
        for containedBox in containedBoxes[box] {
            boxes.insert(containedBox)
            if status[containedBox] {
                queue.append(containedBox)
            }
        }
        for key in keys[box] {
            if status[key] == false && boxes.contains(key) {
                queue.append(key)
            }
            status[key] = true
        }
        totalCandies += candies[box]
    }
    
    return totalCandies
    }
}

