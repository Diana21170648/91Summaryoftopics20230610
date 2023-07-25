【Day 46 】2023-07-25 - 76. 最小覆盖子串 #48
Open
azl397985856 opened this issue yesterday · 7 comments
Comments
@azl397985856
azl397985856 commented yesterday
76. 最小覆盖子串
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/minimum-window-substring

前置知识
Sliding Window
哈希表
题目描述
给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。



示例：

输入：S = "ADOBECODEBANC", T = "ABC"
输出："BANC"


提示：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

@Diana21170648
Diana21170648 commented now
思路
更新滑动窗口

代码
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, counter, N, ct = 0, Counter(), len(s), Counter(t)
        k = 0
        ret, ans = inf, ""
        for r in range(N):
            counter[s[r]] += 1
            if s[r] in t and counter[s[r]] == ct[s[r]]:
                k += 1
            while k == len(ct):
                if r - l + 1 < ret:
                    ans = s[l:r+1]
                ret = min(r - l + 1, ret)
                counter[s[l]] -= 1
                if s[l] in t and counter[s[l]] == ct[s[l]]-1:
                    k -= 1
                l += 1
        return ans
复杂度分析

时间复杂度：O(N+k)。
空间复杂度：O(s)

@azl397985856 azl397985856 added 滑动窗口 46 labels yesterday
@GuitarYs
GuitarYs commented 11 hours ago
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1

        window_count = {}

        formed = 0

        start = 0
        min_length = float('inf')

        left = 0

        for right in range(len(s)):
            char = s[right]

            window_count[char] = window_count.get(char, 0) + 1

            if char in target_count and window_count[char] <= target_count[char]:
                formed += 1

            while formed == len(t):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                char = s[left]
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                left += 1

        if min_length == float('inf'):
            return ""

        return s[start:start+min_length]
@jackgaoyuan
jackgaoyuan commented 9 hours ago
func minWindow(s string, t string) string {
	var res string
	cnt := math.MaxInt32
	hashMap := make(map[byte]int)
	l := 0
	r := 0
	for i := 0; i < len(t); i++ {
		hashMap[t[i]]++
	}
	for r < len(s) {
		hashMap[s[r]]--
		for check(hashMap) {
			if r-l+1 < cnt {
				cnt = r - l + 1
				res = s[l : r+1]
			}
			hashMap[s[l]]++
			l++
		}
		r++
	}
	return res
}

func check(hashMap map[byte]int) bool {
	for _, v := range hashMap {
		if v > 0 {
			return false
		}
	}
	return true
}
@catkathy
catkathy commented 5 hours ago
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = collections.defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float('inf')
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -=1
            end += 1

            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]]==0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res
@huizsh
huizsh commented 4 hours ago
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, counter, N, ct = 0, Counter(), len(s), Counter(t)
        k = 0
        ret, ans = inf, ""
        for r in range(N):
            counter[s[r]] += 1
            if s[r] in t and counter[s[r]] == ct[s[r]]:
                k += 1
            while k == len(ct):
                if r - l + 1 < ret:
                    ans = s[l:r+1]
                ret = min(r - l + 1, ret)
                counter[s[l]] -= 1
                if s[l] in t and counter[s[l]] == ct[s[l]]-1:
                    k -= 1
                l += 1
        return ans
@wzbwzt
wzbwzt commented 3 hours ago • edited 
/*
思路：
滑动窗口
while 右边界 < 合法条件：
// 右边界扩张
window右边界+1
更新状态信息
// 左边界收缩
while 符合收缩条件：
window左边界+1
更新状态信息

复杂度：
时间复杂度： O(N+K);N 为 S 串长度，K 为 T 串长度
空间复杂度： O(S)，其中 S 为 T 字符集元素个数
*/

func minWindow(s string, t string) (ans string) {
	counter := map[byte]int{}
	l := 0
	N := len(s)
	counter_t := map[byte]int{}
	for i := 0; i < len(t); i++ {
		counter_t[t[i]]++
	}

	res := math.MaxInt32
	k := 0
	for r := 0; r < N; r++ {
		counter[s[r]]++
		if _, ok := counter_t[s[r]]; ok && counter[s[r]] == counter_t[s[r]] {
			k++
		}
		for k == len(counter_t) {
			//收缩左边
			if r-l+1 < res {
				ans = s[l : r+1]
			}
			res = min((r - l + 1), res)

			counter[s[l]]--
			if _, ok := counter_t[s[l]]; ok && counter[s[l]] == counter_t[s[l]]-1 {
				k--
			}
			l++
		}

	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
@mo660
mo660 commented 8 minutes ago
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> hs, ht;
        for (auto c: t) ht[c] ++ ;
        string res;
        int cnt = 0;
        for (int i = 0, j = 0; i < s.size(); i ++ ) {
            hs[s[i]] ++ ;
            if (hs[s[i]] <= ht[s[i]]) cnt ++ ;

            while (hs[s[j]] > ht[s[j]]) hs[s[j ++ ]] -- ;
            if (cnt == t.size()) {
                if (res.empty() || i - j + 1 < res.size())
                    res = s.substr(j, i - j + 1);
            }
        }
        return res;
    }
};
