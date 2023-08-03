【Day 55 】2023-08-03 - 198. 打家劫舍 #57
Open
azl397985856 opened this issue yesterday · 7 comments
Comments
@azl397985856
azl397985856 commented yesterday
198. 打家劫舍
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/house-robber/

前置知识
暂无

题目描述
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

0 <= nums.length <= 100
0 <= nums[i] <= 400

@Diana21170648
Diana21170648 commented now
思路
记忆化递归动态规划 打家劫舍

代码
#20230803 第122(55)天 
#T=O(n)
#S=O(1)
#没用dp数组

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]
        else:
            pre=nums[0]
            cur=max(nums[1],pre)
            for i in range(2,n):
                cur,pre=max(pre+nums[i],cur),cur
            return cur
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)，使用了记忆化递归优化空间复杂度

@azl397985856 azl397985856 added 动态规划 55 labels yesterday
@Moin-Jer
Moin-Jer commented 12 hours ago
class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int length = nums.length;
        if (length == 1) {
            return nums[0];
        }
        int[] dp = new int[length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < length; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }
        return dp[length - 1];
    }
}
@mo660
mo660 commented 10 hours ago
class Solution {
public:
    int rob(vector<int>& nums) {
    int prev = 0;
    int curr = 0;

    // 每次循环，计算“偷到当前房子为止的最大金额”
    for (int i : nums) {
        // 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
        // dp[k] = max{ dp[k-1], dp[k-2] + i }
        int temp = max(curr, prev + i);
        prev = curr;
        curr = temp;
        // 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]
    }

    return curr;
    }
};
@GuitarYs
GuitarYs commented 9 hours ago
public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return nums[0];
        }
        if (n == 2) {
            return Math.max(nums[0], nums[1]);
        }
        int[] dp = new int[n];
        dp[0] = nums[0];  // 第一个房屋的最高金额为其本身的金额
        dp[1] = Math.max(nums[0], nums[1]);  // 第二个房屋的最高金额为两个房屋中金额较大的那个
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]); //每一个房屋得到的金额已经是加上之前的了
        }

        return dp[n-1];
    }
@snmyj
snmyj commented 1 hour ago
class Solution {
public:
    int rob(vector<int>& nums) {
        int n=nums.size();
        vector<int> dp(n);
        if(nums.size()==1) return nums[0];
        dp[0]=nums[0];
        dp[1]=max(nums[0],nums[1]);
        for(int i=2;i<n;i++){
            dp[i]=max(dp[i-1],dp[i-2]+nums[i]);
        }
        return dp[n-1];
    }
}; 
@Alexno1no2
Alexno1no2 commented 1 hour ago
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # 子问题：
        # f(k) = 偷 [0..k) 房间中的最大金额

        # f(0) = 0
        # f(1) = nums[0]
        # f(k) = max{ rob(k-1), nums[k-1] + rob(k-2) }

        N = len(nums)
        dp = [0] * (N+1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N+1):
            dp[k] = max(dp[k-1], nums[k-1] + dp[k-2])
        return dp[N]
@Master-guang
Master-guang commented 24 minutes ago
var rob = function(nums) {
    // 备忘录
    let memo = new Array(nums.length).fill(-1);
    // 强盗从第 0 间房子开始抢劫
    return dp(nums, 0, memo);
};

// 返回 dp[start..] 能抢到的最大值
function dp(nums, start, memo) {
    if (start >= nums.length) {
        return 0;
    }
    // 避免重复计算
    if (memo[start] != -1) return memo[start];

    let res = Math.max(dp(nums, start + 1, memo),
            nums[start] + dp(nums, start + 2, memo));
    // 记入备忘录
    memo[start] = res;
    return res;
}
