【Day 43 】2023-07-22 - 1456. 定长子串中元音的最大数目 #45
Open
azl397985856 opened this issue yesterday · 6 comments
Comments
@azl397985856
azl397985856 commented yesterday
1456. 定长子串中元音的最大数目
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

前置知识
暂无

题目描述
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。



示例 1：

输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
示例 2：

输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
示例 3：

输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
示例 4：

输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
示例 5：

输入：s = "tryhard", k = 4
输出：1


提示：

1 <= s.length <= 10^5
s 由小写英文字母组成
1 <= k <= s.length

@Diana21170648
Diana21170648 commented 1 minute ago
思路
滑动窗口

代码
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        temp = 0
        vowels = set(['a','e','i','o','u'])
        for i in range(k):
            res += s[i] in vowels
        if res==k: return k
        temp = res
        for i in range(k,len(s)):
            temp += (s[i] in vowels) - (s[i-k] in vowels)
            res = max(temp,res)
            if res ==k: return k
        return res
复杂度分析

时间复杂度：O(N)，其中 N 为字符串长度。
空间复杂度：O(1)
  
@azl397985856 azl397985856 added 滑动窗口 43 labels yesterday
@Beanza
Beanza commented yesterday
public int maxVowels(String s, int k) {

if (s == null || s.length() < k)
    return 0;

int res = 0;
Set<Character> set = new HashSet<>(){{
    add('a');add('e');add('i');add('o');add('u');
}};

for (int i = 0; i < s.length() - k + 1; i++) {

    String sub = s.substring(i, i + k);
    int count = 0;

    for (int j = 0; j < sub.length(); j++)
        if (set.contains(sub.charAt(j)))
            count++;

    res = Math.max(res, count);
}

return res;
}

@HuiyingC
HuiyingC commented 20 hours ago • edited 
Intuition

fixed length sliding window
dp memo stores cnt
Code

def maxVowels(self, s, k):
    if len(s) < k: return 0

    vowels = {'a', 'e', 'i', 'o', 'u'}
    ans = cnt = 0
    for i, c in enumerate(s):  # key 
        if c in vowels:
            cnt += 1
        if i >= k and s[i - k] in vowels:
            cnt -= 1
        ans  = max(cnt, ans)
    
    return ans    
Complexity Analysis
Time complexity: O(n)
Space complexity: O(n)

@zhaoygcq
zhaoygcq commented 10 hours ago
思路
滑动窗口：

首先记录第一个窗口的元音字母数目num；
移动窗口，如果移出的元素(左边)为元音字母，则num--；
如果移入的元素(右边)为元音字母，则num++；
代码
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    let ans = -1;
    let left = 0, right = k;
    const Letters = ['a', 'e', 'i', 'o', 'u'];
    let num = count(s.slice(left, right));
    while(right <= s.length) {
        if(left > 0) {
            if(Letters.includes(s[right-1])) {
                num++;
            }
            if(Letters.includes(s[left-1])) {
                num--
            }
        }
        num > ans && (ans = num)
        left++;
        right++;
    }
    return ans;
};

function count(str) {
    const Letters = ['a', 'e', 'i', 'o', 'u'];
    
    let num = 0;
    for(let val of str) {
        Letters.includes(val) && num++;
    }
    return num;
}
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
@passengersa
passengersa commented 9 hours ago
代码
var maxVowels = function(s, k) {
const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
let maxCount = 0;
let currentCount = 0;

// 初始化长度为k的第一个子字符串中的元音字母数
for (let i = 0; i < k; i++) {
if (vowels.has(s[i])) {
currentCount++;
}
}
maxCount = currentCount;

// 滑动窗口，依次计算每个长度为k的子字符串中的元音字母数
for (let i = k; i < s.length; i++) {
if (vowels.has(s[i - k])) {
currentCount--;
}
if (vowels.has(s[i])) {
currentCount++;
}
maxCount = Math.max(maxCount, currentCount);
}

return maxCount;
};

@Moin-Jer
Moin-Jer commented 6 minutes ago
class Solution {
    public int maxVowels(String s, int k) {
        int n = s.length();
        int vowel_count = 0;
        for (int i = 0; i < k; ++i) {
            vowel_count += isVowel(s.charAt(i));
        }
        int ans = vowel_count;
        for (int i = k; i < n; ++i) {
            vowel_count += isVowel(s.charAt(i)) - isVowel(s.charAt(i - k));
            ans = Math.max(ans, vowel_count);
        }
        return ans;
    }

    public int isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ? 1 : 0;
    }
}
