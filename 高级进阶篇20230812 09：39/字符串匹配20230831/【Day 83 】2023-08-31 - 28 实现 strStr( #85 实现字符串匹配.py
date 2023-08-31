【Day 83 】2023-08-31 - 28 实现 strStr( #85
Open
azl397985856 opened this issue 11 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
28 实现 strStr(
入选理由
暂无

题目地址
[ 之 BF&RK 篇）

https://leetcode-cn.com/problems/implement-strstr/]( 之 BF&RK 篇）

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
@azl397985856 azl397985856 added 字符串 83 labels 11 hours ago
@freesan44
freesan44 commented 3 hours ago
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

@GuitarYs
GuitarYs commented 1 hour ago
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
@Diana21170648
Diana21170648 commented 7 minutes ago
思路
暴力法时间复杂度m*n，滚动哈希选的好，直接是m+n

代码
#暴力法和滚动哈希

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and  not needle:
            return 0
        if not haystack or len(haystack)<len(needle):
            return -1
        if not needle:
            return 0

        hash_val=0
        tar=0
        prime=101

        for i in range(len(haystack)):
            if i<len(needle):
                hash_val=hash_val*26+(ord(haystack[i])-ord("a"))
                hash_val%=prime
                tar=tar*26+(ord(needle[i])-ord("a"))
                tar%=prime
            else:
                hash_val = (hash_val - (ord(haystack[i - len(needle)]) - ord("a")) * ((26 ** (len(needle) - 1)) % prime)) * 26 + (ord(haystack[i]) - ord("a"))#更新哈希表的值，减去左边，加上右边
                hash_val%=prime

            if  i>=len(needle)-1 and hash_val==tar and haystack[i-len(needle)+1:i+1]==needle:
                return i-len(needle)+1
        return 0 if hash_val==tar and haystack[i-len(needle)+1:i+1]==needle else -1


复杂度分析

时间复杂度：O(N+M)，其中 N 为haystacy数组长度,M为needle的长度。
空间复杂度：O(1)
