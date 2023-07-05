【Day 26 】2023-07-05 - 26.删除排序数组中的重复项 #27
Open
azl397985856 opened this issue 10 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 10 hours ago
26.删除排序数组中的重复项
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

前置知识
暂无

题目描述
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。



示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。


说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
  print(nums[i]);
}

@Diana21170648
Diana21170648 commented now
思路
用快慢指针（读写指针）

代码
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=right=0
        if not nums:
            return 0
        while right<len(nums):
            if nums[right]!=nums[left]:#如果不相等，则读指针后移，写指针也后
                left+=1
                nums[left]=nums[right]#保证最后返回的nums不重复
            right+=1
        return left+1#索引从0开始
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 双指针 数组 26 labels 10 hours ago
@hengistchan
hengistchan commented 8 hours ago
双指针，重拳出击

function removeDuplicates(nums: number[]): number {
  let i = 1, cur = nums[0], j = 0
  while (i < nums.length) {
    if (nums[i] !== cur) {
      nums[j + 1] = nums[i]
      j++
      cur = nums[i]
    }
    i++
  }
  return nums.length - i + j + 1
};
@SoSo1105
SoSo1105 commented 2 hours ago
思路
双指针法

代码
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
               continue
            else:
                p += 1
                nums[p] = nums[i]
        # 题目要求返回的是长度，所有坐标要加 1
        return p + 1
复杂度分析

时间复杂度：O(N)
空间复杂度：O(1)
