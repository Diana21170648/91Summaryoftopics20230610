【Day 45 】2023-07-24 - 438. 找到字符串中所有字母异位词 #47
Open
azl397985856 opened this issue yesterday · 7 comments
Comments
@azl397985856
azl397985856 commented yesterday
438. 找到字符串中所有字母异位词
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

前置知识
Sliding Window
哈希表
题目描述
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
@Diana21170648
Diana21170648 commented now
思路
滑动窗口

代码
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        ans = []
        for i in range(len(s)):
            if i >= len(p):
                target[s[i - len(p)]] += 1
                if target[s[i - len(p)]] == 0:
                    del target[s[i - len(p)]]
            target[s[i]] -= 1
            if target[s[i]] == 0:
                del target[s[i]]
            if len(target) == 0:
                ans.append(i - len(p) + 1)
        return ans
复杂度分析

时间复杂度：O(N)，其中 N 为str长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 滑动窗口 45 labels yesterday
@freesan44
freesan44 commented 15 hours ago
class Solution {
    func findAnagrams(_ s: String, _ p: String) -> [Int] {
        var target = [Character: Int]()
        var ans = [Int]()
        
        for char in p {
            target[char, default: 0] += 1
        }
        
        for i in 0..<s.count {
            if i >= p.count {
                let charToRemove = s[s.index(s.startIndex, offsetBy: i - p.count)]
                target[charToRemove] = (target[charToRemove] ?? 0) + 1
                if target[charToRemove] == 0 {
                    target[charToRemove] = nil
                }
            }
            
            let charToAdd = s[s.index(s.startIndex, offsetBy: i)]
            target[charToAdd, default: 0] -= 1
            if target[charToAdd] == 0 {
                target[charToAdd] = nil
            }
            
            if target.isEmpty {
                ans.append(i - p.count + 1)
            }
        }
        
        return ans
    }
}
@GuitarYs
GuitarYs commented 13 hours ago
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        target = Counter(p)
        
        left = 0
        current = Counter(s[:len(p)])
        
        while left <= len(s) - len(p):
            if current == target:
                result.append(left)
                
            if current[s[left]] > 1:
                current[s[left]] -= 1
            else:
                del current[s[left]]
            
            if left + len(p) < len(s):
                current[s[left + len(p)]] += 1
            
            left += 1
        
        return result
@catkathy
catkathy commented 6 hours ago
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        HashMap<Character, Integer> window_map = new HashMap<>();
        HashMap<Character, Integer> p_map = new HashMap<>();
        for (int i = 0; i < p.length(); i++){
            char c1 = p.charAt(i);
            p_map.put(c1, p_map.getOrDefault(c1, 0) + 1);
        }
        int left, right, count;
        left = right = count = 0;
        ArrayList<Integer> res = new ArrayList<>();
        
        while(right < s.length()){
            char c = s.charAt(right);
            right++;
            if (p_map.containsKey(c)){
                window_map.put(c, window_map.getOrDefault(c, 0) + 1);
                if(window_map.get(c).equals(p_map.get(c))){
                    count++;
                }
            }
            while(right - left == p.length()){
                if (count == p_map.size()){
                    res.add(left);
                }
                char d = s.charAt(left);
                left++;
                if (p_map.containsKey(d)){
                    if (window_map.get(d).equals(p_map.get(d))){
                        count--;
                    }
                    window_map.put(d, window_map.getOrDefault(d, 0) -1);
                }
            } 
        }
        return res;  
    }
}
@jennyjgao
jennyjgao commented 3 hours ago
public class MedianFindAnagrams438 {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<Integer>();
        if (s.length() < p.length()) {
            return res;
        }
        int[] pcount = new int[26];
        int[] scount = new int[26];

        for (int i = 0; i < p.length(); i++) {    //记录第一组p长度的字符是否符合条件
            scount[s.charAt(i) - 'a']++;
            pcount[p.charAt(i) - 'a']++;
        }
        if (Arrays.equals(scount, pcount)) {
            res.add(0);
        }
        for (int i = 0; i < s.length() - p.length(); i++) {    //将第一组的第一个字符数量减去
            scount[s.charAt(i) - 'a']--;
            //将窗口移动到第二组的最后一个字符的位置
            scount[s.charAt(i + p.length()) - 'a']++;
            if (Arrays.equals(scount, pcount)) {
                res.add(i + 1);
            }
        }
        return res;
    }
}
@Beanza
Beanza commented 53 minutes ago
class Solution {
func findAnagrams(_ s: String, _ p: String) -> [Int] {
var target = Character: Int
var ans = Int

    for char in p {
        target[char, default: 0] += 1
    }
    
    for i in 0..<s.count {
        if i >= p.count {
            let charToRemove = s[s.index(s.startIndex, offsetBy: i - p.count)]
            target[charToRemove] = (target[charToRemove] ?? 0) + 1
            if target[charToRemove] == 0 {
                target[charToRemove] = nil
            }
        }
        
        let charToAdd = s[s.index(s.startIndex, offsetBy: i)]
        target[charToAdd, default: 0] -= 1
        if target[charToAdd] == 0 {
            target[charToAdd] = nil
        }
        
        if target.isEmpty {
            ans.append(i - p.count + 1)
        }
    }
    
    return ans
}
}

@Fuku-L
Fuku-L commented 5 minutes ago
代码
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        if(s.length() < p.length()){
            return new ArrayList<Integer>();
        }
        List<Integer> res = new ArrayList<>();
        int sLen = s.length();
        int pLen = p.length();
        int[] sCnt = new int[26];
        int[] pCnt = new int[26];
        for(int i = 0; i<pLen; i++){
            sCnt[s.charAt(i) - 'a']++;
            pCnt[p.charAt(i) - 'a']++;
        }
        if(Arrays.equals(sCnt, pCnt)){
            res.add(0);
        }
        for(int i = 0; i<sLen - pLen; i++){
            sCnt[s.charAt(i) - 'a']--;
            sCnt[s.charAt(i+pLen) - 'a']++;   
            if(Arrays.equals(sCnt, pCnt)){
                res.add(i+1);
            }
        }
        return res;
    }
}
