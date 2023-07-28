【Day 49 】2023-07-28 - 52. N 皇后 II #51
Open
azl397985856 opened this issue yesterday · 7 comments
Comments
@azl397985856
azl397985856 commented yesterday
52. N 皇后 II
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/n-queens-ii/

前置知识
回溯
深度优先遍历
题目描述
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。


示例 1：


输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：1
 

提示：

1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

@Diana21170648
Diana21170648 commented now
思路
dfs+回溯

代码
class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(pre,i):
            nonlocal queen
            if i==n:
                queen+=1
                return
            for j in range(n):
                if j in col:
                    if i-j in right and i+j in left:
                        col.discard(j)
                        right.discard(i-j)
                        left.discard(i+j)
                        dfs(pre+[j],i+1)
                        col.add(j)
                        right.add(i-j)
                        left.add(i+j)
            return
        col=set(list(range(n)))
        right=set(list(range(1-n,n,1)))
        left=set(list(range(2*n)))
        queen=0
        dfs([],0)
        return queen


复杂度分析

时间复杂度：O(N！)，其中 N 为数组长度。
空间复杂度：O(N)


@azl397985856 azl397985856 added 回溯 49 labels yesterday
@Beanza
Beanza commented yesterday
const totalNQueens = function (n) {
let res = 0;
const dfs = (n, row, col, pie, na) => {
if (row >= n) {
res++;
return;
}
// 将所有能放置 Q 的位置由 0 变成 1，以便进行后续的位遍历
// 也就是得到当前所有的空位
let bits = ~(col | pie | na) & ((1 << n) - 1);
while (bits) {
// 取最低位的1
let p = bits & -bits;
// 把P位置上放入皇后
bits = bits & (bits - 1);
// row + 1 搜索下一行可能的位置
// col ｜ p 目前所有放置皇后的列
// (pie | p) << 1 和 (na | p) >> 1) 与已放置过皇后的位置 位于一条斜线上的位置
dfs(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1);
}
};
dfs(n, 0, 0, 0, 0);
return res;
};

@mo660
mo660 commented 12 hours ago
class Solution {
public:
    int totalNQueens(int n) {
        dfs(n, 0, 0, 0, 0);
        
        return this->res;
    }
    
    void dfs(int n, int row, int col, int ld, int rd) {
        if (row >= n) { res++; return; }
        
        // 将所有能放置 Q 的位置由 0 变成 1，以便进行后续的位遍历
        int bits = ~(col | ld | rd) & ((1 << n) - 1);
        while (bits > 0) {
            int pick = bits & -bits; // 注: x & -x
            dfs(n, row + 1, col | pick, (ld | pick) << 1, (rd | pick) >> 1);
            bits &= bits - 1; // 注: x & (x - 1)
        }
    }

private:
    int res = 0;
};
@GuitarYs
GuitarYs commented 10 hours ago
class NQueens:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.columns = []

    def solveNQueens(self):
        self.backtrack(0)
        return self.count

    def backtrack(self, row):
        if row == self.n:
            self.count += 1
            return

        for col in range(self.n):
            if self.is_valid(row, col):
                self.columns.append(col)
                self.backtrack(row + 1)
                self.columns.pop()

    def is_valid(self, row, col):
        for r, c in enumerate(self.columns):
            if c == col or r - c == row - col or r + c == row + col:
                return False
        return True
@wzbwzt
wzbwzt commented 5 hours ago
/*
思路：
深度优先搜索

复杂度：
时间复杂度为 O(n!)
空间复杂度为 O(n)
*/

func totalNQueens(n int) int {
	res := 0
	var dfs func(n, row, col, pie, na int)

	dfs = func(n, row, col, pie, na int) {
		if row >= n {
			res++
			return
		}
		bits := ^(col | pie | na) & ((1 << n) - 1)
		for bits > 0 {
			p := bits & -bits
			bits = bits & (bits - 1)
			dfs(n, row+1, col|p, (pie|p)<<1, (na|p)>>1)
		}
	}

	dfs(n, 0, 0, 0, 0)
	return res
}
@Moin-Jer
Moin-Jer commented 2 hours ago
class Solution {
    public int totalNQueens(int n) {
        Set<Integer> columns = new HashSet<Integer>();
        Set<Integer> diagonals1 = new HashSet<Integer>();
        Set<Integer> diagonals2 = new HashSet<Integer>();
        return backtrack(n, 0, columns, diagonals1, diagonals2);
    }

    public int backtrack(int n, int row, Set<Integer> columns, Set<Integer> diagonals1, Set<Integer> diagonals2) {
        if (row == n) {
            return 1;
        } else {
            int count = 0;
            for (int i = 0; i < n; i++) {
                if (columns.contains(i)) {
                    continue;
                }
                int diagonal1 = row - i;
                if (diagonals1.contains(diagonal1)) {
                    continue;
                }
                int diagonal2 = row + i;
                if (diagonals2.contains(diagonal2)) {
                    continue;
                }
                columns.add(i);
                diagonals1.add(diagonal1);
                diagonals2.add(diagonal2);
                count += backtrack(n, row + 1, columns, diagonals1, diagonals2);
                columns.remove(i);
                diagonals1.remove(diagonal1);
                diagonals2.remove(diagonal2);
            }
            return count;
        }
    }
}
@Alexno1no2
Alexno1no2 commented 34 minutes ago
class Solution:
    def __init__(self):
        self.res = []

    def totalNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        self.backtrack(board, 0)
        return len(self.res)

    def backtrack(self, board: List[List[str]], row: int) -> None:
        if row == len(board):
            self.res.append(1)
            return
      
        n = len(board[row])
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
            
            board[row][col] = "Q"
            self.backtrack(board, row + 1)
            board[row][col] = "."

    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        n = len(board)
        # 检查列是否有皇后冲突
        for i in range(n):
            if board[i][col] == "Q":
                return False
        
        # 检查右上方是否有皇后冲突
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
    
        # 检查左上方是否有皇后冲突
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        return True
