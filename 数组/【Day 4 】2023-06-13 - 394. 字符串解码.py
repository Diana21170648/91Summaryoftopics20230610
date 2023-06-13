【Day 4 】2023-06-13 - 394. 字符串解码 #5
Open
azl397985856 opened this issue 16 hours ago · 9 comments
Open
【Day 4 】2023-06-13 - 394. 字符串解码
#5
azl397985856 opened this issue 16 hours ago · 9 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
394. 字符串解码
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/decode-string/

前置知识
栈
括号匹配
题目描述
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

@Diana21170648
Diana21170648 commented now
思路
dfs+栈 递归

代码
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(start):
            rstr=rcnt=''#rstr为重复的字符串，rcnt为出现的重复的数字
            while start<len(s):
                if s[start].isnumeric():#是数字，可能有多位
                    rcnt+=s[start]
                elif s[start]=='[':#遇见左括号，开始递归
                    start,tstr=dfs(start+1)#更新指针
                    rstr=rstr+tstr*int(rcnt)
                    rcnt=''#清空重复的数字
                elif s[start]==']':#遇见右括号，则一次dfs结束
                    return start,rstr
                else:
                    rstr+=s[start]
                start+=1
            return rstr
        return dfs(0)#递归的入口
复杂度分析

时间复杂度：O(N)，其中 N 为解码后s的长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added 栈 DFS 4 labels 16 hours ago
@SoSo1105
SoSo1105 commented 7 hours ago
思路
用python中的正则表达式实现（逐层替换）

代码
class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            s = re.sub(r'(\d+)\[([A-Za-z]*)\]', lambda m:int(m.group(1)) * m.group(2), s)
        return s
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@zhaoygcq
zhaoygcq commented 7 hours ago
思路
使用栈对字符进行存储;

遍历当前字符串，如果字符不是一个']'，直接入栈。
如果当前字符是一个']';则需要将栈中的一部分数据进行弹出：
弹出数据时，若当前字符是在'['字符之前出栈的都是普通字符；
在'['之后弹出的是数字；拿到数字过后，直接进行字符串重建x = str.repeat(y);
注意：上一步重建的字符串还需要添加会栈中(保证最终的字符串中各子串的相对位置不变)
遍历完成，根据栈中内容，完成整体结果输出
代码
/**
 * @param {number} maxSize
 */
/**
 * @param {string} s
 * @return {string}
 */
const decodeString = (s) => {
    let stack = [];
    let temp = [];
    let num = [];
    for(let i = 0; i < s.length; i++) {
        if(s[i] !== ']') {
            stack.push(s[i]);
        } else {
            // 取出字符出栈
            while(stack[stack.length - 1] !== '[') {
                temp.unshift(stack.pop());
            }
            // 需要将'['出栈
            stack.pop();

            // 取出数字
            while(/\d/.test(stack[stack.length - 1])) {
                num.unshift(stack.pop())
            }

            let numStr = Number(num.join(""));
            let str = temp.join("");
            num.length = 0;
            temp.length = 0;
            stack.push(str.repeat(numStr));
        }
    }
    return stack.join("");
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@bi9potato
bi9potato commented 4 hours ago
Approch
Nested brackets require concatenating strings from inside out, which corresponds to LIFO property of stack.

Traverse each char in string s:

If c == '[', push multiplier and string into the stack.

If c == ']',

Pop the multiplier and string from stack.
Multiply the current string by the popped multiplier and concatenate it with the popped string.
If c == digit, concatenate and record it.

If c == char, append it to the current string.

Note:
Implement the stack using LinkedList/ ArrayDeque (not thread-safe) cuz they're faster than Stack (thread-safe).
StringBuilder (not thread-safe) is faster than StringBuffer(thread-safe).
Code
class Solution {
    public String decodeString(String s) {

        Deque<Integer> n_stack = new LinkedList<>();
        Deque<StringBuilder> s_stack = new LinkedList<>();

        StringBuilder sb = new StringBuilder();
        int n = 0;

        for( int i = 0; i < s.length(); i++) {

            char c = s.charAt(i);

            if (c >= '0' && c <= '9') {
                n = n*10 + c-'0';
            } else if (c == '[') {
                n_stack.push(n);
                n = 0;
                s_stack.push(sb);
                sb = new StringBuilder();
            } else if (c == ']') {

                int temp_n = n_stack.pop(); 
                StringBuilder temp_sb = new StringBuilder();
                for(int j = 0; j < temp_n; j++) {
                    temp_sb.append(sb);
                }

                sb = s_stack.pop().append(temp_sb);
            } else { // c == char
                sb.append(c);
            }

        }

        return sb.toString();
        
    }
}
Complexity Analysis
Time: 
Space: 
@snmyj
snmyj commented 2 hours ago
class Solution {
public:
    string decodeString(string s) {
        stack<char> ss;
        string obj,ans="";
        int cnt,bit;
        for(int i=0;i<s.size();i++){
            if(s[i]==']'){
               obj="";
               cnt=0;
               bit=1;
               while(ss.top()!='['){
                    obj+=ss.top();
                    ss.pop();
               }
               reverse(obj.begin(),obj.end());
            
               ss.pop();
              
               while(!ss.empty()&&ss.top()>='0'&&ss.top()<='9'){
                   cnt+=(ss.top()-'0')*bit;
                   bit*=10;
                   ss.pop();

               }

             
               for(int i=0;i<cnt;i++){
                   for(auto &x:obj) ss.push(x);
               }

            
               
            }
            else ss.push(s[i]);
        }

        while(!ss.empty()) {
            ans+=ss.top();
            ss.pop();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};

T(o(k*n)) k是括号中字符数的平均个数。

@huizsh
huizsh commented 2 hours ago
class Solution:
def decodeString(self, s: str) -> str:
stack = []
for c in s:
if c == ']':
repeatStr = ''
repeatCount = ''
while stack and stack[-1] != '[':
repeatStr = stack.pop() + repeatStr
# pop 掉 "["
stack.pop()
while stack and stack[-1].isnumeric():
repeatCount = stack.pop() + repeatCount
stack.append(repeatStr * int(repeatCount))
else:
stack.append(c)
return "".join(stack)

@YQYCS
YQYCS commented 1 hour ago
思路
⽤栈处理，遇到 "["，就要开始重复字符串了，另外重复的数字是可能存在多位的，
所以需要往前找到不为数字的那⼀位，把数字转换出来。
最后⽤把 stack ⾥⾯的字符串都串联起来即可

class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)
复杂度
时间复杂度: O(n)
空间复杂度：O(n)

@wzbwzt
wzbwzt commented 1 hour ago
/*
思路:
栈思路,遍历s,压入栈，遇到']'弹栈
只有四种可能出现的字符: 字母\ 数字(可能对位)\ [ \ ]

复杂度：
时间复杂度为O(n)
空间复杂度为O(n)
*/

func decodeString(s string) string {
	stack := []string{}
	last := []int{}
	tmpCount := ""
	for _, v := range s {
		if unicode.IsDigit(v) {
			tmpCount += string(v)
			continue
		}

		if len(tmpCount) != 0 {
			stack = append(stack, tmpCount)
			tmpCount = ""
		}

		if v == '[' {
			last = append(last, len(stack))
		}
		if v == ']' {
			new := last[len(last)-1]
			num := stack[new-1]
			value := make([]string, len(stack)-new-1)
			copy(value, stack[new+1:])
			stack = stack[:new-1]
			num_i, _ := strconv.Atoi(string(num))
			for i := 0; i < num_i; i++ {
				stack = append(stack, strings.Join(value, ""))
			}
			last = last[:len(last)-1]
			continue
		}

		stack = append(stack, string(v))
	}
	return strings.Join(stack, "")
}
@Alexno1no2
Alexno1no2 commented 1 hour ago
class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        for item in s:
            if item == ']':
                strs = []
                repeat = []
                while res[-1] != '[':
                    strs.insert(0,res.pop())
                res.pop()
                while res and res[-1].isdigit():
                    repeat.insert(0,res.pop())
                res.append(int(''.join(repeat))*''.join(strs))
                continue 
            res.append(item)
            
        return ''.join(res)

