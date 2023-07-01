【Day 22 】2023-07-01 - 3. 无重复字符的最长子串 #23
Open
azl397985856 opened this issue 17 hours ago · 6 comments
Comments
@azl397985856
azl397985856 commented 17 hours ago
3. 无重复字符的最长子串
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

前置知识
哈希表
双指针
题目描述
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
@Diana21170648
Diana21170648 commented 1 minute ago
思路
先存入哈希表，然后用滑动窗口，窗口内只能出现不重复的元素，出现重复的元素，证明需要缩小窗口的范围，窗口的左边界和右边界用双指针处理
自己最初的思路和暴力差不多，如果出现重复，则中断循环
set集合无序且唯一，是更高效的统计方式

代码
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}#collections.defaultdict()创建哈希表
        left=right=0#创建双指针
        ans=0
        for char in range(len(s)):
            char=s[right]
            right+=1
            seen[char]=seen.get(char,0)+1#求哈希表窗口里面元素的频率
            while seen[char]>1:#先判断左边是够需要收缩，右边是确定了吗
                left0=s[left]
                left+=1
                seen[left0]-=1
            ans=max(ans,right-left)      
            #seen[char].append()
        return ans
复杂度分析

时间复杂度：O(N)，其中 N 为str长度。
空间复杂度：O(s)，字符集的长度

@azl397985856 azl397985856 added 双指针 哈希表 滑动窗口 22 labels 17 hours ago
@Beanza
Beanza commented 15 hours ago
class Solution {
public:
int lengthOfLongestSubstring(string s) {
// 哈希集合，记录每个字符是否出现过
unordered_set occ;
int n = s.size();
// 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
int rk = -1, ans = 0;
// 枚举左指针的位置，初始值隐性地表示为 -1
for (int i = 0; i < n; ++i) {
if (i != 0) {
// 左指针向右移动一格，移除一个字符
occ.erase(s[i - 1]);
}
while (rk + 1 < n && !occ.count(s[rk + 1])) {
// 不断地移动右指针
occ.insert(s[rk + 1]);
++rk;
}
// 第 i 到 rk 个字符是一个极长的无重复字符子串
ans = max(ans, rk - i + 1);
}
return ans;
}
};

@zhaoygcq
zhaoygcq commented 7 hours ago
思路
滑动窗口：

设置一个标识字符其实位置索引值的变量left
遍历字符串中的所有字符，使用map对字符的位置进行记录。
如果当前字符已经存在于map中，并且其位置(map中记录的字符位置)在起始变量left之后，则需要更新left： left的值应该更新为map记录的字符位置的后一位，因为前面的字符肯定会导致重复。
每一次循环都需要取最大的窗口值，同时更新map中的字符位置信息
代码
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let map = {};
    let res = 0;
    let left = 0;
    for(let i = 0; i < s.length; i++) {
        const curr = s[i];
        if(map[curr] >= 0 && map[curr] >= left) {
            left = map[curr] + 1; 
        }
        map[curr] = i;
        res = Math.max(i - left + 1, res);
    }
    return  res;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@SunStrongChina
SunStrongChina commented 5 hours ago
思路
双指正，一个forward负责向前开拓，一个shrink负责收缩，当出现重复字符时，进行收缩

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        shrink = 0
        forward = 0
        max_len = 0
        rangeStr = defaultdict(int)
        while forward < len(s):
            if rangeStr[s[forward]] == 0:
                rangeStr[s[forward]] = 1
            else:
                while rangeStr[s[forward]]== 1 :
                    ##开始收缩
                    rangeStr[s[shrink]] -= 1
                    if rangeStr[s[shrink]] == 0:
                        del rangeStr[s[shrink]]
                    shrink += 1
                rangeStr[s[forward]] = 1
            max_len = max(max_len,len(rangeStr))
            forward += 1
        return max_len
时间复杂度：O(n）
空间复杂度：O(n)

@catkathy
catkathy commented 3 hours ago
Code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)

        return res
@hengistchan
hengistchan commented 1 hour ago
function lengthOfLongestSubstring(s: string): number {
  let l = 0, r = 0, sum = 0
  const map = Array(128).fill(0)
  const hasIn = (map: Array<number>) => {
    for (const key of map) {
      if (key > 1) return false
    }
    return true
  }
  while (r < s.length) {
    map[s.charCodeAt(r)]++
    while (!hasIn(map)) {
      map[s.charCodeAt(l)]--
      l++
    }
    sum = Math.max(sum, r - l + 1)
    r++
  }

  return sum
};
