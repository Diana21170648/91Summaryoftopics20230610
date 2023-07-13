【Day 34 】2023-07-13 - 1904. 你完成的完整对局数 #36
Open
azl397985856 opened this issue 16 hours ago · 4 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
1904. 你完成的完整对局数
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/the-number-of-full-rounds-you-have-played/

前置知识
模拟
题目描述
一款新的在线电子游戏在近期发布，在该电子游戏中，以 刻钟 为周期规划若干时长为 15 分钟 的游戏对局。这意味着，在 HH:00、HH:15、HH:30 和 HH:45 ，将会开始一个新的对局，其中 HH 用一个从 00 到 23 的整数表示。游戏中使用 24 小时制的时钟 ，所以一天中最早的时间是 00:00 ，最晚的时间是 23:59 。

给你两个字符串 startTime 和 finishTime ，均符合 "HH:MM" 格式，分别表示你 进入 和 退出 游戏的确切时间，请计算在整个游戏会话期间，你完成的 完整对局的对局数 。

例如，如果 startTime = "05:20" 且 finishTime = "05:59" ，这意味着你仅仅完成从 05:30 到 05:45 这一个完整对局。而你没有完成从 05:15 到 05:30 的完整对局，因为你是在对局开始后进入的游戏；同时，你也没有完成从 05:45 到 06:00 的完整对局，因为你是在对局结束前退出的游戏。

如果 finishTime 早于 startTime ，这表示你玩了个通宵（也就是从 startTime 到午夜，再从午夜到 finishTime）。

假设你是从 startTime 进入游戏，并在 finishTime 退出游戏，请计算并返回你完成的 完整对局的对局数 。

 

示例 1：

输入：startTime = "12:01", finishTime = "12:44"
输出：1
解释：你完成了从 12:15 到 12:30 的一个完整对局。
你没有完成从 12:00 到 12:15 的完整对局，因为你是在对局开始后的 12:01 进入的游戏。
你没有完成从 12:30 到 12:45 的完整对局，因为你是在对局结束前的 12:44 退出的游戏。


示例 2：

输入：startTime = "20:00", finishTime = "06:00"
输出：40
解释：你完成了从 20:00 到 00:00 的 16 个完整的对局，以及从 00:00 到 06:00 的 24 个完整的对局。
16 + 24 = 40


示例 3：

输入：startTime = "00:00", finishTime = "23:59"
输出：95
解释：除最后一个小时你只完成了 3 个完整对局外，其余每个小时均完成了 4 场完整对局。


 

提示：

startTime 和 finishTime 的格式为 HH:MM
00 <= HH <= 23
00 <= MM <= 59
startTime 和 finishTime 不相等

@Diana21170648
Diana21170648 commented 1 minute ago
思路
开始时间以右边的结束时间为主，结束时间以左边的

代码
class Solution:
    def numberOfRounds(self, startTime:str, finishTime:str)->int:
        sh,sm=map(int,startTime.split(":"))
        eh,em=map(int,finishTime.split(":"))
        count_jinwei=0#看天数是否加1
        #转换成分钟,看时间是否进位
        if sh*60+sm>eh*60+em:
            count_jinwei+=1

        #处理开始时间：
        if 0<sm<=15:
            sm=15
        elif 15<sm<=30:
            sm=30
        elif 30<sm<=45:
            sm=45
        elif 45<sm<=60:
            sm=0
            sh+=1#小时进位

        #处理结束时间：
        if 0<=em<15:
            em=0
        elif 15<=em<30:
            em=15
        elif 30<=em<45:
            em=30
        elif 45<=em<60:
            em=45

        start_shijian=sh*60+sm
        end_shijian=eh*60+em
        if count_jinwei==1:
            end_shijian+=24*60
        return max(0,(end_shijian-start_shijian))//15#把时间加一起之后取整
#s=Solution()
#startTime="12:01"
#finishTime="12:46"
#print(s.numberOfRounds1904(startTime,finishTime))
复杂度分析

时间复杂度：O(1)
空间复杂度：O(1)


@azl397985856 azl397985856 added 模拟 34 labels 16 hours ago
@HuiyingC
HuiyingC commented 8 hours ago • edited 
Intuition

key points: is_overnight, floor, ceiling, edge case
Code

def numberOfRounds(self, loginTime, logoutTime):
    hs, ms = (int(x) for x in loginTime.split(":"))
    ts = 60 * hs + ms
    hf, mf = (int(x) for x in logoutTime.split(":"))
    tf = 60 * hf + mf
    if 0 <= tf - ts < 15: return 0 # edge case 

    # tf//15 -> convert logout time to the same / earlier 15 min count, we are effectively getting the floor.
    # (ts+14)//15 -> convert login time to the same / later 15 min count, we are effectively getting the ceiling.
    # (ts>tf)*96 -> if login time is later than logout time, add 4 quarters per hour * 24 hours = 96 counts, otherwise add 0.
    return tf//15 - (ts+14)//15 + (ts>tf)*96
Complexity Analysis

Time complexity: O(1)

Space complexity: O(1)

@zhaoygcq
zhaoygcq commented 5 hours ago
思路
分割开始/结束时间；通过分钟数确定偏移量offset；通过小时决定整体的数量count。
最后的结果为 count - offset

代码
/**
 * @param {string} loginTime
 * @param {string} logoutTime
 * @return {number}
 */
var numberOfRounds = function(loginTime, logoutTime) {
    let offset = 0;
    let count = 0;
    let startArr = loginTime.split(":").map(item => Number(item));
    let startTime = startArr[0];
    let offsetTime = startArr[1];
    offset += findStartOffset(offsetTime);
    let endArr = logoutTime.split(":").map(item => Number(item));
    let endTime = endArr[0];
    offsetTime = endArr[1];
    offset -= findEndOffset(offsetTime);
    if(endTime != startTime) {
        if(endTime < startTime) {
            endTime += 24;
        }
    } else {
        if(endArr[1] < startArr[1]) {
            endTime += 24;
        }
    }

    count += (endTime - startTime) * 4 - offset
    console.log(offset, "==", count)
    return count >= 0 ? count : 0;
};

function findStartOffset(offsetTime) {
    const offsetArr = [0, 15, 30, 45];
    for(let i = 0; i < offsetArr.length; i++) {
        if(offsetTime <= offsetArr[i]) {
            return i;
        }
    }
    return 4;
}

function findEndOffset(offsetTime) {
    const offsetArr = [0, 15, 30, 45];
    for(let i = offsetArr.length - 1; i >= 0; i--) {
        if(offsetTime >= offsetArr[i]) {
            return i;
        }
    }
}
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@GuitarYs
GuitarYs commented 4 hours ago
class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        start_hour, start_minute = map(int, loginTime.split(":"))
        end_hour, end_minute = map(int, logoutTime.split(":"))

        if end_hour < start_hour or (end_hour == start_hour and end_minute < start_minute):
            end_hour += 24

        start_rounded_minute = ((start_minute + 14) // 15) * 15
        end_rounded_minute = (end_minute // 15) * 15

        start_time = start_hour * 60 + start_rounded_minute
        end_time = end_hour * 60 + end_rounded_minute

        return max(0, (end_time - start_time) // 15)
