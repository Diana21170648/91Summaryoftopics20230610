【Day 88 】2023-09-05 - 451 根据字符出现频率排序 #90
Open
azl397985856 opened this issue 11 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
451 根据字符出现频率排序
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/sort-characters-by-frequency/comments/

前置知识
排序算法
堆
哈希表
题目描述
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:

输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
@Diana21170648
Diana21170648 commented 1 minute ago
思路
哈希表统计次数
优先队列排序
出堆构成降序字符串

代码
class Solution:
    def frequencySort(self, s: str) -> str:
        dict={}
        for ch in s:
            dict[ch]=dict.get(ch,0)+1
        pq=sorted(dict.items(),key=lambda x:x[1],reverse=True)
        res=[]#存储结果
        for ch,count in pq:
            #count=dict[ch]
            res.append(ch*count)
        return ''.join(res)
复杂度分析

时间复杂度：O(N+KlogK)，其中 N 为字符串个数，K为不重复字符串个数。
空间复杂度：O(K)，最坏情况下，均不重复，K=N

@azl397985856 azl397985856 added 堆 链表 88 labels 11 hours ago
@freesan44
freesan44 commented 2 hours ago
class Solution {
    func frequencySort(_ s: String) -> String {
        var dict: [Character: Int] = [:]
        
        for ch in s {
            dict[ch, default: 0] += 1
        }
        
        let vals = dict.sorted(by: { $0.value > $1.value })
        
        var res = ""
        
        for (k, v) in vals {
            res += String(repeating: k, count: v)
        }
        
        return res
    }
}

