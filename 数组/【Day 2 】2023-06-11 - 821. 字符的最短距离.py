【Day 2 】2023-06-11 - 821. 字符的最短距离 #3
Open
azl397985856 opened this issue 2 days ago · 42 comments
Open
【Day 2 】2023-06-11 - 821. 字符的最短距离
#3
azl397985856 opened this issue 2 days ago · 42 comments
Comments
@azl397985856
azl397985856 commented 2 days ago
821. 字符的最短距离
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/shortest-distance-to-a-character

前置知识
数组的遍历(正向遍历和反向遍历)
题目描述
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:

- 字符串 S 的长度范围为 [1, 10000]。
- C 是一个单字符，且保证是字符串 S 里的字符。
- S 和 C 中的所有字母均为小写字母。

@azl397985856 azl397985856 added 字符串 2 labels 2 days ago
@bi9potato
bi9potato commented 2 days ago • 
Aproach
Forward and backward traversal

Code
class Solution {
    public int[] shortestToChar(String s, char c) {


        int len = s.length();
        int c_idx = -len;

        int[] res = new int[len];
        
        // Traverse from left
        // Calculate distance from each char to the nearest c on its left
        for (int i = 0; i <len; i++) {
            if (s.charAt(i) == c) c_idx = i;
            res[i] = i-c_idx;
        }

        // Traverse from right
        // Calculate distance from each char to the nearest c on its right
        // compare two distances to keep the shortest one
        for (int i = c_idx; i > -1; i-- ) {
            if (s.charAt(i) == c) c_idx = i;
            res[i] = Math.min(res[i], c_idx-i);
        }

        return res;

    }
}
Complexity Analysis

time 
space 
@acy925
acy925 commented 2 days ago • 
思路
将问题分解为两次遍历数组。
首先，从左到右遍历，同时维护一个记录字符 s 位置的变量 prev。记录数组每个元素到该变量的距离 i - prev。（注：变量初始值为负无穷）
然后，从右到左遍历，同时维护一个记录字符 s 位置的变量 prev。记录数组每个元素到该变量的距离 prev - i。（注：变量初始值为正无穷）
最后，比较上述两个距离，最小值为结果。

代码
class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@YizheWill
YizheWill commented yesterday
Traverse from left, then right.

def shortest_to_char(s, c)
  prev = -Float::INFINITY
  ans = []

  s.each_char.with_index do |x, i|
    prev = i if x == c
    ans << i - prev
  end
  
  prev = Float::INFINITY
  (s.length - 1).downto(0) do |i|
    prev = i if s[i] == c
    ans[i] = [ans[i], prev - i].min
  end
  
  ans
end
Time complexity: O(n)
Space complexity: O(n)
@qiaojunch
qiaojunch commented yesterday • 
思路：
## two pointers
## 1. iterate over s and find the indices of c.
## 2. iterate over s again, use a pointer j to record the closest c to s[i].
## 3. find the smallest dist,
### if i < the left most c, ans = pos_of_c[0] - i
###. if i > the right most c, ans = i - pos_of_c[-1]
###. else, ans = whichever is close to i

代码：

    pos, ans, n = [], [], len(s)
    for i in range(n):
        if s[i] == c:
            pos.append(i)

    j = 0 # point to the closest c to char in s
    for i in range(n):
        if s[i] == c:  
            ans.append(0)
            j += 1
        elif i < pos[0]:
            ans.append(pos[0] - i)
        elif i > pos[-1]:
            ans.append(i - pos[-1])
        else:
            dist_to_left = i - pos[j-1]
            dist_to_right = pos[j] - i
            ans.append(min(dist_to_left, dist_to_right))
    return ans
复杂度：
time：o(n)
space: o(n)

@hjy-u
hjy-u commented yesterday • 
traverse left -> right then right -> left

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [0]*len(s)
        idx = float('-inf')
        for i, ch in enumerate(s):
            if ch == c:
                idx = i
            answer[i] = i - idx
        for i in range(idx, -1, -1):
            if s[i] == c:
                idx = i
            answer[i] = min(answer[i], idx - i)
        return answer
time: O(N)
space: O(N)

@guangsizhongbin
guangsizhongbin commented yesterday
题目地址(821. 字符的最短距离)
https://leetcode.cn/problems/shortest-distance-to-a-character/

题目描述
给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。

返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。

两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。

 

示例 1：

输入：s = "loveleetcode", c = "e"
输出：[3,2,1,0,1,0,0,1,2,2,1,0]
解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。


示例 2：

输入：s = "aaab", c = "b"
输出：[3,2,1,0]


 

提示：
1 <= s.length <= 104
s[i] 和 c 均为小写英文字母
题目数据保证 c 在 s 中至少出现一次
前置知识
公司
暂无
思路
关键点
代码
语言支持：Go
Go Code:

func shortestToChar(s string, c byte) []int {

	var res []int = make([]int, len(s))

    cur := math.MaxInt

    // 1. 从前往后
    for index, char := range s {
        if char == int32(c) {
            cur = index
        }

        if cur == math.MaxInt {
            res[index]  = math.MaxInt
        } else {
            res[index] = index - cur
        }
    }

    // 2. 从后往前
    cur = math.MaxInt
    for index := len(s) - 1; index >= 0 ; index-- {
        char := s[index]

        if char == c {
            cur = index
        }

        abs := cur - index
        if res[index] > abs {
            res[index] = abs
        }
    }

    return res
}
复杂度分析

令 n 为数组长度。

时间复杂度：$O(n)$
空间复杂度：$O(n)$
@SoSo1105
SoSo1105 commented yesterday
思路
数组的遍历

代码
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexList = []
        for index,val in enumerate(s):
            if val == c:
                indexList.append(index)
        resList = []
        p = 0
        # print(indexList)
        for index,val in enumerate(s):
            # print(index)
            if p < len(indexList)-1 and (abs(index-indexList[p]) > abs(index-indexList[p+1])):
                p += 1
            resList.append(abs(index-indexList[p]))
        return resList
复杂度分析

时间复杂度：O(N)
空间复杂度：O(1)
@zhaoygcq
zhaoygcq commented yesterday
思路
遍历字符串；

创建一个结果数组res，长度与字符串长度相同；并对每一个数组项赋初值Infinity;
如果当前字符的值于目标字符c相同，那当前的res[i] = 0,并以当前位置向两边发散：如果一个字符到当前字符的距离比他原有的值要小(res[j] > i - j)，那就对其进行重新赋值；反之则终止此次发散。
最终返回结果数组res
代码
/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
    const len = s.length;
    let res = new Array(len).fill(Infinity);
    for(let i = 0; i < len; i++) {
        if(s[i] === c) {
            res[i] = 0;
            for(let j = i - 1; j >= 0; j--) {
                if(res[j] > i - j) {
                    res[j] = i - j;
                } else {
                    break;
                }
            }

            for(let j = i + 1; j < len; j++) {
                if(res[j] > j - i) {
                    res[j] = j - i;
                } else {
                    break;
                }
            }
        }
    }

    return res;
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@mo660
mo660 commented yesterday
思路
记录每一c在s中的位置
遍历s，计算出每一个字符与c位置的最小值
代码
class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> coordinate;
        for(int i = 0; i < s.length(); i++)
        {
            if (s[i] == c)
            {
                coordinate.push_back(i);
            }
        }
        vector<int> res;
        for(int i = 0; i < s.length(); i++)
        {
            int tmp = INT32_MAX;
            for(auto it : coordinate)
            {
                tmp = min(tmp, abs(i-it));
            }
            res.push_back(tmp);
        }
        return res;
    }
};
复杂度
时间O(n+k)

空间O(k)

@dorian-byte
dorian-byte commented yesterday
思路：

这段代码的思路是找出字符串 s 中每个字符到目标字符 c 的最短距离。代码通过两次遍历实现这一目标：一次正向遍历，一次反向遍历。

在正向遍历中，使用变量 prev 记录上一个目标字符 c 的位置。对于每个字符 s[i]，如果它是目标字符 c，则更新 prev 为当前位置 i。然后计算 res[i] 为当前位置 i 减去 prev 的距离，表示当前字符到上一个目标字符的距离。

在反向遍历中，同样使用变量 prev 记录上一个目标字符 c 的位置。对于每个字符 s[i]，如果它是目标字符 c，则更新 prev 为当前位置 i。然后计算 res[i] 为当前位置 i 和 prev 的距离的最小值，表示当前字符到下一个目标字符的距离。

最终，返回结果列表 res，其中包含了每个字符到目标字符的最短距离。

代码：

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [float('inf')] * len(s)
        prev = float('-inf')

        # Forward pass
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            res[i] = i - prev

        prev = float('inf')

        # Backward pass
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)

        return res
复杂度分析：

时间复杂度：代码中使用两次遍历，正向遍历和反向遍历，因此时间复杂度为 O(N)，其中 N 是字符串 s 的长度。

空间复杂度：代码中使用了结果列表 res 和两个变量 prev，因此空间复杂度为 O(N)，其中 N 是字符串 s 的长度。

@YQYCS
YQYCS commented yesterday
功能
实现了一个函数，输入一个字符串s和一个字符c，输出一个列表，列表中的每个元素表示s中对应位置到字符c的最短距离。
算法思路
遍历字符串s中的每个字符，如果该字符就是c，则距离为0，否则向左向右分别查找最近的一个字符c，并计算距离。最后取左右距离中的较小值作为该位置到字符c的最短距离。
时间复杂度
因为对于每个字符，都需要向左向右查找最近的字符c，最坏情况下需要遍历整个字符串两遍，所以时间复杂度为O(n)。
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(s)):
            if (i == 0 or i == len(s)-1) and s[i] == c:
                res.append(0)
            else:
                j, k = i, i
                m, n = 0, 0
                while(s[j] != c):
                    j += 1
                    m += 1
                    if j > len(s)-1:
                        m = float("inf")
                        break
                while(s[k] != c): 
                    k -= 1
                    n += 1
                    if k < 0:
                        n = float("inf")
                        break
                res.append(min(m,n))
        return res
@zhouliuhuo
zhouliuhuo commented yesterday
class Solution {
public int[] shortestToChar(String s, char c) {
String[] split = s.split("");
ArrayList indexs = new ArrayList<>();
for (int i = 0; i < split.length; i++) {
String s1 = split[i];
if (String.valueOf(c).equals(s1)) {
indexs.add(i);
}
}

    int[] shortes = new int[split.length];
    for (int i = 0; i < shortes.length; i++) {
        if (indexs.contains(i)) {
            shortes[i] = 0;
        } else {
            int min = split.length;
            for (Integer index : indexs) {
                min = Integer.min(min, Math.abs(index - i));
            }
            shortes[i] = min;
        }
    }
    return shortes;
}
}

@catkathy
catkathy commented yesterday
思路
iterating through the string s while calculating the occurrence of character C.

Code
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        n = len(s)
        ans = [0] * n
        j = float('-inf')
        
        for i, ch in enumerate(s):
            if ch == c:
                j = i
            ans[i] = i - j
        
        j = float('inf')
        
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                j = i
            ans[i] = min(ans[i], j - i)
        
        return ans
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(n)
@snmyj
snmyj commented yesterday
class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> pos,ans;
       for(int i=0;i<s.length();i++){
           if(s[i]==c) pos.push_back(i);
       }
       for(int i=0;i<s.length();i++){
           if(s[i]==c) ans.push_back(0);
           else{
               int min=INT_MAX;
               for(int j=0;j<pos.size();j++){
                  if(abs(pos[j]-i)<min) min=abs(pos[j]-i);
               }
               ans.push_back(min);
           }
       }
       return ans;
    }
};
@zhuxinyu-znb
zhuxinyu-znb commented yesterday
思路
左到右遍历一遍记录位置的同时记录一遍到c的距离
再从右到左遍历比较取最小值

代码
/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
    let n = s.length
    const res = new Array(n).fill(0)
    for(let i = 0, x = -n; i < n; ++i) {
        if (s[i] === c) {
            x = i
        }
        res[i] = i - x
    }
    for(let j = n - 1, y = 2 * n; j >= 0; --j) {
        if (s[j] === c) {
            y = j
        }
        res[j] = Math.min(res[j], y - j)
    }
    return res
};
复杂度
O(n)

@Diana21170648
Diana21170648 commented yesterday
思路
数组从两端遍历

代码
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        res=[]
        #标记字符c的位置，有则标记为0，没有则标记为None
        for i in range(n):
            if s[i]==c:
                res.append(0)
            else:
                res.append(None)
        #只需要遍历非0的位置
        #从左向右遍历
        for i in range(1,n):
            if res[i] !=0 and res[i-1] is not None:
                res[i]=res[i-1]+1
        #从右向左遍历
        for i in range(n-2,-1,-1):
            if res[i] is None or res[i+1]+1 < res[i]:
                res[i]=res[i+1]+1
        return res
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)
@joemonkeylee
joemonkeylee commented yesterday
function shortestToChar(s: string, c: string): number[] {
  const N = s.length;
  let res: number[] = new Array(N).fill(Number.MAX_SAFE_INTEGER);

  let prev = 0;
  for (let i = 0; i < N; i++) {
    if (s[i] == c) {
      for (let j = prev; j <= i; j++) {
        res[j] = i - j;
      }
      prev = i;
    }
  }

  prev = N - 1;
  for (let i = N - 1; i >= 0; i--) {
    if (s[i] == c) {
      for (let j = prev; j >= i; j--) {
        res[j] = Math.min(res[j], j - i);
      }
      prev = i;
    }
  }
  return res;
}
@Miller-em
Miller-em commented yesterday
思路
首先记录每一个目标字符的位置，然后再对s字符串进行遍历，对每个位置计算目标字符的位置的绝对值，找出最小的那个。

代码
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        e_indexes = []
        res = []

        # 记录每一个e的位置
        for i in range(len(s)):
            if s[i] == c:
                e_indexes.append(i)
        
        # 计算每一个位置跟目标的距离
        for i in range(len(s)):
            index = min([abs(i-e) for e in e_indexes])
            res.append(index)
        return res
复杂度
时间复杂度 O(N^2)
空间复杂度 O(N)

@freesan44
freesan44 commented 19 hours ago
代码
class Solution821 {
    func shortestToChar(_ S: String, _ C: Character) -> [Int] {
        var result = [Int]()
        for (i, char) in S.enumerated() {
            if char == C {
                result.append(0)
            } else {
                var left = i
                var right = i
                while left >= 0 || right < S.count {
                    if left >= 0 && S[S.index(S.startIndex, offsetBy: left)] == C {
                        result.append(i - left)
                        break
                    }
                    if right < S.count && S[S.index(S.startIndex, offsetBy: right)] == C {
                        result.append(right - i)
                        break
                    }
                    left -= 1
                    right += 1
                }
            }
        }
        return result
    }
    func test() {
        var s = "loveleetcode"
        var c: Character = "e"
        let ret = shortestToChar(s,c);
        print(ret);
    }
}
@yzhyzhyzh123
yzhyzhyzh123 commented 18 hours ago
思路
分别从前往后，从后往前遍历，取这两个中较小的一个就是答案最近的距离。

代码
class Solution {
    public int[] shortestToChar(String s, char c) {
        int len = s.length();
        int[] res = new int[len];
        int index = -len;
        // 从左往右，第一次遍历记录下s[i]左边最近的一个c字符
        for (int i = 0; i < len; i++) {
            if (s.charAt(i) == c) {
                index = i;
            }
            res[i] = i - index;
        }
        index =  len  * 2;
        // 第二次遍历记录下s[i]右边最近的一个c字符，从右向左
        // 取这两个中较小的一个，这就是距离c字符最近的
        for (int i = len - 1; i >= 0; --i) {
            if (s.charAt(i) == c) {
                index = i;
            }
            res[i] = Math.min(res[i], index - i);
        }
        return res;
    }
}
复杂度
时间复杂度：O(n)，需要遍历两次字符串的所有字符。
空间复杂度：O(1)，只需常数的空间。

@jameswangxin
jameswangxin commented 18 hours ago
 class Solution {
    public int[] shortestToChar(String s, char c) {
        int n = s.length();
        int lp = -n, rp= -n;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == c) {
                lp = i;
            } else {
                int diff = Math.abs(i-lp);
                ans[i] = diff;
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == c) {
                rp = i;
            } else {
                if (rp == -1) {
                    continue;
                }
                int diff = Math.abs(i-rp);
                ans[i] = Math.min(ans[i], diff);
            }
        }
        return ans;
    }
}
正向遍历一遍数组，如果当前遍历到的字符是题目中给定的字符，那么记录一下此时字符出现的位置，否则更新一下当前字符与给的字符的下标差；反向遍历数组也是做类似的操作，遍历的同时与第一次正向遍历数组计算出的距离差两者取较小值作为当前位置的最终结果。

时间复杂度 : O(n)

空间复杂度: O(n)

@C2tr
C2tr commented 18 hours ago
class Solution:
def shortestToChar(self, s: str, c: str) -> List[int]:
res = [float('inf')] * len(s)
prev = float('-inf')

    # Forward pass
    for i in range(len(s)):
        if s[i] == c:
            prev = i
        res[i] = i - prev

    prev = float('inf')

    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev = i
        res[i] = min(res[i], prev - i)

    return res
@MetSystem
MetSystem commented 17 hours ago
using System;
using System.Collections.Generic;

public class Program
{
public static void Main()
{
Console.WriteLine("Hello World");
string S = "loveleetcode";
char C = 'e';
int [] result = get(S,C);
for(int i =0 ;i<result.Length;i++){
Console.WriteLine(result[i]+",");
}
}

public static int[] get(string s, char c){
	    List<int>  cList = new List<int>();
        for(int i =0 ;i<s.Length;i++){
            if(s[i]== c){ cList.Add(i); }
        }
        int[] result = new int[s.Length];
		for(int j = 0 ;j<s.Length;j++){
			if(s[j] == c){
				result[j]= 0;
			}else{
				int cI = 0;
				int mI = 0;
				for(int k = 0 ;k<cList.Count;k++){
					if(cList[k]>j){
						cI =cList[k] -j;
					}else{
						cI = j -cList[k];
					}
					if(mI== 0  || cI<mI){
						mI	= cI ;
					}
				}	
				result[j]=mI;
				
			}
				
		}

        return result;
	}
}
@RanDong22
RanDong22 commented 17 hours ago
解题思路
先获取到对应的字母位于数组中的所有下标idxs
重新遍历 s，从idxs[0]和idxs[1]开始，用 last 和next存储当前对比的下标， idx 存储当前对比的索引，用当前下标对比，取 i - index[0] 和 i - index[1]的绝对值中较小的一个放入结果中
当i === next的时候， 重置last, next ,idx

代码
var shortestToChar = function (s: string, c: string) {
  let idxs = [];
  let final = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === c) {
      idxs.push(i);
    }
  }
  idxs.push(999999999999);
  let last = idxs[0];
  let next = idxs[1];
  let idx = 1;
  for (let i = 0; i < s.length; i++) {
    final.push(Math.min(Math.abs(last - i), next - i));
    if (i === next) {
      idx++;
      last = next;
      next = idxs[idx];
    }
  }
  return final;
};
@Beanza
Beanza commented 17 hours ago
##思路
将字符串放进一个数组 将字符C从左到右进行遍历 当C==idex[i]时，记录下标index。将index 与其他字符下标相减放进新的数组里并返回。
##代码
##复杂度
O(n)

@kingxiaozhe
kingxiaozhe commented 17 hours ago
function shortestToChar(S, C) {
  const result = [];

  for (let i = 0; i < S.length; i++) {
    let minDistance = Infinity;

    for (let j = 0; j < S.length; j++) {
      if (S[j] === C) {
        minDistance = Math.min(minDistance, Math.abs(i - j));
      }
    }

    result.push(minDistance);
  }

  return result;
}

@beginner-jamji
beginner-jamji commented 17 hours ago
思路
首先应该获取到该字符在字符串 s 中的所有下标位置，遍历一次字符串，并将等于目标字符的下标添加至动态数组arr中，使用指针比较下标间的最短距离。

代码
class Solution:
def shortestToChar(self, s: str, c: str) -> List[int]:
res, p, arr = [], 0, [i for i in range(len(s)) if s[i] == c]
for i, j in enumerate(s):
if p < len(arr) - 1 and abs(arr[p] - i) > abs(arr[p + 1] - i):
p += 1
res.append(abs(arr[p] - i))
return res

复杂度
时间复杂度O(n)
空间复杂度O(n)

@SunStrongChina
SunStrongChina commented 17 hours ago • 
思路：先找到c字符所在的位置，然后遍历字符数据（不是离左边近就是离右边近），两个一比较取最近

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ##先找到c的1位置
        indexs = []
        for i,s1 in enumerate(s):
            if s1 == c:
                indexs.append(i)
        result = []
        i = 0
        for j in range(len(indexs)):
            while i <= indexs[j]:
                if j-1 >=0:
                    minDis = abs(indexs[j] -i)
                    if i -indexs[j-1] < minDis:
                        minDis = i -indexs[j-1]
                else:
                    minDis = abs(indexs[j] - i)
                result.append(minDis)
                i +=1
        while i < len(s):
            result.append(i - indexs[-1])
            i += 1
        return result
时间复杂度：o(n)
空间复杂度: o(n)

@Beanza
Beanza commented 17 hours ago via email 
感谢您的解答！
对于改题目的解题思路我已经了解，但是并不能理解用js语法写的代码。目前仅掌握C语言，请问如何跟上进度？




Beanzacute
***@***.***



&nbsp;
…
@GuitarYs
GuitarYs commented 17 hours ago
class Solution:
    def shortestToChar(self, s:str, c:str) : #指定s、c的类型
        n = len(s)
        answer = [0] * n
        print('answer的类型',type(answer))
        last_position = -float("inf")
        for i in range(n):
            if s[i] == c:
                last_position = i
            answer[i] = i - last_position

        next_position = float("inf")
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_position = i
            answer[i] = min(answer[i], next_position - i)

        return answer

s = "loveleetcode"
c = "e"
solution = Solution()
ans = solution.shortestToChar(s, c)
print(ans)  # 输出 [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

s = "aaab"
c = "b"
solution = Solution()
ans = solution.shortestToChar(s, c)
print(ans)  # 输出 [3, 2, 1, 0]
@yetfan
yetfan commented 17 hours ago
代码
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n

        idx = -n
        for i, ch in enumerate(s):
            if ch == c:
                idx = i
            ans[i] = i - idx

        idx = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], idx - i)
        return ans
@Erjian96
Erjian96 commented 16 hours ago • 
def solution(s, c):

a = [i for i in range(len(s)) if c == s[i]]
print(a)
b = []

for i in a:

    for x in range(len(s)):

        b.append(min(abs(x-i),abs(len(s)-x-i)))
        
return b
@zcytm3000
zcytm3000 commented 16 hours ago
class Solution:
def shortestToChar(self, s: str, c: str) -> List[int]:
a=[]
b=[]
for i,ch in enumerate(s):
if ch==c:
b.append(int(i))
return([min(abs(x-i) for i in b) for x in range(len(s))])

@61hhh
61hhh commented 16 hours ago
思路
遍历计算每个字符最近的左 c 保存距离、遍历计算每个字符最近的右 c ，取更小值保存距离。每次匹配到 c 就更新下标

代码
class Solution {
    public int[] shortestToChar(String s, char c) {
        int len = s.length();
        int[] res = new int[len];
        int pos = -len;
        // 找到每个字符左边最近的c，计算距离
        for (int i = 0; i < len; i++) {
            if (s.charAt(i) == c) {
                pos = i;
            }
            res[i] = i - pos;
        }
        // 找到每个字符右边最近的c，计算距离，与左c取更小值
        pos = 2 * len;
        for (int i = len - 1; i >= 0; i--) {
            if (s.charAt(i) == c) {
                pos = i;
            }
            res[i] = Math.min(res[i], pos - i);
        }
        return res;
    }
}
复杂度分析
时间复杂度：O(N)
空间复杂度：O(N)
@sosdogecoin
sosdogecoin commented 16 hours ago
def solution(s, c):

a = [i for i in range(len(s)) if c == s[i]]
print(a)
b = []

for i in a:

for x in range(len(s)):

    b.append(min(abs(x-i),abs(len(s)-x-i)))
return b

复杂度分析
时间复杂度：O(N)
空间复杂度：O(N)

@Beanza
Beanza commented 16 hours ago via email 
感谢您的解答！






Beanzacute
***@***.***



&nbsp;
…
@Fuku-L
Fuku-L commented 16 hours ago
class Solution {
    public int[] shortestToChar(String s, char c) {
            int[] res = new int[s.length()];
            int ch = c;
            for (int i = 0; i < s.length(); i++) {
                int a = s.indexOf(ch, i);
                if (a == i) {
                    res[i] = 0;
                } else {
                    res[i] = Math.abs(a - i);
                }
            }
            for (int i = s.length() - 1; i >= 0; i--) {
                int a = s.lastIndexOf(ch, i);
                if (Math.abs(a - i) < res[i]) {
                    res[i] = Math.abs(a - i);
                } else if(a<0){ // 如果找到
                    break;
                }
            }
            return res;
    }
}
@Sencc
Sencc commented 16 hours ago
代码
class Solution:
def shortestToChar(self, s: str, c: str) -> List[int]:
e_indexes = []
res = []

    for i in range(len(s)):
        if s[i] == c:
            e_indexes.append(i)
    
    for i in range(len(s)):
        index = min([abs(i-e) for e in e_indexes])
        res.append(index)
    return res
@yaya-bb
yaya-bb commented 16 hours ago
var shortestToChar = function(s, c) {
    let res = Array(s.length);

    //贪心法
    //先从左到右遍历
    for(let i = 0 ;i <s.length ; i++)
    {
        if(s[i] === c)
        {
            res[i] = i;
        }else{
            //void 0 == undefined)，如果
            res[i] = (res[i-1] === void 0 ? Infinity : res[i-1]);
        }
    }
    //从右往左遍历
    for(let i = s.length -1; i>= 0;i--)
    {
        
        if(res[i] === Infinity || res[i+1] - i < i- res[i])
        {
            res[i] = res[i+1];
        }
    }
    for(let i = 0 ;i <res.length ; i++){
        res[i] = Math.abs(res[i] - i);
    }
    return res;
};
时间复杂度：O(n)
空间复杂度：O(n)
@Alexno1no2
Alexno1no2 commented 16 hours ago
class Solution:
     def shortestToChar(self, s: str, c: str) -> List[int]:
         c_idx = [ i for i in range(len(s)) if s[i] == c ]
         return [ min(abs( i - j )  for j in c_idx) for i in range(len(s)) ]
@YGNAUH
YGNAUH commented 16 hours ago
思路：

1.初始化一个结果数组 res，将其中的每个元素赋值为一个足够大的数。
2.遍历字符串 S，并判断每个位置上的字符是否为目标字符 C：
如果是，则将当前位置的 res 值赋为 0。
如果不是，则分别从左右两个方向开始遍历，记录距离当前位置最近的目标字符的距离，并更新 res 值。
3.返回结果数组 res。

class Solution {
    public int[] shortestToChar(String S, char C) {
        int n = S.length();
        int[] res = new int[n];
        Arrays.fill(res, n);
        int pos = -n;
        for (int i = 0; i < n; i++) {
            if (S.charAt(i) == C) pos = i;
            res[i] = Math.min(res[i], i - pos);
        }
        for (int i = n - 1; i >= 0; i--) {
            if (S.charAt(i) == C) pos = i;
            res[i] = Math.min(res[i], pos - i);
        }
        return res;
    }
}
@wzbwzt
wzbwzt commented 16 hours ago
/*
思路：
遍历数组

复杂度：
空间复杂度为 O(n)
时间复杂度为 O(n)
*/

func shortestToChar(s string, c byte) []int {
	n := len(s)
	res := make([]int, n)

	l := 0
	if s[0] != c {
		l = n
	}
	r := strings.IndexByte(s[1:], c) + 1

	for i := 0; i < n; i++ {
		res[i] = min(abs(i-l), abs(r-i))
		if i == r {
			l = r
			r = strings.IndexByte(s[l+1:], c) + l + 1
		}
	}

	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
