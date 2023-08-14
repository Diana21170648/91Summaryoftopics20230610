【Day 66 】2023-08-14 - 435. 无重叠区间 #68
Open
azl397985856 opened this issue 11 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
435. 无重叠区间
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/non-overlapping-intervals/

前置知识
暂无

题目描述
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
lis

代码
class Solution:
    def LIS(SELF,A:List[int])->int:
        d=[]#存储最长递增子序列的元素
        for s,e in A:
            i=bisect.bisect_left(d,e)
            if i<len(d):
                d[i]=e
            elif not d or d[-1]<=s:
                d.append(e)
        return len(d)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        if n==0:
            return 0
        ans=1#至少考虑一个不重叠的区间
        intervals.sort(key=lambda a:a[0])
        return n-self.LIS(intervals)
复杂度分析

时间复杂度：O(NlogN)，其中 N 为数组长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added 贪心 66 labels 11 hours ago
@freesan44
freesan44 commented 3 hours ago
class Solution {
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        let n = intervals.count
    if n == 0 {
        return 0
    }
    
    var dp = [Int](repeating: 1, count: n)
    var ans = 1
    var sortedIntervals = intervals.sorted { $0[0] < $1[0] }
    
    for i in 0..<n {
        for j in (0..<i).reversed() {
            if sortedIntervals[i][0] >= sortedIntervals[j][1] {
                dp[i] = max(dp[i], dp[j] + 1)
                break // 由于是按照开始时间排序的，因此可以剪枝
            }
        }
    }
    
    return n - dp.max()!
    }
}

