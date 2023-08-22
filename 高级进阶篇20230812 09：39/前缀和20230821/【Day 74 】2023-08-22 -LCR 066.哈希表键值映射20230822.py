【Day 74 】2023-08-22 - 677. 键值映射 #76
Open
azl397985856 opened this issue 18 hours ago · 1 comment
Comments
@azl397985856
azl397985856 commented 18 hours ago
677. 键值映射
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/map-sum-pairs

前置知识
哈希表
Trie
DFS
题目描述
实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:

输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5

@azl397985856 azl397985856 added 前缀树 74 labels 18 hours ago
@Diana21170648
Diana21170648 commented now
思路
哈希表

代码
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap={}

    def sum(self,prefix: str ) -> int :
        count=0
        for key in self.hashmap:
            if key.startswith(prefix):
                count+=self.hashmap[key]
        return count

    def insert(self,key: str, val: int ) ->None:
        self.hashmap[key]=val#没有就插入，有就覆盖
复杂度分析

时间复杂度：insert是O(1)，sum是O(N*S,)其中 N 为key的个数，s是前缀长度。
空间复杂度：O(N),N为不重复的key的个数
