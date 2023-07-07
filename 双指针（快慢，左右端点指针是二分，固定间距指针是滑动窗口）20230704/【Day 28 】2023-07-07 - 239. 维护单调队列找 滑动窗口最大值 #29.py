【Day 28 】2023-07-07 - 239. 滑动窗口最大值 #29
Open
azl397985856 opened this issue 11 hours ago · 4 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
239. 滑动窗口最大值
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/sliding-window-maximum/

前置知识
队列
滑动窗口
题目描述
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

进阶：

你能在线性时间复杂度内解决此题吗？

 

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
1 [3  -1  -3] 5  3  6  7       3
1  3 [-1  -3  5] 3  6  7       5
1  3  -1 [-3  5  3] 6  7       5
1  3  -1  -3 [5  3  6] 7       6
1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

@Diana21170648
Diana21170648 commented now
思路
维护单调队列

代码
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans=[]
        q=collections.deque()
        for i in range(len(nums)):
            while q and nums[q[-1]]<=nums[i]:#队列不为空，且元素小，移除队尾元素
                q.pop()
            while q and i-q[0]>=k:#队列不为空，队头元素不在滑动窗口内，弹出队头移除失效元素
                q.popleft()
            q.append(i)
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans

复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(k)

@azl397985856 azl397985856 added 双指针 滑动窗口 28 labels 11 hours ago
@bi9potato
bi9potato commented 9 hours ago
Approach
Monotonic queue.

Code
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {

        int[] res = new int[nums.length-k+1];

        Deque<Integer> dq = new LinkedList<>();

        for (int j = 0, i = 1-k; j < nums.length; i++, j++) {

            if (i > 0 && dq.peekFirst() == nums[i-1]) {
                dq.removeFirst();
            }

            while (!dq.isEmpty() && dq.peekLast() < nums[j] ) {
                dq.removeLast();
            }

            dq.addLast(nums[j]);

            if (i >= 0) {
                res[i] = dq.peekFirst();
            }

        }

        return res;
        
    }
}
Complexity Analysis
Time 
Space 
@SoSo1105
SoSo1105 commented 3 hours ago
思路
用一个数组index记录滑动窗口中可能是最大值的下标
第一个窗口的index中只保留3和-1的下标，因为有3在，1不可能是最大值
第三个窗口的index中只保留5的下标，因为有5在，-1和-3在滑动过程中也不可能是最大值

所以，当第i个数的下标准备进index时，需要移除所有index中已有下标指向的比第i个数要小的数的下标，如在第三个窗口中，-1，-3的下标都要出index，3的下标也要出index,因为超过了窗口范围
当第i个数小于index最后一个数时，i进index，因为当i前面的下标出index后，i指向的数有可能是最大的

代码
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n<2 or k==1:
            return nums
        res = []
        index = [0]    
        queue = [nums[0]]
        
        for i in range(1,n):
            
            if index[0]<=i-k:
                index.pop(0)
            while index and nums[index[-1]]<nums[i]:
                index.pop()
            index.append(i)
            if i>=k-1:
                res.append(nums[index[0]])
          
        return res 
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@zhaoygcq
zhaoygcq commented 17 minutes ago
思路
维护一个双端队列：
遍历数组，维护一个值递减的队列；当遍历到索引i，并且i >= k - 1的时候，可以取出队头的值(该窗口中的最大值)；
同时，当队头的值已经在窗口之外时，需要将其弹出

代码
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const maxSlidingWindow = function (nums, k) {
    let res = [];
    if(nums.length < k) return res;
    let queue = [];
    for(let i = 0; i < nums.length; i++) {
        let curr = nums[i];
        while(queue.length && nums[queue[queue.length - 1]] < curr) {
            queue.pop();
        }
        queue.push(i);

        while(i >= k && queue[0] <= i - k) {
            queue.shift();
        }
        if(i >= k - 1) {
            res.push(nums[queue[0]])
        }
    }

    return res;
}
复杂度分析

时间复杂度：O(kN)，其中 N 为数组长度。
空间复杂度：O(N)
