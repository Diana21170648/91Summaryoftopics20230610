【Day 90 】2023-09-07 - 1054. 距离相等的条形码 #92
Open
azl397985856 opened this issue 10 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 10 hours ago
1054. 距离相等的条形码
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/distant-barcodes/

前置知识
堆
贪心
题目描述
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

 

示例 1：

输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]
示例 2：

输入：[1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]
 

提示：

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000

@Diana21170648
Diana21170648 commented now
思路
堆，分奇数和偶数，按频率的降序排序

代码
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n=len(barcodes)
        ans=[0]*n
        even,odd=0,1
        for x,count in sorted(((x,count) for x,count in Counter(barcodes).items()),key=lambda x:x[1],reverse=True):
            while count:
                count-=1
                if even<n:
                    ans[even]=x
                    even+=2
                else:
                    ans[odd]=x
                    odd+=2
        return ans
复杂度分析

时间复杂度：O(NlogK)，其中 N 为元素个数，K为不重复元素的个数。
空间复杂度：O(K),K为不重复元素的个数。

@azl397985856 azl397985856 added 堆 贪心 90 labels 10 hours ago
@yetfan
yetfan commented 9 hours ago
代码
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        length = len(barcodes)
        if length < 2:
            return barcodes

        counts = {}
        max_count = 0
        for b in barcodes:
            counts[b] = counts.get(b, 0) + 1
            max_count = max(max_count, counts[b])

        evenIndex = 0
        oddIndex = 1
        half_length = length // 2
        res = [0] * length
        for x, count in counts.items():
            while count > 0 and count <= half_length and oddIndex < length:
                res[oddIndex] = x
                count -= 1
                oddIndex += 2
            while count > 0:
                res[evenIndex] = x
                count -= 1
                evenIndex += 2
        return res
