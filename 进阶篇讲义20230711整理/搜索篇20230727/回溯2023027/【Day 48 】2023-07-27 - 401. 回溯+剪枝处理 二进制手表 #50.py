【Day 48 】2023-07-27 - 401. 二进制手表 #50
Open
azl397985856 opened this issue yesterday · 8 comments
Comments
@azl397985856
azl397985856 commented yesterday
401. 二进制手表
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/binary-watch/

前置知识
暂无

题目描述
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。


例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。



示例：

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]


提示：

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
超过表示范围（小时 0-11，分钟 0-59）的数据将会被舍弃，也就是说不会出现 "13:00", "0:61" 等时间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-watch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


@Diana21170648
Diana21170648 commented 1 minute ago
思路
用回溯处理二进制手表，笛卡尔积找两个集合的所有可能，剪枝处理所有不满足的情况

代码
from itertools import combinations
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def possible_number(count,minute=False):
            if count==0:
                return [0]
            if minute:
                return filter(lambda a:a<60,map(sum,combinations([1,2,4,8,16,32],count)))
            return filter(lambda a:a<12,map(sum,combinations([1,2,4,8],count)))
        
        ans=set()#用笛卡尔积表示两个集合的所有可能得组合，但是得处理不满足题目要求的情况
        for i in range(min(4,turnedOn+1)):#到num+1处理所有可能的情况
            for a in possible_number(i):
                for b in possible_number(turnedOn-i,True):
                    ans.add(str(a)+":"+str(b).rjust(2,'0'))
        return list(ans)

复杂度分析

时间复杂度：O(2^N)。
空间复杂度：O(2^N)

@azl397985856 azl397985856 added 回溯 48 labels yesterday
@GuitarYs
GuitarYs commented 18 hours ago
class Solution:
    def readBinaryWatch(self, num: int) -> [str]:
        result = []

        def countBits(n):
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                n >>= 1
            return count
        def getTimeString(hours, minutes):
            return str(hours) + ':' + '{:02d}'.format(minutes)
        for hours in range(12):
            for minutes in range(60):
                if countBits(hours) + countBits(minutes) == num:
                    result.append(getTimeString(hours, minutes))

        return result
@freesan44
freesan44 commented 13 hours ago
class Solution {
    func readBinaryWatch(_ num: Int) -> [String] {
        return (0..<12).flatMap { a in
            (0..<60).compactMap { b in
                let binary = String(a, radix: 2) + String(b, radix: 2)
                let count = binary.filter { $0 == "1" }.count
                if count == num {
                    return "\(a):\(String(b).padding(toLength: 2, withPad: "0", startingAt: 0))"
                } else {
                    return nil
                }
            }
        }
    }
}
@acy925
acy925 commented 9 hours ago
代码
class Solution:
    def readBinaryWatch(self, sum: int) -> List[str]:
        res = []
        for i in range(1<<10):
            # 看我们穷举到i变成二进制有多少个1，2^10 次方种情况
            cur_one = 0

            # j用来数当前i有多少个1
            for j in range(10):
                if (i >> j) & 1 == 1: # i 的第 j 位是1
                    cur_one += 1

            # 假如说当前i 的二进制位上的1，和num亮了多少盏灯一样的话
            # 我们就要判断这个当前i能不能构成合法时间了
            if cur_one == sum:
                # 只有上面四盏灯才是小时，i 右移 6 位，比较高的 4 位
                hour = i >> 6
                # 下面六盏灯是分钟
                # 63 = 111111
                minute = i & 63

                # 看时间合不合法
                if hour < 12 and minute < 60:
                    res.append("%d:%02d"%(hour,minute))

        return res

@dorian-byte
dorian-byte commented 9 hours ago
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
    from itertools import combinations
    leds = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
    times = []

    for comb in combinations(range(10), turned_on):
        hour = sum(leds[i] for i in comb if i < 4)
        minute = sum(leds[i] for i in comb if i >= 4)
        if hour < 12 and minute < 60:
            times.append(f"{hour}:{minute:02d}")

    return times
@wzbwzt
wzbwzt commented 3 hours ago
/*
思路:

复杂度：
时间复杂度：O(turnedOn^2)
空间复杂度：O(1)
*/

func readBinaryWatch(turnedOn int) (ans []string) {
	h_num := min(4, turnedOn+1)
	for i := 0; i <= h_num; i++ {
		for _, h := range possible_number(i, false) {
			m := turnedOn - i
			if m < 0 {
				continue
			}
			for _, m := range possible_number(m, true) {
				ans = append(ans, fmt.Sprintf("%d:%02d", h, m))
			}
		}
	}
	return
}

func possible_number(count int, m bool) (ans []int) {
	if count == 0 {
		return []int{0}
	}
	if !m {
		for i := 0; i < 12; i++ {
			if bits.OnesCount(uint(i)) == count {
				ans = append(ans, i)
			}
		}
	} else {
		for i := 0; i < 60; i++ {
			if bits.OnesCount(uint(i)) == count {
				ans = append(ans, i)
			}
		}
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
@passengersa
passengersa commented 52 minutes ago
代码：
var readBinaryWatch = function(turnedOn) {
var result = [];
for (var hour = 0; hour < 12; hour++) {
for (var minute = 0; minute < 60; minute++) {
if (countBits(hour) + countBits(minute) === turnedOn) {
result.push(hour + ":" + (minute < 10 ? "0" + minute : minute));
}
}
}
return result;
};

function countBits(num) {
var count = 0;
while (num > 0) {
count += num & 1;
num >>= 1;
}
return count;
}

@Alexno1no2
Alexno1no2 commented 9 minutes ago
'''
总体思路
在10个灯中选num个灯点亮，如果选择的灯所组成的时间已不合理（小时超过11，分钟超过59）就进行剪枝
也就是从0到10先选一个灯亮，再选当前灯的后面的灯亮，再选后面的灯的后面的灯亮，一直到num个灯点满

具体思路
为了方便计算，分别设置了小时数组和分钟数组
递归的四个参数分别代表：剩余需要点亮的灯数量，从索引index开始往后点亮灯，当前小时数，当前分钟数
每次进入递归后，先判断当前小时数和分钟数是否符合要求，不符合直接return
for循环枚举点亮灯的情况，从index枚举到10，每次枚举，
减少一个需要点亮的灯数量num - 1
从当前已点亮的灯后面选取下一个要点亮的灯 i + 1
在hour中增加当前点亮灯的小时数，如果i大于3，当前灯是分钟灯而不是小时灯，则加上0个小时
在minute中增加当前点亮灯的分钟数，如果i没有大于3，当前灯是小时灯而不是分钟灯，则加上0分钟
当剩余需要点亮的灯数量为0的时候，已枚举完一种情况，根据题目要求的格式加到res列表中
返回res

'''
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1, 2, 4, 8, 0, 0, 0, 0, 0, 0]
        minutes = [0, 0, 0, 0, 1, 2, 4, 8, 16, 32]
        res = []
        def backtrack(num, index, hour, minute):
            if hour > 11 or minute > 59:
                return
            if num == 0:
                res.append('%d:%02d' % (hour, minute))
                return
            for i in range(index, 10):
                backtrack(num - 1, i + 1, hour + hours[i], minute + minutes[i])
        
        backtrack(num, 0, 0, 0)
        return res


