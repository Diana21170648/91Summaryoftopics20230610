【Day 20 】2023-06-29 - 347. 前 K 个高频元素 #21
Open
azl397985856 opened this issue 12 hours ago · 5 comments
Comments
@azl397985856
azl397985856 commented 12 hours ago
347. 前 K 个高频元素
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/top-k-frequent-elements/

前置知识
哈希表
堆排序
快速选择
题目描述
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

1 <= nums.length <= 10^5
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

@Diana21170648
Diana21170648 commented now
思路
哈希表+堆排序

代码
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}#哈希表存元素
        for num in nums:
            seen[num]=seen.get(num,0)+1
        #建堆
        heap=[]
        for num,freq in seen.items():
            #把数字和频率作为一个元组加到堆中
            
            heapq.heappush(heap,(freq,num))
            #如果堆中元素超过k，则移除频率最低的元素
            if len(heap)>k:
                heapq.heappop(heap)
        #将堆中剩余元素按频率从高到低加入到列表中，降序排序
        res=[]
        for i in range(k-1,-1,-1):
            res.append(heapq.heappop(heap)[1])

        return res[::-1]
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added 哈希表 排序 堆 20 labels 12 hours ago
@GuitarYs
GuitarYs commented 9 hours ago
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    frequent_nums = sorted(counts, key=lambda x: counts[x], reverse=True)
    return frequent_nums[:k]

# 示例1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
result1 = topKFrequent(nums1, k1)
print(result1)  # 输出: [1, 2]

# 示例2
nums2 = [1]
k2 = 1
result2 = topKFrequent(nums2, k2)
print(result2)  # 输出: [1]
@zhaoygcq
zhaoygcq commented 3 hours ago
思路
遍历数据，使用map记录数据的次数；之后基于map的记录数据，排序，返回结果

代码
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let map = new Map();
    for(let val of nums) {
        if(!map.has(val)) {
            map.set(val, 1)
        } else {
            let count = map.get(val);
            map.set(val, ++count);
        }
    }

    let entries = [...map.entries()];
    entries.sort((a, b) => b[1] - a[1]);
    return entries.slice(0, k).map(item => item[0]);
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@RocJeMaintiendrai
RocJeMaintiendrai commented 18 minutes ago
class Solution {
public int[] topKFrequent(int[] nums, int k) {
Map<Integer, Integer> map = new HashMap<>();
for(int num : nums) {
map.put(num, map.getOrDefault(num, 0) + 1);
}
Queue heap = new PriorityQueue<>((a, b) -> map.get(b) - map.get(a));
for(int key : map.keySet()) {
heap.add(key);
}
int[] res = new int[k];
for(int i = 0; i < k; i++) {
res[i] = heap.poll();
}
return res;
}
}

@bi9potato
bi9potato commented 15 minutes ago
Approach
HashMap + Min Heap

Code
class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num)+1);
            } else {
                map.put(num, 0);
            }
        }

        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
            (a, b) -> {
                return a.getValue().compareTo(b.getValue());
            }
        );

        for( Map.Entry<Integer, Integer> ele : map.entrySet()) {
            pq.offer(ele);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        int[] res = new int[k];
        for(int i = 0; i < k; i++) {
            res[i] = pq.poll().getKey();
        }

        return res;






        
    }
}
Complexity Analysis
Time 
Space 
