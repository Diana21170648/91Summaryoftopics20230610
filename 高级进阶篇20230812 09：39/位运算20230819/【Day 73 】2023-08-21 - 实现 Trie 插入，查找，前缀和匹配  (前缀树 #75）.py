【Day 73 】2023-08-21 - 实现 Trie (前缀树 #75
Open
azl397985856 opened this issue 16 hours ago · 3 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
实现 Trie (前缀树
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/implement-trie-prefix-tree

前置知识
树
Trie
题目描述
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple"); // 返回 true
trie.search("app"); // 返回 false
trie.startsWith("app"); // 返回 true1
trie.insert("app");
trie.search("app"); // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

@Diana21170648
Diana21170648 commented 1 minute ago
思路
前缀树

代码
class TireNode:
    def __init__(self):
        self.count=0
        self.perCount=0
        self.children={}#字典


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TireNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TireNode()
            node=node.children[char]
            node.perCount+=1
        node.count+=1



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.count>0
            


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.perCount>0
复杂度分析

时间复杂度：O(1)创建Tire，插入查找和匹配为O(N)
空间复杂度：O(char总字数*字符集的大小)

@azl397985856 azl397985856 added 前缀树 73 labels 16 hours ago
@freesan44
freesan44 commented 8 hours ago
class TrieNode {
    var count: Int
    var preCount: Int
    var children: [Character: TrieNode]

    init() {
        count = 0
        preCount = 0
        children = [:]
    }
}

class Trie {
    var root: TrieNode

    init() {
        root = TrieNode()
    }

    func insert(_ word: String) {
        var node = root
        for ch in word {
            if node.children[ch] == nil {
                node.children[ch] = TrieNode()
            }
            node = node.children[ch]!
            node.preCount += 1
        }
        node.count += 1
    }

    func search(_ word: String) -> Bool {
        var node = root
        for ch in word {
            if node.children[ch] == nil {
                return false
            }
            node = node.children[ch]!
        }
        return node.count > 0
    }

    func startsWith(_ prefix: String) -> Bool {
        var node = root
        for ch in prefix {
            if node.children[ch] == nil {
                return false
            }
            node = node.children[ch]!
        }
        return node.preCount > 0
    }
}
@GuitarYs
GuitarYs commented 1 hour ago
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        current = self.root
        for ch in word:
            index = self._char_to_index(ch)
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for ch in word:
            index = self._char_to_index(ch)
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.is_end_of_word

    def startsWith(self, prefix):
        current = self.root
        for ch in prefix:
            index = self._char_to_index(ch)
            if not current.children[index]:
                return False
            current = current.children[index]
        return True


# 示例用法
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # 返回 True
print(trie.search("app"))  # 返回 False
print(trie.startsWith("app"))  # 返回 True
trie.insert("app")
print(trie.search("app"))  # 返回 True
