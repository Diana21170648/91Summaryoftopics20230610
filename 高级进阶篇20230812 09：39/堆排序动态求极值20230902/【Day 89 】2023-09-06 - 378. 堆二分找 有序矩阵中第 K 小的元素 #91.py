【Day 89 】2023-09-06 - 378. 有序矩阵中第 K 小的元素 #91
Open
azl397985856 opened this issue 11 hours ago · 1 comment
Comments
@azl397985856
azl397985856 commented 11 hours ago
378. 有序矩阵中第 K 小的元素
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

前置知识
二分查找
堆
题目描述
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例：

matrix = [
 [ 1,  5,  9],
 [10, 11, 13],
 [12, 13, 15]
],
k = 8,

返回 13。
 

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

@azl397985856 azl397985856 added the 89 label 11 hours ago
@Diana21170648
Diana21170648 commented now
思路
堆二分找有序矩阵中的第K小

代码
class Solution:
    def notGreaterCount(self, matrix, target):
        # 等价于在matrix中搜索mid，搜索的过程中利用有序的性质记录比mid小的元素个数

        # 我们选择左下角，作为开始元素
        curRow = 0
        # 多少列
        COL_COUNT = len(matrix[0])
        # 最后一列的索引
        LAST_COL = COL_COUNT - 1
        res = 0

        while curRow < len(matrix):
            # 比较最后一列的数据和target的大小
            if matrix[curRow][LAST_COL] < target:
                res += COL_COUNT
            else:
                i = COL_COUNT - 1
                while i >= 0 and matrix[curRow][i] > target:
                    i -= 1
                # 注意这里要加1
                res += i + 1
            curRow += 1

        return res

    def kthSmallest(self, matrix, k):
        if len(matrix) < 1:
            return None
        start = matrix[0][0]
        end = matrix[len(matrix) - 1][len(matrix[0]) - 1]
        while start < end:
            mid = start + ((end - start) >> 1)
            count = self.notGreaterCount(matrix, mid)
            if count < k:
                start = mid + 1
            else:
                end = mid
        # 返回start，mid，end都一样
        return start
复杂度分析

时间复杂度：O(Nlog（r-l）)，其中 N 为数组长度。
空间复杂度：O(1)
