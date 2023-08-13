【Day 65 】2023-08-13 - 455. 分发饼干 #67
Open
azl397985856 opened this issue 20 hours ago · 2 comments
Comments
@azl397985856
azl397985856 commented 20 hours ago
455. 分发饼干
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/assign-cookies/

前置知识
暂无

题目描述
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

注意：

你可以假设胃口值为正。
一个小朋友最多只能拥有一块饼干。

示例 1:

输入: [1,2,3], [1,1]

输出: 1

解释:

你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

示例 2:

输入: [1,2], [1,2,3]

输出: 2

解释:

你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.
@Diana21170648
Diana21170648 commented 1 minute ago
思路
贪心，选大饼干先满足胃口大的

代码
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        si,gi=0,0
        count=0
        #当孩子没有满足且饼干还有剩余
        while si<len(s) and gi<len(g):
            #如果饼干值大于孩子的胃口值，证明可以满足孩子的胃口
            if s[si]>=g[gi]:
                count+=1
                si+=1#饼干分完
            gi+=1#开始满足下一个孩子
        return count
复杂度分析

时间复杂度：O(NlogN)，其中 N 为数组长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 贪心 65 labels 20 hours ago
@Fuku-L
Fuku-L commented 18 hours ago
代码
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // 1. 对两个数组进行排序
        Arrays.sort(g);
        Arrays.sort(s);
        // 2. 记录满足的孩子数量
        int child = 0;
        int cookie = 0;
        // 3. 遍历饼干数组
        while (cookie < s.length && child < g.length ) {
            if (s[cookie] >= g[child]) {
                child++;
            }
            cookie++;
        }
        return child;
    }
}
