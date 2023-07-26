【Day 47 】2023-07-26 - Number of Operations to Decrement Target to Zero #49
Open
azl397985856 opened this issue 10 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 10 hours ago
Number of Operations to Decrement Target to Zero
入选理由
暂无

题目地址
https://binarysearch.com/problems/Number-of-Operations-to-Decrement-Target-to-Zero

前置知识
暂无

题目描述
You are given a list of positive integers nums and an integer target. Consider an operation where we remove a number v from either the front or the back of nums and decrement target by v.

Return the minimum number of operations required to decrement target to zero. If it's not possible, return -1.

Constraints

n ≤ 100,000 where n is the length of nums Example 1 Input nums = [3, 1, 1, 2, 5, 1, 1] target = 7 Output 3 Explanation We can remove 1, 1 and 5 from the back to decrement target to zero.

Example 2 Input nums = [2, 4] target = 7 Output -1 Explanation There's no way to decrement target = 7 to zero.

@Diana21170648
Diana21170648 commented now
思路
滑动窗口+逆向思维

代码
  def solve(self, A, target):
        if not A and not target: return 0
        target = sum(A) - target
        ans = len(A) + 1
        i = t = 0

        for j in range(len(A)):
            t += A[j]
            while i <= j and t > target:
                t -= A[i]
                i += 1
            if t == target: ans = min(ans, len(A) - (j - i + 1))
        return -1 if ans == len(A) + 1 else ans
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 滑动窗口 47 labels 10 hours ago
@GuitarYs
GuitarYs commented 4 hours ago
class Solution:
    def minOperations(self, nums, target):
        memo = {}

        def dp(nums, target):
            if target == 0:
                return 0
            if target < 0 or len(nums) == 0:
                return float('inf')

            if target in memo:
                return memo[target]

            option1 = dp(nums[:-1], target - nums[-1]) + 1
            option2 = dp(nums[1:], target - nums[0]) + 1
            result = min(option1, option2)
            memo[target] = result
            return result

        result = dp(nums, target)

        if result == float('inf'):
            return -1
        else:
            return result
1
