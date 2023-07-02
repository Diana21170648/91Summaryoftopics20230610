【Day 23 】2023-07-02 - 30. 串联所有单词的子串 #24
Open
azl397985856 opened this issue 16 hours ago · 6 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
30. 串联所有单词的子串
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words

前置知识
哈希表
双指针
题目描述
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
s = "barfoothefoobarman",
words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
s = "wordgoodgoodgoodbestword",
words = ["word","good","best","word"]
输出：[]

@Diana21170648
Diana21170648 commented now
思路
两个哈希表，字符串,剪枝

代码
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        seen={}#第一个哈希表
        #left=right=0
        ans=[]
        n=len(s)
        m=len(words)
        k=len(words[0])
        if words is None or len(words)==0:
            return ans

        for word in words:#求每个单词出现的频率
            seen[word]=seen.get(word,0)+1

        for i in range(n-m*k+1):
            #得到当前窗口字符串
            cur_str=s[i:i+m*k]
            #新建第二个哈希表，暂存words的组合字符串
            temp={}
            j=0

            while j<len(cur_str):
                #提取单词
                word=cur_str[j:j+k]
                #剪枝，很早了解，第一次见，剪枝就是退出的意思
                if word not in seen:
                    break
                temp[word]=temp.get(word,0)+1#统计在temp里面word出现的频率
                #继续剪枝
                if temp[word]>seen[word]:
                    break
                j+=k
            if j==len(cur_str):
                ans.append(i)

        return ans
复杂度分析

时间复杂度：O(NMK)，n为s的长度，m为words的长度，k为单个word的长度。
空间复杂度：O(M)

@azl397985856 azl397985856 added 双指针 哈希表 字符串 23 labels 16 hours ago
@chang-you
chang-you commented 12 hours ago
class Solution {
   public List<Integer> findSubstring(String s, String[] words) {
        if (s == null || words == null || words.length == 0) {
            return new ArrayList<>();
        }

        List<Integer> res = new ArrayList<>();
        int n = words.length;
        int m = words[0].length();
        HashMap<String, Integer> map = new HashMap<>();

        for (String str : words) {
            map.put(str, map.getOrDefault(str, 0) + 1);
        }

        for (int i = 0; i <= s.length() - n * m; i++) {
            HashMap<String, Integer> copy = new HashMap<>(map);
            int k = n;
            int j = i;
            while (k > 0) {
                String str = s.substring(j, j + m);
                if (!copy.containsKey(str) || copy.get(str) < 1) {
                    break;
                }
                copy.put(str, copy.get(str) - 1);
                k--;
                j += m;
            }
            if (k == 0) res.add(i);
        }
        return res;
   }
}
@SoSo1105
SoSo1105 commented 9 hours ago
思路
滑动窗口

代码
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter

        # 处理特殊情况
        if not s or not words:
            return []
        
        # 哈希表统计单词出现次数，用以后续比较
        word_cnt = Counter(words)
        
        # 单词长度
        word_len = len(words[0])

        # 返回结果列表
        ans = []

        # 遍历，进行窗口滑动
        for i in range(word_len):
            left = i
            right = i
            cnt = 0

            # 哈希表记录窗口的单词出现次数
            window = Counter()

            # 限定边界
            # 这里表示窗口的内容不足以组成串联所有单词的子串，循环结束
            while left + len(words) * word_len <= len(s):
                # 窗口单词出现的次数，与 word_cnt 对比
                while cnt <  len(words):
                    word = s[right:right+word_len]
                    # 如果单词不在 words 中，或者此时单词数量大于 words 中的单词数量时，退出循环另外处理
                    # 单词次数相等也跳出另外判断
                    # 否则更新哈希表 window
                    if (word not in words) or (window[word] >= word_cnt[word]):
                        break
                    window[word] += 1
                    cnt += 1
                    right += word_len
                
                # 先判断哈希表是否相等，相等则加入返回列表中
                if word_cnt == window:
                    ans.append(left)

                # 再处理单词数溢出的情况
                # 区分在于单词是否在 words 中
                if word in words:
                    # 剔除左边部分
                    left_word = s[left: left+word_len]
                    window[left_word] -= 1
                    left += word_len
                    cnt -= 1
                    
                else:
                    # 如果单词不在 words 中，
                    # 清空哈希表，重置窗口开始位置
                    right += word_len
                    window.clear()
                    left = right
                    cnt = 0

        return ans
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@zhaoygcq
zhaoygcq commented 4 hours ago
思路
简单模拟

通过map记录words中的所有单词
遍历字符串s，取出符合长度的子串，遍历子串，判断子串中的单词数是否与map记录的相同，相同则记录索引。
代码
/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function(s, words) {
    if(!words.length || !s) return [];
    let wordsMap = {};
    let res = [];
    let wordsLen = words.length;
    let strLen = words[0].length;
    let subStrLen = strLen * wordsLen;
    for(let val of words) {
        if(!wordsMap[val]) {
            wordsMap[val] = 1;
        } else {
            wordsMap[val]++;
        }
    }
    for(let i = 0; i < s.length - subStrLen + 1; i++) {
        let subStr = s.slice(i, subStrLen + i);
        // 遍历子串，记录子串是否符合要求
        compareSubStr(subStr, strLen, wordsMap) && res.push(i);
    }
    return res;
};

function compareSubStr(str, strLen, map) {
    let newMap = {};
    for(let i = 0; i < str.length; i += strLen) {
        let temp = str.slice(i, i + strLen);
        newMap[temp] ? newMap[temp]++ : newMap[temp] = 1;
    }

    let keys = Object.keys(map);
    for(let key of keys) {
        if(!newMap[key] || newMap[key] != map[key]) {
            return false;
        }
    }

    return true;
}
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@acy925
acy925 commented 2 hours ago
思路
    # 把 s 按 k 分成窗口，每 m 个窗口形成一组
    # 统计该组里的有效单词个数，与给定的单词组匹配个数
代码
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word

                if w not in words:# 如果新的word不是给定的 word，则删除窗口，重新统计
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:             # 如果新的word是给定的 word，则更新窗口hashmap
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                if cur_cnt == word_num :
                        res.append(left)
        return res
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@catkathy
catkathy commented 1 hour ago
思路
滑动窗口

Code
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = len(words) * word_length
        word_freq = Counter(words)
        result = []

        for i in range(len(s) - total_length + 1):
            seen = {}
            for j in range(i, i + total_length, word_length):
                curr_word = s[j:j + word_length]
                if curr_word not in word_freq or seen.get(curr_word, 0) >= word_freq[curr_word]:
                    break
                seen[curr_word] = seen.get(curr_word, 0) + 1
            else:
                result.append(i)

        return result
