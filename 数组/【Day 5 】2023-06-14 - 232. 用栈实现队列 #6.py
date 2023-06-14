【Day 5 】2023-06-14 - 232. 用栈实现队列 #6
Open
azl397985856 opened this issue 10 hours ago · 4 comments
Open
【Day 5 】2023-06-14 - 232. 用栈实现队列
#6
azl397985856 opened this issue 10 hours ago · 4 comments
Comments
@azl397985856
azl397985856 commented 10 hours ago
232. 用栈实现队列
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/implement-queue-using-stacks/

前置知识
栈
队列
题目描述
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek(); // 返回 1
queue.pop(); // 返回 1
queue.empty(); // 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的、 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
@azl397985856 azl397985856 added 栈 5 labels 10 hours ago

@Diana21170648
Diana21170648 commented now
思路
用两个栈实现一个先进先出的队列
push进s1里
pop时，先判断s2非空，再pop进s2
peek的是s2的队头元素
s1和s2均空时，则为真，否则一直为false

代码
class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]


    def push(self, x: int) -> None:
        self.s1.append(x)


    def pop(self) -> int:
        #先用oeak保证s2非空
        self.peek()
        return self.s2.pop()


    def peek(self) -> int:
        #把s1栈的元素压入栈s2
        if not self.s2:#此时s2为空
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]


    def empty(self) -> bool:#为空返回True
        return not self.s1 and not self.s2
复杂度分析

时间复杂度：O(N)，其中 N 为栈中元素的个数。
空间复杂度：O(N)

@yetfan
yetfan commented 9 hours ago
代码
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack2:
            return self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


    def peek(self) -> int:
        ans = self.pop()
        self.stack2.append(ans)
        return ans


    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
@bi9potato
bi9potato commented 7 hours ago
Approach
Code
class MyQueue {

    Deque<Integer> s1;
    Deque<Integer> s2;

    public MyQueue() {

        s1 = new LinkedList<>();
        s2 = new LinkedList<>();
        
    }
    
    public void push(int x) {

        s1.push(x);
        
    }
    
    public int pop() {

        if (s2.isEmpty()) {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }

        return s2.pop();
        
    }
    
    public int peek() {

        if (s2.isEmpty()) {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }

        return s2.peek();
        
    }
    
    public boolean empty() {

        return s1.isEmpty() && s2.isEmpty();
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
Complexity Analysis
Time:
 for push,
 for pop,
 for peek,
 for empty
Space: 
@zhaoygcq
zhaoygcq commented 2 hours ago
思路
栈与队列的本质区别：

栈是先进后出
队列是先进先出
所以，要想通过栈去模拟一个队列，那就需要两个栈(一个用于存，一个用于取)。两者主要的区别体现在去首个元素
如队列[1,2,3]的队首是1；如果是栈，那其栈顶元素为3；所以可以在取队列首个元素时，先将栈中
的所有内容弹出[3,2,1](只在当前作为取的这个栈为空时才需要弹出用于存的栈的所有内容);这样栈顶元素就是1了
代码
var MyQueue = function() {
    this.queue = [];
    this.hqueue = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.queue.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    if(!this.hqueue.length) {
        while(this.queue.length) {
            this.hqueue.push(this.queue.pop());
        }
    }

    return this.hqueue.pop();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    if(!this.hqueue.length) {
        while(this.queue.length) {
            this.hqueue.push(this.queue.pop());
        }
    }

    return this.hqueue[this.hqueue.length - 1];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return !this.queue.length && !this.hqueue.length;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@Diana21170648
Diana21170648 commented now
思路
用两个栈实现一个先进先出的队列
push进s1里
pop时，先判断s2非空，再pop进s2
peek的是s2的队头元素
s1和s2均空时，则为真，否则一直为false

代码
class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]


    def push(self, x: int) -> None:
        self.s1.append(x)


    def pop(self) -> int:
        #先用oeak保证s2非空
        self.peek()
        return self.s2.pop()


    def peek(self) -> int:
        #把s1栈的元素压入栈s2
        if not self.s2:#此时s2为空
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]


    def empty(self) -> bool:#为空返回True
        return not self.s1 and not self.s2
复杂度分析

时间复杂度：O(N)，其中 N 为栈中元素的个数。
空间复杂度：O(N)
