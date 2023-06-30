【Day 21 】2023-06-30 - 447. 回旋镖的数量 #22
Open
azl397985856 opened this issue 12 hours ago · 7 comments
Comments
@azl397985856
azl397985856 commented 12 hours ago
447. 回旋镖的数量
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/number-of-boomerangs/

前置知识
哈希表
两点间距离计算方法
排列组合基础知识
题目描述
给定平面上  n 对不同的点，“回旋镖” 是由点表示的元组  (i, j, k) ，其中  i  和  j  之间的距离和  i  和  k  之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设  n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:


输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

@Diana21170648
Diana21170648 commented 1 minute ago
思路
回旋镖，一个点到其余两个点的距离相同，另两个点之间的距离不相同（等腰三角形）

代码
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n=len(points)
        ans=0
        for i in range(n):
            seen=collections.defaultdict(int)
            for j in range(n):#顺序也需要考虑进去
                dist=abs(points[i][0]-points[j][0])**2+abs(points[i][1]-points[j][1])**2#每对点之间距离的平方
                seen[dist]+=1#把距离求出来放进哈希表
            for count in seen.values():
                ans+=count*(count-1)
        return ans
复杂度分析

时间复杂度：O(N^2)，其中 N 为元组数。
空间复杂度：O(N)

@azl397985856 azl397985856 added 哈希表 Math 21 labels 12 hours ago
@joemonkeylee
joemonkeylee commented 9 hours ago
function numberOfBoomerangs(points: number[][]): number {
    let res = 0;
    for (let i = 0; i < points.length; i++) {
        const map = new Map();
        for (let j = 0; j < points.length; j++) {
            if (i === j) continue;
            const hypotenuse =
                Math.pow(points[i][0] - points[j][0], 2) +
                Math.pow(points[i][1] - points[j][1], 2);
            map.set(hypotenuse, (map.get(hypotenuse) ?? 0) + 1);
        }
        for (let count of map.values()) {
            res += count * (count - 1)
        }
    }
    return res;
};
@bi9potato
bi9potato commented 6 hours ago
class Solution {
    public int numberOfBoomerangs(int[][] points) {

        if (points.length < 3) return 0;

        int res = 0;

        for (int i = 0; i < points.length; i++) {
            // System.out.println(points[i]);
            
            HashMap<Integer, Integer> map = new HashMap<>();

            for (int j = 0; j < points.length; j++) {

                if (i == j) continue;

                int dis = distance(points[i], points[j]);
                if (map.containsKey(dis)) {
                    map.put(dis, map.get(dis)+1);
                } else {
                    map.put(dis, 1);
                }
                

            }

            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (entry.getValue() >= 2) {
                    res += entry.getValue() * (entry.getValue()-1);
                }
            }



        }

        return res;

    }

    private int distance(int[] a, int[] b) {
        return (a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1]);
    }
}
@freesan44
freesan44 commented 3 hours ago
class Solution {
    func numberOfBoomerangs(_ points: [[Int]]) -> Int {
        if points.isEmpty || points.count <= 2 {
        return 0
    }

    var res = 0
    var equalCount = [Int: Int]()

    for i in 0..<points.count {
        for j in 0..<points.count {
            let distance = getDistance(points[i], points[j])
            equalCount[distance, default: 0] += 1
        }

        for count in equalCount.values {
            res += count * (count - 1)
        }
        equalCount.removeAll()
    }

    return res
    }
    private func getDistance(_ x: [Int], _ y: [Int]) -> Int {
    let x1 = y[0] - x[0]
    let y1 = y[1] - x[1]

    return x1 * x1 + y1 * y1
}
}
@zhaoygcq
zhaoygcq commented 3 hours ago
思路
欧式距离： Math.sqrt((x1-x2) ** (x1-x2) + (y1-y2) ** (y1-y2))
遍历数据，使用map记录每一个节点到齐相邻节点的欧式距离的数量，可直接求平方和，避免开方。
之后记录map中存储的数量；
注意：
假设 [B1, B2, ... Bn] 为 n 个和 A 距离相同的点。 那么 [B1, B2, ... Bn] 中任意两个点其实都和A构成了回旋镖三元组， 所以就转化成从**n个点中任选两个（需要考虑顺序）**的问题。 答案当然是： n * (n - 1) 。

代码
/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfBoomerangs = function(points) {
    let ans = 0;
    for (const p of points) {
        const cnt = new Map();
        for (const q of points) {
            const dis = (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1]);
            cnt.set(dis, (cnt.get(dis) || 0) + 1);
        }
        for (const [_, m] of cnt.entries()) {
            ans += m * (m - 1);
        }
    }
    return ans;
};
复杂度分析

时间复杂度：O(N2)，其中 N 为数组长度。
空间复杂度：O(N)
@mo660
mo660 commented 2 hours ago
思路
A(n, 2)

代码
class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int res = 0;
        for(auto it : points){
            unordered_map<int, int> mp;
            for(auto it1 : points){
                int num = (it1[0] - it[0])*(it1[0] - it[0]) + (it1[1] - it[1])*(it1[1] - it[1]);
                mp[num]++;
            }
            for(auto &p : mp){
                res += p.second*(p.second-1);
            }
        }
        return res;
    }
};
@61hhh
61hhh commented 33 minutes ago
代码
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();// 距离:相同距离的点数量
        for (int i = 0; i < points.length; i++) {
            // 遍历其他点 统计其他点到点i的距离
            for (int j = 0; j < points.length; j++) {
                if (i == j) {
                    continue;
                }
                int distance = calDistance(points[i], points[j]);
                map.put(distance, map.getOrDefault(distance, 0) + 1);
            }
            // 相同距离点集中取两个与当前点i构成回旋镖
            // 考虑顺序用排列 A(n,2) = n*(n-1);
            for (int val : map.values()) {
                res += val * (val - 1);
            }
            map.clear();// 清空map
        }
        return res;
    }

    private int calDistance(int[] p1, int[] p2) {
        int x = p2[0] - p1[0];
        int y = p2[1] - p1[1];
        return x * x + y * y;
    }
}
复杂度
时间复杂度：O(n^2)
空间复杂度：O(n)
