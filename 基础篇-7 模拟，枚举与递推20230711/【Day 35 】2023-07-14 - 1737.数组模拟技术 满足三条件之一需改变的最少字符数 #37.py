【Day 35 】2023-07-14 - 1737. 满足三条件之一需改变的最少字符数 #37
Open
azl397985856 opened this issue 12 hours ago · 4 comments
Comments
@azl397985856
azl397985856 commented 12 hours ago
1737. 满足三条件之一需改变的最少字符数
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

前置知识
计数
枚举
题目描述
给你两个字符串 a 和 b ，二者均由小写字母组成。一步操作中，你可以将 a 或 b 中的 任一字符 改变为 任一小写字母 。

操作的最终目标是满足下列三个条件 之一 ：

a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。
b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。
a 和 b 都 由 同一个 字母组成。
返回达成目标所需的 最少 操作数。

 

示例 1：

输入：a = "aba", b = "caa"
输出：2
解释：满足每个条件的最佳方案分别是：
1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。
示例 2：

输入：a = "dabadd", b = "cda"
输出：3
解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。
 

提示：

1 <= a.length, b.length <= 105
a 和 b 只由小写字母组成

@Diana21170648
Diana21170648 commented now
思路
模拟计数，字母只有26个，所以可以用数组计数

代码
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        counter_a=[0]*26#实际索引0-25
        counter_b=[0]*26

        #遍历找各字母出现的次数，最坏的情况就是a与b中所有字母都不同，那就需要m+n的长度
        for aa in a:
            counter_a[ord(aa)-ord('a')]+=1
        for bb in b:
            counter_b[ord(bb)-ord('a')]+=1

        #开始计算转换,需要改变的最少字符数
        ans=len(a)+len(b)
        for i in range(26):
            ans=min(ans,len(a)+len(b)-counter_a[i]-counter_b[i])
        
        #把a中所有字母变得比b小，需要转换的最少字符数
        for i in range(1,26):#不从0开始是因为a就是0
            t=0
            for j in range(i,26):
                t+=counter_a[j]
            for j in range(i):
                t+=counter_b[j]
            ans=min(ans,t)
        #把b中所有字母变得比a小，需要转换的最少字符数
        for i in range(1,26):
            t=0
            for j in range(i,26):
                t+=counter_b[j]
            for j in range(i):
                t+=counter_a[j]
            ans=min(ans,t)
        return ans




复杂度分析

时间复杂度：O(N+M)，其中 N 为字符串a的长度，M为字符串b的长度。
空间复杂度：O(26)


@azl397985856 azl397985856 added 枚举 35 labels 12 hours ago
@YizheWill
YizheWill commented 4 hours ago • edited 
class Solution:
    def minCharacters(self, a: str, b: str) -> int:

        A = [0] * 26
        B = [0] * 26
        for ch in a:
            A[ord(ch)-ord('a')] += 1
        for ch in b:
            B[ord(ch)-ord('a')] += 1

        n1, n2 = len(a), len(b)
        presum1 = presum2 = 0
        ans = n1+n2
        
        for i in range(25):
            presum1 += A[i]
            presum2 += B[i]

            ans = min(ans, n1-presum1+presum2, presum1+n2-presum2, n1-A[i] + n2-B[i])

        ans = min(ans, n1-A[25] + n2-B[25])

        return ans
@dorian-byte
dorian-byte commented 4 hours ago
    def minCharacters(self, word1: str, word2: str) -> int:
        count1 = [0] * 26
        count2 = [0] * 26
        
        for ch in word1:
            count1[ord(ch) - ord('a')] += 1
        
        for ch in word2:
            count2[ord(ch) - ord('a')] += 1
        
        len1, len2 = len(word1), len(word2)
        prefix_sum1 = prefix_sum2 = 0
        min_ops = len1 + len2
        
        for i in range(25):
            prefix_sum1 += count1[i]
            prefix_sum2 += count2[i]
            min_ops = min(min_ops, len1 - prefix_sum1 + prefix_sum2, prefix_sum1 + len2 - prefix_sum2, len1 - count1[i] + len2 - count2[i])
        
        min_ops = min(min_ops, len1 - count1[25] + len2 - count2[25])
        
        return min_ops
@freesan44
freesan44 commented 3 hours ago
class Solution {
    func minCharacters(_ A: String, _ B: String) -> Int {
        var counter_A = [Int](repeating: 0, count: 26)
    var counter_B = [Int](repeating: 0, count: 26)
    
    for a in A {
        let index = Int(a.asciiValue! - Character("a").asciiValue!)
        counter_A[index] += 1
    }
    
    for b in B {
        let index = Int(b.asciiValue! - Character("a").asciiValue!)
        counter_B[index] += 1
    }
    
    var ans = A.count + B.count
    
    for i in 0..<26 {
        ans = min(ans, A.count + B.count - counter_A[i] - counter_B[i])
    }
    
    for i in 1..<26 {
        var t = 0
        for j in i..<26 {
            t += counter_A[j]
        }
        
        for j in 0..<i {
            t += counter_B[j]
        }
        
        ans = min(ans, t)
    }
    
    for i in 1..<26 {
        var t = 0
        for j in i..<26 {
            t += counter_B[j]
        }
        
        for j in 0..<i {
            t += counter_A[j]
        }
        
        ans = min(ans, t)
    }
    
    return ans
    }
}
