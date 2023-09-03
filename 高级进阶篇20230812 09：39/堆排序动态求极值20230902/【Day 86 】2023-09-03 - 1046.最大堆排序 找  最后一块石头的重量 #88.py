【Day 86 】2023-09-03 - 1046.最后一块石头的重量 #88
Open
azl397985856 opened this issue 12 hours ago · 1 comment
Comments
@azl397985856
azl397985856 commented 12 hours ago
1046.最后一块石头的重量
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/last-stone-weight/

前置知识
堆
题目描述
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

 

示例：

输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000
@azl397985856 azl397985856 added 堆 86 labels 12 hours ago
@Diana21170648
Diana21170648 commented 1 minute ago
思路
建立堆，两两比较，再考虑舍弃还是入堆，然后知道达到边界条件，就是只有一个元素的时候，返回堆顶元素，达到目标

代码
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[-stone for stone in stones]
        heapq.heapify(h)
        while len(h)>1:
            a,b=heapq.heappop(h),heapq.heappop(h)
            if a !=b:
                heapq.heappush(h,a-b)
        return -h[0] if h else 0
复杂度分析

时间复杂度：O(NlogN)，其中 N 为数组长度,logN为堆的插入删除复杂度。
空间复杂度：O(N)
