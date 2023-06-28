【Day 19 】2023-06-28 - 两数之和 #20
Open
azl397985856 opened this issue 20 hours ago · 16 comments
Comments
@azl397985856
azl397985856 commented 20 hours ago
两数之和
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/two-sum

前置知识
哈希表
题目描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

@Diana21170648
Diana21170648 commented now
思路
用哈希表做两数之和（也可以暴力法）

代码
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            if nums[i] in map:
                return [map[nums[i]],i]
            map[target-nums[i]]=i
        return []
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)

@azl397985856 azl397985856 added 双指针 哈希表 19 labels 20 hours ago
@joemonkeylee
joemonkeylee commented 18 hours ago • 
function twoSum(nums: number[], target: number): number[] {
    let res: number[] = [];
    let dict: Map<number, number> = new Map<number, number>();
    let temp: number = 0;
    for (let i = 0; i < nums.length; i++) {
        temp = target - nums[i];
        if (dict.has(temp)) {
            let index = dict.get(temp);
            return [i, index]
        } else {
            dict.set(nums[i], i);
        }
    }
    return res;
};
@hengistchan
hengistchan commented 18 hours ago
func twoSum(nums []int, target int) []int {
	m := map[int]int{}
	for i, v := range nums {
		if _, ok := m[v]; ok {
			return []int{m[v], i}
		}
		m[target-v] = i
	}
	return nil
}
@bi9potato
bi9potato commented 18 hours ago
Approach
HashMap

Code
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                return new int[] {i, map.get(nums[i])};
            }

            map.put(target - nums[i], i);
        }

        return null;

    }
}
Complexity Analysis
Time 
Space 
@freesan44
freesan44 commented 12 hours ago
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
//        for (index,value) in nums.enumerated(){
//            let tempTarget = target
//            var temp = tempTarget - value
//            //遍历index之后的数组
//            for (index2,value2) in nums.enumerated().filter({ (index2,_) in index2>index}){
//                if (temp - value2) == 0{
//                    return[index,index2]
//                }
//            }
//
//        }
        var dic : [Int:Int] = [Int:Int]()
        for (index, value) in nums.enumerated(){
            let tempTarget = target
            var temp = tempTarget - value
            if dic[temp] != nil {
                return [dic[temp]!,index]
            }
            dic[value] = index
//            print(dic)
        }
        
        return []
    }
}
@zhaoygcq
zhaoygcq commented 11 hours ago
思路
遍历数组，同时使用map记录已经遍历的数据；

代码
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = new Map();

    for(let index = 0; index < nums.length; index++) {
        let val = nums[index];

        if(map.has(val)) {
            return [map.get(val), index];
        }
        map.set(target - val, index);        
    }

    return [];
};
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@jackgaoyuan
jackgaoyuan commented 10 hours ago
func twoSum(nums []int, target int) []int {
    // m = { value: index }
    m := make(map[int]int)
    for i, v := range nums {
        if index, ok := m[target - v]; !ok {
            m[v] = i
        } else {
            return []int{index, i}
        }
    }
    return []int{}
}
@mo660
mo660 commented 10 hours ago
思路
哈希做法

代码
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int>mp;
        for(int i = 0; i < nums.size(); i++){
            if (mp.count(target - nums[i])){
                return {mp[target - nums[i]], i};
            }
            mp[nums[i]] = i;
        }
        return {};
    }
};
@wzbwzt
wzbwzt commented 6 hours ago
/*
思路：
双指针

复杂度：
空间复杂度: O(1)
时间复杂度： O(n^2), n为数组长度
*/

func twoSum(nums []int, target int) (out []int) {
	for i, v := range nums {
		for j := i + 1; j < len(nums); j++ {
			if v+nums[j] == target {
				out = append(out, i, j)
				return
			}
		}
	}
	return
}
/*
思路：
哈希表
空间换时间

复杂度：
空间复杂度: O(n)
时间复杂度： O(n), n为数组长度
*/

func twoSum2(nums []int, target int) (out []int) {
	targer_map := make(map[int]int)
	for i, v := range nums {
		index, ok := targer_map[v]
		if ok {
			out = append(out, i, index)
			return
		}
		targer_map[target-v] = i
	}
	return
}
@61hhh
61hhh commented 5 hours ago
思路
哈希表存储数值与index映射

代码
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int minusNum = target - nums[i];
            if (map.containsKey(minusNum)) {
                return new int[]{map.get(minusNum), i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
复杂度
时间复杂度：O(n)
空间复杂度：O(n)
@catkathy
catkathy commented 4 hours ago
Code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j]==target:
                    return i, j
@RanDong22
RanDong22 commented 3 hours ago
function twoSum(nums: number[], target: number): number[] {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (map.has(target - nums[i])) {
      return [i, map.get(target - nums[i])];
    }
    map.set(nums[i], i);
  }
  return [];
}
@GuitarYs
GuitarYs commented 3 hours ago
def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

# 示例测试
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # 输出 [0, 1]

nums = [3, 2, 4]
target = 6
result = twoSum(nums, target)
print(result)  # 输出 [1, 2]

nums = [3, 3]
target = 6
result = twoSum(nums, target)
print(result)  # 输出 [0, 1]
@snmyj
snmyj commented 3 hours ago
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hashs;
        vector<int> ret;
        for(int i=0;i<nums.size();i++) {
            
            if(hashs.count(target-nums[i])) {
                ret.push_back(i);
                int j=hashs[target-nums[i]];
                
                ret.push_back(j);
                
            }
            hashs[nums[i]]=i;
         }
        return ret;
    }
};
@Alexno1no2
Alexno1no2 commented 2 hours ago
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for index,value in enumerate(nums):
            if target - value in res:
                return [index,res[target - value]]
            else:
                res[value] = index
        return


@Master-guang
Master-guang commented 2 hours ago
// 思路：哈希表秒解，今天的题目有点简单了
var twoSum = function(nums, target) {
    let map = new Map();
    for(let i = 0; i < nums.length; i++) {
        let index = target - nums[i];
        if(map.has(nums[i])) {
            return [map.get(nums[i]), i]
        } else {
            map.set(index, i)
        }
    }
};
