【Day 32 】2023-07-11 - 657. 机器人能否返回原点 #33
Open
azl397985856 opened this issue 10 hours ago · 7 comments
Comments
@azl397985856
azl397985856 commented 10 hours ago
657. 机器人能否返回原点
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/robot-return-to-origin/

前置知识
模拟
题目描述
在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。

移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。

注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。

 

示例 1:

输入: "UD"
输出: true
解释：机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。

示例 2:

输入: "LL"
输出: false
解释：机器人向左移动两次。它最终位于原点的左侧，距原点有两次 “移动” 的距离。我们返回 false，因为它在移动结束时没有返回原点。

@Diana21170648
Diana21170648 commented 3 minutes ago
思路
简单图题目，模拟是直接把题目翻译为代码即可
以原点为坐标，左加右减，上加下减

代码
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        for move in moves:
            if move=='R':
                x+=1
            if move=='L':
                x-=1
            if move=='U':
                y+=1
            if move=='D':
                y-=1
        return x==0 and y==0
    
复杂度分析

时间复杂度：O(N)，其中 N 为字符串长度。
空间复杂度：O(1)


@azl397985856 azl397985856 added 模拟 32 labels 10 hours ago
@bi9potato
bi9potato commented 9 hours ago
class Solution {
    public boolean judgeCircle(String moves) {

        int x = 0, y = 0;

        for (int i = 0; i < moves.length(); i++) {
            char c = moves.charAt(i);

            if (c == 'U') {
                y -=1;
            } else if (c == 'D') {
                y +=1;
            } else if (c == 'L') {
                x -=1;
            } else {
                x +=1;
            }
        }

        if (x == 0 && y == 0) {
            return true;
        }

        return false;
        
    }
}
@joemonkeylee
joemonkeylee commented 7 hours ago
var judgeCircle = function (moves) {
  let x = 0
  let y = 0
  for (let i = 0; i < moves.length; i++) {
    switch (moves[i]) {
      case 'L': {
        x--
        break
      }
      case 'R': {
        x++
        break
      }
      case 'U': {
        y--
        break
      }
      case 'D': {
        y++
        break
      }
    }
  }
  return x === 0 && y === 0
};
@hengistchan
hengistchan commented 7 hours ago
class Solution {
    public boolean judgeCircle(String moves) {

        int x = 0, y = 0;

        for (int i = 0; i < moves.length(); i++) {
            char c = moves.charAt(i);

            if (c == 'U') {
                y -=1;
            } else if (c == 'D') {
                y +=1;
            } else if (c == 'L') {
                x -=1;
            } else {
                x +=1;
            }
        }

        if (x == 0 && y == 0) {
            return true;
        }

        return false;
        
    }
}
@HuiyingC
HuiyingC commented 3 hours ago • edited 
思路
题目要求回到原点，那么只要上、下相等，左、右相等即可

代码
class Solution(object):
    def judgeCircle(self, moves):
        if not moves: return True

        cnt_map = collections.Counter(moves)

        # opt 1 遍历4次
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')
        
        # opt 2 遍历一次
        ans = False
        if 'U' in cnt_map:
            ans = 'D' in cnt_map and cnt_map['U'] == cnt_map['D']
        if ans and 'L' in cnt_map:
            ans = 'R' in cnt_map and cnt_map['L'] == cnt_map['R']

        return ans
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(1)，储存counter
@freesan44
freesan44 commented 2 hours ago
class Solution {
    func judgeCircle(_ moves: String) -> Bool {
    var x = 0
    var y = 0
    for move in moves {
        if move == "R" { x += 1 }
        if move == "L" { x -= 1 }
        if move == "U" { y += 1 }
        if move == "D" { y -= 1 }
    }

    return x == 0 && y == 0
}
}
@mo660
mo660 commented 30 minutes ago
代码
class Solution {
public:
    bool judgeCircle(string moves) {
        int sLen = moves.length();
        pair<int, int> coordinate(0, 0);
        for (int i = 0; i < sLen; i++)
        {
            switch (moves[i])
            {
            case 'L':
                coordinate.second -= 1;
                break;
            case 'R':
                coordinate.second += 1;
                break;
            case 'U':
                coordinate.first += 1;
                break;
            case 'D':
                coordinate.first -= 1;
                break;
            default:
                break;
            }
        }
        if (0 == coordinate.first && 0 == coordinate.second)
            return true;
        else
            return false;
    }
};
