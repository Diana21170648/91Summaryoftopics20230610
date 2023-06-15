768. 最多能完成排序的块 II
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii/

前置知识
栈
单调栈
队列
题目描述
这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。

arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

示例 1:

输入: arr = [5,4,3,2,1]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。
示例 2:

输入: arr = [2,1,3,4,4]
输出: 4
解释:
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。
注意:

arr的长度在[1, 2000]之间。
arr[i]的大小在[0, 10**8]之间。

@Diana21170648
Diana21170648 commented now
思路
单调升序栈，a比栈顶小，则a应该在栈顶的下边，所一栈顶出栈并记为最大值，然后pop所有有比a大的值，直到把a放进栈
如果直接添加，则升序序列还在继续，则栈块数未增加，如果弹出再增加证明升序序列结束，压入元素，栈数增加1

代码
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int: 
        stack=[]
        for a in arr:
            if stack and stack[-1]>a:#单调升序栈，a比栈顶小，则a应该在栈顶的下边，所一栈顶出栈并记为最大值，然后pop所有有比a大的值，直到把a放进栈
            #如果直接添加，则升序序列还在继续，则栈块数未增加，如果弹出再增加证明升序序列结束，压入元素，栈数增加1
                cur=stack[-1]
                while stack and stack[-1]>a:
                    stack.pop()
                stack.append(cur)
            else:
                stack.append(a)
        return len(stack)#stack存的是块信息，栈里存储的是所有块的最大值，栈的大小就是最终划分块的数量
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added 栈 哈希表 6 labels 18 hours ago
@yfu6
yfu6 commented 12 hours ago
class Solution:
def maxChunksToSorted(self, arr: List[int]) -> int:
stack = []

    for num in arr:
        largest = num
        while stack and stack[-1] > num:
            largest = max(largest, stack.pop())
        stack.append(largest)
    
    return len(stack)
@freesan44
freesan44 commented 9 hours ago
思路
计数排序

代码
class Solution768 {
    func maxChunksToSorted(_ arr: [Int]) -> Int {
        // 定义一个变量 ans，用于记录最终的答案
        var ans = 0
        var countA = [Int: Int]()
        var countB = [Int: Int]()
        
        // 遍历 arr 和 arr.sorted()，将它们的每个元素合并成一个元组 (a, b)
        for (a, b) in zip(arr, arr.sorted()) {
            // 在 countA 中增加 a 出现的次数
            countA[a, default: 0] += 1
            // 在 countB 中增加 b 出现的次数
            countB[b, default: 0] += 1
            // 如果 countA 和 countB 相等，那么说明 arr 的前 i 个元素可以分成一个 chunk，并将 ans 加 1
            print(countA,countB)
            if countA == countB {
                ans += 1
            }
        }

        // 返回最终的答案
        return ans
    }
    func test() {
//        var arr = [5,4,3,2,1]
        var arr = [2,1,3,4,4]
        let ret = maxChunksToSorted(arr);
        print(ret);
    }
    
}
@SoSo1105
SoSo1105 commented 8 hours ago
思路
通过单调栈实现逻辑

代码
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for i in arr:
            if stack and stack[-1]>i:
                cur = stack[-1]
                while stack and stack[-1]>i:
                    stack.pop()
                stack.append(cur)
            else:
                stack.append(i)
        return len(stack)



if __name__ == '__main__':
    arr = [5,4,3,2,1]
    result = Solution().maxChunksToSorted(arr)
    print(result)
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@dorian-byte
dorian-byte commented 7 hours ago
思路：

这个问题可以通过一次遍历数组来解决。我们可以使用两个辅助数组mx和mn，其中mx[i]表示从数组开头到第i个位置的最大值，mn[i]表示从数组末尾到第i个位置的最小值。然后，我们遍历数组，对于每个位置i，如果mx[i]小于等于mn[i+1]，说明在位置i可以分割一个新的块，我们将结果加一。最后返回结果即可。

代码：

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        mx, mn = [-1] * n, [float('inf')] * n

        # Calculate max values from the start to current position
        mx[0] = arr[0]
        for i in range(1, n):
            mx[i] = max(mx[i-1], arr[i])
        
        # Calculate min values from the end to current position
        mn[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            mn[i] = min(mn[i+1], arr[i])
        
        # Count all chunk points
        return sum(mx[i] <= mn[i+1] for i in range(n-1)) + 1
复杂度分析：

时间复杂度：遍历数组需要O(n)的时间，其中n是数组的长度。

空间复杂度：需要两个辅助数组mx和mn来存储最大值和最小值，每个数组的长度为n，因此空间复杂度为O(n)。

(以上内容由ChatGPT生成。我通过对比ChatGPT的答案来修改自己写的代码，然后再自己打一遍。)

@YizheWill
YizheWill commented 7 hours ago
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        mx, mn = [-1] * n, [float('inf')] * n

        # Calculate max values from the start to current position
        mx[0] = arr[0]
        for i in range(1, n):
            mx[i] = max(mx[i-1], arr[i])
        
        # Calculate min values from the end to current position
        mn[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            mn[i] = min(mn[i+1], arr[i])
        
        # Count all chunk points
        return sum(mx[i] <= mn[i+1] for i in range(n-1)) + 1
@Miller-em
Miller-em commented 5 hours ago
l## 思路
能够实现题述功能的小子块必须和全部排好序的数组的局部数组内的元素的出现频次是一样的。因此考虑使用哈希表记录频次。

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = Counter()
        res = 0

        for x, y in zip(arr, sorted):
            cnt[x] += 1
            if cnt[x] == 0:
                del cnt[x]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            if len(cnt) == 0:
                res += 1
        return res
@RanDong22
RanDong22 commented 3 hours ago
768
前置知识
双指针

思路
从左到右依次遍历，同时满足以下条件即可分块：

双指针的范围内最大值，不大于下一个值
双指针的范围内最大值，不大于后续范围内的最小值
代码
function maxChunksToSorted(arr: number[]): number {
  let count = 1,
    i = 0,
    j = 1,
    max = arr[i];
  while (j < arr.length) {
    const rMin = Math.min(...arr.slice(j));
    if (max > arr[j] || max > rMin) {
      max = Math.max(max, arr[j]);
      j++;
    } else {
      i = j++;
      max = arr[i];
      count++;
    }
  }
  return count;
}
复杂度
时间复杂度：O(n^2)
空间复杂度：O(1)

@bi9potato
bi9potato commented 3 hours ago
Approach
Code
class Solution {
    public int maxChunksToSorted(int[] arr) {

        Deque<Integer> deq = new LinkedList<>();

        for (int num : arr) {

            if (deq.isEmpty()) {
                deq.push(num);
            } else { // deq is not empty
                int max = deq.peek();
                if (num >= max) {
                    deq.push(num);
                } else { // num < max
                    while (!deq.isEmpty() && deq.peek() > num) {
                        deq.pop();
                    }
                    deq.push(max);
                }
            }


        }

        return deq.size();

    }
}
Complexity Analysis
Time 
Space 
@Alexno1no2
Alexno1no2 commented 2 hours ago
单调栈个数，其中单调栈中的每一个元素代表每一块中的最大值。
class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]: 
                head = stack.pop()
                while stack and num < stack[-1]: 
                    stack.pop()
                stack.append(head)
            else: stack.append(num)
        print(stack)
        return len(stack)

@catkathy
catkathy commented 14 minutes ago
Code
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for value in arr:
            if not stack or value >= stack[-1]:
                stack.append(value)
            else:
                max_value = stack.pop()
                while stack and stack[-1] > value:
                    stack.pop()
                stack.append(max_value)
        return len(stack)
复杂度分析：
Time: O（n)
Space: O(n)
Space:
@Master-guang
Master-guang commented 9 minutes ago
思路：要想划分最多的块，并且保证排序后的结果和原数组的排序结果相同，则块中的元素必须保证，块中的最大值都比右边的元素小或者相同，块中的最小值都比左边的元素大或者相同。
var maxChunksToSorted = function(arr) {
  const stack = [];
  for (const num of arr) {
      if (stack.length === 0 || num >= stack[stack.length - 1]) {
          stack.push(num);
      } else {
          const mx = stack.pop();
          while (stack.length && stack[stack.length - 1] > num) {
              stack.pop();
          }
          stack.push(mx);
      }
  }
  return stack.length;
};

//test
let arr = [2,1,3,4,4]
console.log(maxChunksToSorted(arr))
@syh-coder
syh-coder commented 9 minutes ago
var maxChunksToSorted = function (arr) {
const stack = [];
for (let i = 0; i < arr.length; i++) {
a = arr[i];
if (stack.length > 0 && stack[stack.length - 1] > a) {
const cur = stack[stack.length - 1];
while (stack && stack[stack.length - 1] > a) stack.pop();
stack.push(cur);
} else {
stack.push(a);
}
}
return stack.length;
};

@syh-coder
syh-coder commented 8 minutes ago via email 
你好，我是宋宇恒，我已收到你的邮件，我会尽快查阅，谢谢
@snmyj
snmyj commented 6 minutes ago
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
       vector<int> brr(arr);
       int cnt=0;
       sort(brr.begin(),brr.end());
       for(int i=0;i<arr.size();i++){
           if(arr[i]!=brr[i]) {
               for(int j=arr.size()-1;;j--){
                   if(brr[i]==arr[j]){
                           cnt++;
                           i=j;
                           break;
                   }
               }
           }
           else cnt++;
       }
        return cnt;
    }
};

