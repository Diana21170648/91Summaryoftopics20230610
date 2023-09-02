【Day 85 】2023-09-02 - 215. 数组中的第 K 个最大元素 #87
Open
azl397985856 opened this issue 17 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 17 hours ago
215. 数组中的第 K 个最大元素
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

前置知识
堆
排序
题目描述

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

@azl397985856 azl397985856 added 堆 85 labels 17 hours ago
@Fuku-L
Fuku-L commented 2 hours ago
代码
class Solution {
    int quickselect(int[] nums, int l, int r, int k) {
        if (l == r) return nums[k];
        int x = nums[l], i = l - 1, j = r + 1;
        while (i < j) {
            do i++; while (nums[i] < x);
            do j--; while (nums[j] > x);
            if (i < j){
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
            }
        }
        if (k <= j) return quickselect(nums, l, j, k);
        else return quickselect(nums, j + 1, r, k);
    }
    public int findKthLargest(int[] _nums, int k) {
        int n = _nums.length;
        return quickselect(_nums, 0, n - 1, n - k);
    }
}
@Alexno1no2
Alexno1no2 commented 1 hour ago
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
                
        def maxHepify(arr, i, end):     # 大顶堆
            j = 2*i + 1                 # j为i的左子节点【建堆时下标0表示堆顶】
            while j <= end:             # 自上而下进行调整
                if j+1 <= end and arr[j+1] > arr[j]:    # i的左右子节点分别为j和j+1
                    j += 1                              # 取两者之间的较大者
                
                if arr[i] < arr[j]:             # 若i指示的元素小于其子节点中的较大者
                    arr[i], arr[j] = arr[j], arr[i]     # 交换i和j的元素，并继续往下判断
                    i = j                       # 往下走：i调整为其子节点j
                    j = 2*i + 1                 # j调整为i的左子节点
                else:                           # 否则，结束调整
                    break
        
        n = len(nums)
        
        # 建堆【大顶堆】
        for i in range(n//2-1, -1, -1):         # 从第一个非叶子节点n//2-1开始依次往上进行建堆的调整
            maxHepify(nums, i, n-1)

        # 排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆
        # k-1次重建堆（堆顶元素），或 k次交换到尾部（倒数第k个元素）
        for j in range(n-1, n-k-1, -1):
            nums[0], nums[j] = nums[j], nums[0]     # 堆顶元素（当前最大值）放置到尾部j
            maxHepify(nums, 0, j-1)                 # j-1变成尾部，并从堆顶0开始调整堆
        
        return nums[-k]
@Diana21170648
Diana21170648 commented 1 minute ago
思路
小顶堆，数组短排序也行，就是时间复杂度高一点

代码
#k大的小顶堆

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        h=[]
        for i in range(k):
            heapq.heappush(h,nums[i])
        for i in range(k,n):
            if nums[i]>h[0]:
                heapq.heapreplace(h,nums[i])
        return h[0]
         
复杂度分析

时间复杂度：O(Nlogk)，其中 N 为数组长度。
空间复杂度：O(k)，小顶堆空间换时间
