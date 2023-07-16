【Day 37 】2023-07-16 - 69. x 的平方根 #39
Open
azl397985856 opened this issue yesterday · 5 comments
Comments
@azl397985856
azl397985856 commented yesterday
69. x 的平方根
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/sqrtx

前置知识
二分法
题目描述
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
由于返回类型是整数，小数部分将被舍去
@Diana21170648
Diana21170648 commented now
思路
二分左加右减求左边界

代码
class Solution:
    def mySqrt(self, x: int) -> int:
        ans,l,r=0,0,x
        while l<=r:
            mid=(l+r)//2
            if mid**2<=x:
                ans=mid
                l=mid+1
            if mid**2>x:
                
                r=mid-1
        return int(ans)
复杂度分析

时间复杂度：O(logN)，其中 N 为数组长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 二分 37 labels yesterday
@HuiyingC
HuiyingC commented 14 hours ago
Intuition

二分

Code

def mySqrt(self, x):
    if x < 2: return x

    l, r = 0, x
    while l + 1 < r:
        root = (l+r)//2
        if root > x//root:
            r = root
        elif root < x//root:
            l = root
        else:
            return root
            
    return l # floor
Complexity Analysis

Time complexity: O(logn)

Space complexity: O(1)

@GuitarYs
GuitarYs commented 5 hours ago
lass Solution:
    def sqrt(self, x):
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return result
@Moin-Jer
Moin-Jer commented 3 hours ago
class Solution {
    public int mySqrt(int x) {
        if (x <= 1) {
            return x;
        }
        int l = 1;
        int r = 46340;
        while (l <= r) {
            int mid = (l + r) >>> 1;
            if (mid * mid == x) {
                return mid;
            } else if (mid * mid > x) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }
}
@catkathy
catkathy commented 2 hours ago • edited 
def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right
