【Day 36 】2023-07-15 - 912. 排序数组 #38
Open
azl397985856 opened this issue 11 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
912. 排序数组
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/sort-an-array/

前置知识
数组
排序
题目描述
给你一个整数数组 nums，请你将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

@Diana21170648
Diana21170648 commented 1 minute ago
思路
计数排序和快排都可以

代码
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        cnt=[0]*(50000*2+1)
        res=[]
        #统计频率
        for num in nums:
            cnt[num+50000]+=1#存在负数，加5000使得数组下标为正
        for i in range(len(cnt)):
            res.extend([i-50000]*cnt[i])
        return res
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(M),M=50000*2+1

@azl397985856 azl397985856 added 排序 36 labels 11 hours ago
@HuiyingC
HuiyingC commented 8 hours ago
return sorted(nums)

@acy925
acy925 commented 6 hours ago
代码
public class Solution {
    public int[] sortArray(int[] nums) {
        int len = nums.length;

        for (int i = 1; i < len; i++) {
            // 先暂存这个元素，然后之前元素逐个后移，留出空位
            int temp = nums[i];
            int j = i;
            while (j > 0 && nums[j - 1] > temp) {
                nums[j] = nums[j - 1];
                j--;
            }
            nums[j] = temp;
        }
        return nums;
    }
}
复杂度分析

时间复杂度：O(N2)
空间复杂度：O(1)
