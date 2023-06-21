【Day 12 】2023-06-21 - 146. LRU 缓存机制 #13
Open
azl397985856 opened this issue 11 hours ago · 7 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
146. LRU 缓存机制
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/lru-cache/

前置知识
暂无

题目描述
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。


进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？



示例：

输入

["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
@azl397985856 azl397985856 added 哈希表 链表 12 labels 11 hours ago
@bi9potato
bi9potato commented 8 hours ago
Approach
LinkedList + HashMap
Use LinkedList to store order of keys, and HashMap to store key-value pairs.

@Diana21170648
Diana21170648 commented now
思路
python有内置的的双向链表，OrderedDict
get读操作操作的是头部，put写操作操作的是尾部
链表增删容易，但是查找麻烦，所以用哈希表存起来，使得增删查都只需要O（1）

代码
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.maxsize=capacity
        self.LRUCache=OrderedDict()


    def get(self, key: int) -> int:#读操作
        if key in self.LRUCache:#在缓存中，移动到字典尾部，证明为最常使用的元素
            self.LRUCache.move_to_end(key)
        return self.LRUCache.get(key,-1)#-1代表最尾部的元素,找不到，返回-1


    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:#写操作如果存在则删掉再重新赋值
            del self.LRUCache[key]
        self.LRUCache[key]=value#重新赋值的元素放在末尾
        if len(self.LRUCache)>self.maxsize:#超出缓存容量，则删除字典的头部元素
            self.LRUCache.popitem(last=False)
复杂度分析

时间复杂度：O(1)，增删查平均为O(1)
空间复杂度：O(N),链表和哈希表的大小均为N

Code
class LRUCache {

    private HashMap<Integer, Node> map;
    private int maxLen;
    private DoubleLinkedList dll;


    public LRUCache(int capacity) {
        
        map = new HashMap<>();
        dll = new DoubleLinkedList();
        maxLen = capacity;

    }
    
    public int get(int key) {

        if (map.containsKey(key)) {
            Node node = map.get(key);
            int val = node.val;

            dll.rm(node);
            dll.addLast(node);

            return val;
            
        } else {
            return -1;
        }
        
    }
    
    public void put(int key, int value) {

        if (map.containsKey(key)) {
            Node node = map.get(key);
            node.val = value;
            dll.rm(node);
            dll.addLast(node);
        } else {

            if (dll.getLen() >= maxLen ) {
                int tmp_key = dll.rmFirst();
                map.remove(tmp_key);
            }
            Node node = new Node(key, value);
            map.put(key, node);
            dll.addLast(node);
        }

        
    }
}

class Node {

    public int key, val;

    public Node next, prev;

    public Node (int key, int val) {
        this.key = key;
        this.val = val;
    }

}

class DoubleLinkedList {

    private Node head;
    private Node tail;
    private int len;

    public DoubleLinkedList () {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);

        head.next = tail;
        tail.prev = head;

        len = 0;
    }

    public void rm (Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;

        len--;
    }

    public int rmFirst () {

        if (head.next != tail) {

            int key = head.next.key;

            head.next = head.next.next;
            head.next.prev = head;
            len--;

            return key;
        }

        return -1;

        
    }

    public void rmLast () {
        if (head.next != tail) {
            tail.prev = tail.prev.prev;
            tail.prev.next = tail;
            len--;
        }

        
    }

    public void addLast (Node node) {
        tail.prev.next = node;
        node.prev = tail.prev;

        node.next = tail;
        tail.prev = node;

        len++;

    }

    public int getLen () {
        return len;
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
Complexity Analysis
Time 
 for get and put
Space 
@acy925
acy925 commented 5 hours ago • 
思路
代码
class ListNode: # 定义双链表的节点
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class LRUCache(object):

    def __init__(self, capacity): 
        """
        :type capacity: int
        """
        self.look_up = collections.defaultdict() # 哈希表
        self.head = ListNode(-1,-1) # 双链表，需要头和尾
        self.tail = ListNode(-1,-1)
        self.head.right = self.tail # 刚开始初始化的时候，只有两个结点
        self.tail.left = self.head
        self.capacity = capacity

    def remove(self, node):
        node.left.right = node.right
        node.right.left = node.left # 我右侧节点的左侧等于我的左侧

    def insert(self, node):
        node.right = self.head.right
        node.left = self.head

        self.head.right.left = node
        self.head.right = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.look_up: # 先判断是否存在
            return -1
        else:
            node = self.look_up[key]
            #先把这个节点从链表里remove
            self.remove(node)
            #再把这个节点放到链表头部
            self.insert(node)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.look_up: # 第一种情况：如果哈希表里有key
            node = self.look_up[key]
            node.value = value
            #将这个node从链表里remove，
            self.remove(node)
            #将这个node插入到头部
            self.insert(node)
        else:                  # 第二种情况：如果哈希表里没有key，则插入
            #如果链表已经满了
            if len(self.look_up) == self.capacity:
                node = self.tail.left
                self.remove(node) # 从链表里把最后一个节点删除
                # self.tail.left = node.left
                # node.left.right = self.tail
                del self.look_up[node.key] # 从哈希表里把最后一个节点删除
                

            #创建节点
            node = ListNode(key, value)
            #将节点放入look_up里
            self.look_up[key] = node
            #将节点放入链表里
            self.insert(node)
复杂度分析

时间复杂度：O(1)
空间复杂度：O(N)
@yfu6
yfu6 commented 4 hours ago
def __init__(self, capacity: int):
    self.capacity = capacity
    self.dic = collections.OrderedDict()

def get(self, key: int) -> int:
    if key not in self.dic:
        return -1
    
    self.dic.move_to_end(key)
    return self.dic[key]
    
def put(self, key: int, value: int) -> None:
    if key in self.dic:
        self.dic.move_to_end(key)
    
    self.dic[key] = value
    if len(self.dic) > self.capacity:
        self.dic.popitem(False)
@Beanza
Beanza commented 3 hours ago
def init(self, capacity: int):
self.capacity = capacity
self.dic = collections.OrderedDict()

def get(self, key: int) -> int:
if key not in self.dic:
return -1

self.dic.move_to_end(key)
return self.dic[key]
def put(self, key: int, value: int) -> None:
if key in self.dic:
self.dic.move_to_end(key)

self.dic[key] = value
if len(self.dic) > self.capacity:
    self.dic.popitem(False)
@zhaoygcq
zhaoygcq commented 2 hours ago
思路
直接利用Map中键的特性完成。

代码
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.size = capacity;
    this.map = new Map();
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if(this.map.has(key)) {
        let res = this.map.get(key);
        this.map.delete(key);
        this.put(key, res);
        return res;
    }
    return -1;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if(this.map.has(key)) {
        this.map.delete(key);
    } else if(this.map.size === this.size) {
        let keys = [...this.map.keys()];
        this.map.delete(keys[0])
    }
    this.map.set(key, value);
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@RocJeMaintiendrai
RocJeMaintiendrai commented 1 hour ago
class LRUCache {
private Node head;
private Node tail;
private Map<Integer, Node> map;
private int capacity;

public LRUCache(int capacity) {
    map = new HashMap<>();
    head = new Node(0, 0);
    tail = new Node(0, 0);
    this.capacity = capacity;
    head.next = tail;
    tail.prev = head;
}

public int get(int key) {
    if(!map.containsKey(key)) {
        return -1;
    }
    Node node = map.get(key);
    remove(node);
    insert(node);
    return node.value;
}

public void put(int key, int value) {
    if(map.containsKey(key)) {
        remove(map.get(key));
    }
    if(map.size() == capacity) {
        remove(tail.prev);
    }
    insert(new Node(key, value));
}

private void remove(Node node) {
    map.remove(node.key);
    node.prev.next = node.next;
    node.next.prev = node.prev;
}

private void insert(Node node) {
    map.put(node.key, node);
    Node headNext = head.next;
    headNext.prev = node;
    node.next = headNext;
    head.next = node;
    node.prev = head;
    headNext.prev = node;
}

private class Node {
    Node next, prev;
    int key, value;
    Node(int key, int value) {
        this.key = key;
        this.value = value;
    }
}
}

