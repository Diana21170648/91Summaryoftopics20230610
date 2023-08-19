【Day 71 】2023-08-19 - 260. 只出现一次的数字 III #73
Open
azl397985856 opened this issue 12 hours ago · 1 comment
Comments
@azl397985856
azl397985856 commented 12 hours ago
260. 只出现一次的数字 III
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/single-number-iii/

前置知识
位运算
数组
哈希表
题目描述
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
@azl397985856 azl397985856 added 位运算 71 labels 12 hours ago
@Diana21170648
Diana21170648 commented 1 minute ago
思路
用哈希表做空间复杂度不满足题意，所以用了位运算

代码
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=a=b=0
        n=len(nums)
        first_bit=1
        for i in nums:#将所有的数字异或，会只剩下只出现一次的的数字不为零，相当于筛选出来了只出现一次的元素
            xor ^=i
        while first_bit & xor==0:#与运算，找不同的低位
            first_bit<<=1#左移一位相当于乘以2，直到找到低位bit为1的num

        for i in nums:#异或之后的nums
            if first_bit & i:
                a ^=i
            else:
                b ^=i
        return [a,b]
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
