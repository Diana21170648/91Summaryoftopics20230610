【Day 24 】2023-07-03 - 1590. 使数组和能被 P 整除 #25
Open
azl397985856 opened this issue 11 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
1590. 使数组和能被 P 整除
入选理由
暂无

题目地址
https://leetcode.cn/problems/make-sum-divisible-by-p/

前置知识
哈希表
同余定理及简单推导
前缀和
题目描述
给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。

请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。

子数组 定义为原数组中连续的一组元素。



示例 1：

输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
示例 2：

输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
示例 3：

输入：nums = [1,2,3], p = 3
输出：0
解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。
示例  4：

输入：nums = [1,2,3], p = 7
输出：-1
解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。
示例 5：

输入：nums = [1000000000,1000000000,1000000000], p = 3
输出：0


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109

@Diana21170648
Diana21170648 commented now
思路
第一步，简历哈希表方便查找，第二步处理特殊情况即sums的和小于整数p

代码
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        seen={0:-1}#以应对从数组索引 0 处开始取子数组的情况。注意：这是一个非常重要的技巧
        sum_total=sum(nums)
        n=len(nums)
        cha=sum_total%p#10%6=4
        cur=0
        if sum_total<p:
            return -1
        if cha==0:
            return 0
        for i,x in enumerate(nums):#同时遍历索引和值
            cur=(cur+x)%p#0+3%6=3，在计算当前前缀和的值
            target=(cur-cha+p)%p#3-4+6=5%6=5，在计算目标前缀和的值
            if target in seen:#在哈希表中有目标移除的值或数组
                n=min(n,i-seen[target])#可移除的最小子数组的长度
            seen[cur]=i#把前缀和的索引添加进哈希表
        return -1 if n==len(nums) else n
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(min（N,cha）)

@azl397985856 azl397985856 added Math 哈希表 数组 前缀和 24 labels 11 hours ago
@freesan44
freesan44 commented 2 hours ago
class Solution {
    func minSubarray(_ nums: [Int], _ p: Int) -> Int {
         var total = nums.reduce(0, +)
    let mod = total % p
    if mod == 0 { return 0 }

    var ans = nums.count
    total = 0
    var dic: [Int: Int] = [0: -1]
    for j in 0..<nums.count {
        total += nums[j]
        let cur = total % p
        let target = (cur - mod + p) % p
        if let index = dic[target] {
            ans = min(ans, j - index)
        }
        dic[cur] = j
    }

    if ans == nums.count {
        return -1
    }
    return ans
    }
}
@SoSo1105
SoSo1105 commented 1 hour ago
思路
要移除的连续子数组的和对p求余要等于数组总和对p求余。

代码
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums) % p
        if x == 0:
            return 0
        n = len(nums) 
        d = defaultdict(lambda:-1)
        cur_sum = 0
        d[0] = 0
        ans = n
        for i in range(n):
            cur_sum += nums[i]
            temp =  (cur_sum % p - x + p)%p
            if d[temp] != -1:
                ans = min(ans,i+1-d[temp]) 
            d[cur_sum % p] = i+1
        return -1 if ans == n else ans
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
