【Day 84 】2023-09-01 - 28 实现 strStr( #86
Open
azl397985856 opened this issue 12 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 12 hours ago
28 实现 strStr(
入选理由
暂无

题目地址
[ 之 KMP 篇）

https://leetcode-cn.com/problems/implement-strstr/]( 之 KMP 篇）

https://leetcode-cn.com/problems/implement-strstr/)

前置知识
滑动窗口
字符串
Hash 运算
题目描述
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
kmp

代码
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        if not needle:
            return 0

        def computeNext(needle):  # 更改为不与内置函数冲突的名称
            next = [0] * m
            j = 0
            for i in range(1, len(needle)):
                while j > 0 and needle[i] != needle[j]:
                    j = next[j - 1]
                if needle[i] == needle[j]:
                    j += 1
                next[i] = j
            return next

        next_arr = computeNext(needle)  # 使用与内置函数不冲突的变量名
        i, j = 0, 0
        while i < n and j < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = next_arr[j - 1]
                else:
                    i += 1
        if j == m:
            return i - j
        return -1
复杂度分析

时间复杂度：O(N+M)，其中 N 为数组长度。
空间复杂度：O(M)

@azl397985856 azl397985856 added 字符串 84 labels 12 hours ago
@GuitarYs
GuitarYs commented 11 hours ago
class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1
@freesan44
freesan44 commented 4 hours ago
class Solution {
    func strStr(_ haystack: String, _ needle: String) -> Int {
        let lenA = haystack.count
        let lenB = needle.count
        
        if lenB == 0 {
            return 0
        }
        if lenB > lenA {
            return -1
        }
        
        let endIndex = haystack.index(haystack.endIndex, offsetBy: -(lenB - 1))
        for i in 0...(lenA - lenB) {
            let startIndex = haystack.index(haystack.startIndex, offsetBy: i)
            let endIndex = haystack.index(startIndex, offsetBy: lenB)
            let substring = haystack[startIndex..<endIndex]
            if substring == needle {
                return i
            }
        }
        return -1
    }
}

