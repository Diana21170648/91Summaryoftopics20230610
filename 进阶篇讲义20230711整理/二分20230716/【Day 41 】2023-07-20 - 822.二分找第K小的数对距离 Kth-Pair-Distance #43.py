【Day 41 】2023-07-20 - 822. Kth-Pair-Distance #43
Open
azl397985856 opened this issue 17 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 17 hours ago
822. Kth-Pair-Distance
入选理由
暂无

题目地址
https://binarysearch.com/problems/Kth-Pair-Distance

前置知识
暂无

题目描述
Given a list of integers nums and an integer k, return the k-th (0-indexed) smallest abs(x - y) for every pair of elements (x, y) in nums. Note that (x, y) and (y, x) are considered the same pair.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 5, 3, 2]
k = 3
Output
2
Explanation
Here are all the pair distances:

abs(1 - 5) = 4
abs(1 - 3) = 2
abs(1 - 2) = 1
abs(5 - 3) = 2
abs(5 - 2) = 3
abs(3 - 2) = 1
Sorted in ascending order we have [1, 1, 2, 2, 3, 4].
@Diana21170648
Diana21170648 commented now
思路
二分

代码
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_not_greater(diff):
            i = ans = 0
            for j in range(1, len(nums)):
                while nums[j] - nums[i] > diff:
                    i += 1
                ans += j - i
            return ans

        l, r = 0, nums[-1] - nums[0]
        while l < =r:
            mid = (l + r) // 2
            if count_not_greater(mid) < k:
                l = mid + 1
            else:
                r = mid-1
        return l

复杂度分析

时间复杂度：O(NlogN)，其中 N 为数组长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 二分 41 labels 17 hours ago
@GuitarYs
GuitarYs commented 4 hours ago
class Solution:
    def find_kth_smallest(self, nums, k):
        distances = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                distances.append(abs(nums[i] - nums[j]))

        distances.sort()
        return distances[k]

    def print_example(self):
        nums = [1, 5, 3, 2]
        k = 3

        result = self.find_kth_smallest(nums, k)
        print(result)
@andyli4
andyli4 commented 3 hours ago
var smallestDistancePair = function(nums, k) {
nums.sort(function(a,b){return a-b});
var low = 0;
var high = nums[nums.length-1] - nums[0];
while(low < high){
var mid = Math.floor((low+high)/2);
var count = 0;
var left = 0;
for(var right = 0; right < nums.length; right++){
while(nums[right] - nums[left] > mid) left++;
count += right - left;
}
if(count >= k) high = mid;
else low = mid + 1;
}
return low;
};

