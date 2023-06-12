【Day 3 】2023-06-12 - 1381. 设计一个支持增量操作的栈 #4
Open
azl397985856 opened this issue 16 hours ago · 13 comments
Open
【Day 3 】2023-06-12 - 1381. 设计一个支持增量操作的栈
#4
azl397985856 opened this issue 16 hours ago · 13 comments
Comments
@azl397985856
azl397985856 commented 16 hours ago
1381. 设计一个支持增量操作的栈
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/design-a-stack-with-increment-operation/

前置知识
栈
前缀和
题目描述
请你设计一个支持下述操作的栈。

实现自定义栈类 CustomStack ：

CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量，栈在增长到 maxSize 之后则不支持 push 操作。
void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
int pop()：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 -1 。
void inc(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。


示例：

输入：
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
输出：
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
解释：
CustomStack customStack = new CustomStack(3); // 栈是空的 []
customStack.push(1); // 栈变为 [1]
customStack.push(2); // 栈变为 [1, 2]
customStack.pop(); // 返回 2 --> 返回栈顶值 2，栈变为 [1]
customStack.push(2); // 栈变为 [1, 2]
customStack.push(3); // 栈变为 [1, 2, 3]
customStack.push(4); // 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
customStack.increment(5, 100); // 栈变为 [101, 102, 103]
customStack.increment(2, 100); // 栈变为 [201, 202, 103]
customStack.pop(); // 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
customStack.pop(); // 返回 202 --> 返回栈顶值 202，栈变为 [201]
customStack.pop(); // 返回 201 --> 返回栈顶值 201，栈变为 []
customStack.pop(); // 返回 -1 --> 栈为空，返回 -1


提示：

1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
每种方法 increment，push 以及 pop 分别最多调用 1000 次
@azl397985856 azl397985856 added 栈 3 labels 16 hours ago
@bi9potato
bi9potato commented 14 hours ago
Approch
Trade space for time by using an additional stack.
Add val during the pop operation.

code
class CustomStack {

    private int[] s;
    private int top_pointer;
    private int bottom_pointer;

    private int[] inc_s;

    public CustomStack(int maxSize) {

        s = new int[maxSize];
        top_pointer = -1;
        bottom_pointer = 0;

        inc_s = new int[maxSize];
        
    }
    
    public void push(int x) {

        if ( top_pointer < s.length-1 ) {
            s[++top_pointer] = x;
        } 
        
    }
    
    public int pop() {

        if (top_pointer == -1) {
            return -1;
        } else {
            if (inc_s[top_pointer] != 0) {
                int val = inc_s[top_pointer];
                if (top_pointer != 0) inc_s[top_pointer-1] += val;
                inc_s[top_pointer] = 0;
                return s[top_pointer--] + val;
            } else {
                return s[top_pointer--];
            }
        }

    }
    
    public void increment(int k, int val) {

        if (k-1 > top_pointer) {
            k = top_pointer+1;
        }

        if (k > 0) inc_s[k-1] += val;
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
Complexity Analysis

time: All 
space: All 
 but CostomStack 
@Fuku-L
Fuku-L commented 12 hours ago
思路
因为题目中 inc() 方法需要遍历栈底到k的区间，因此使用使用数组和指针来完成

代码
class CustomStack {
    int[] arr = null;
    int top;
    public CustomStack(int maxSize) {
        arr = new int[maxSize];
        top = -1;
    }
    
    public void push(int x) {
        if(top < arr.length-1){
            arr[++top] = x;
        }
    }
    
    public int pop() {
        if(top >= 0){
            return arr[top--];
        } else {
            return -1;
        }
    }
    
    public void increment(int k, int val) {
        int loop = Math.min(k-1, top);
        for(int i = 0; i <= loop; i++){
            arr[i] += val;
        }
    }
}
复杂度分析

时间复杂度：出栈和入栈为O(1)，increment方法为O(N)， N 为数组长度。
空间复杂度：O(N)
@SoSo1105
SoSo1105 commented 8 hours ago
思路
pop时把栈顶元素弹出

代码
class CustomStack:

    def __init__(self, maxSize: int):
        self.size = 0
        self.maxSize = maxSize
        self.customStack = []

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.customStack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        temp = self.customStack[self.size - 1]
        del self.customStack[self.size - 1]
        self.size -= 1
        return temp

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.customStack[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
@zhaoygcq
zhaoygcq commented 8 hours ago
思路
增量更新数值时，先将栈中所有数据弹出；之后根据个数k以及栈的实际大小完成数据的增量更新

代码
/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    this.maxSize = maxSize;
    this.stack = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if(this.stack.length < this.maxSize) {
        this.stack.push(x);
    }
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    if(this.stack.length) {
        return this.stack.pop();
    }
    return -1;
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    let temp = [];
    while(this.stack.length) {
        temp.push(this.stack.pop());
    }

    while(temp.length && k) {
        this.stack.push(temp.pop() + val);
        k--;
    }

    while(temp.length) {
        this.stack.push(temp.pop())
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */
复杂度分析

时间复杂度：O(N)，其中 N 为数组长度。
空间复杂度：O(N)
@acy925
acy925 commented 7 hours ago
思路
列表实现栈，一个指针变量记录栈顶元素的位置，最后可以优化成全部 O(1)

代码
class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = [0] * maxSize
        self.add = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top != len(self.stk) - 1:
            self.top += 1
            self.stk[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        ans = self.stk[self.top] + self.add[self.top]
        if self.top != 0:
            self.add[self.top - 1] += self.add[self.top]
        self.add[self.top] = 0
        self.top -= 1
        return ans

    def increment(self, k: int, val: int) -> None:
        lim = min(k - 1, self.top)
        if lim >= 0:
            self.add[lim] += val

**复杂度分析**
- 时间复杂度：O(1)
- 空间复杂度：O(N)
@guangsizhongbin
guangsizhongbin commented 7 hours ago
题目地址(1381. 设计一个支持增量操作的栈)
https://leetcode.cn/problems/design-a-stack-with-increment-operation/

题目描述
请你设计一个支持对其元素进行增量操作的栈。

实现自定义栈类 CustomStack ：

CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量。
void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
int pop()：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 -1 。
void inc(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。

 

示例：

输入：
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
输出：
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
解释：
CustomStack stk = new CustomStack(3); // 栈是空的 []
stk.push(1);                          // 栈变为 [1]
stk.push(2);                          // 栈变为 [1, 2]
stk.pop();                            // 返回 2 --> 返回栈顶值 2，栈变为 [1]
stk.push(2);                          // 栈变为 [1, 2]
stk.push(3);                          // 栈变为 [1, 2, 3]
stk.push(4);                          // 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
stk.increment(5, 100);                // 栈变为 [101, 102, 103]
stk.increment(2, 100);                // 栈变为 [201, 202, 103]
stk.pop();                            // 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
stk.pop();                            // 返回 202 --> 返回栈顶值 202，栈变为 [201]
stk.pop();                            // 返回 201 --> 返回栈顶值 201，栈变为 []
stk.pop();                            // 返回 -1 --> 栈为空，返回 -1


 

提示：

1 <= maxSize, x, k <= 1000
0 <= val <= 100
每种方法 increment，push 以及 pop 分别最多调用 1000 次
前置知识
公司
暂无
思路
关键点
代码
语言支持：Go
Go Code:

type CustomStack struct {
    stack []int
}


func Constructor(maxSize int) CustomStack {
    if maxSize < 0 {
        return CustomStack{}
    }

    return CustomStack{
        stack: make([]int, 0, maxSize),
    }
}


func (this *CustomStack) Push(x int)  {
    if len(this.stack) == cap(this.stack) {
        return
    } 
    this.stack = append(this.stack, x)
}


func (this *CustomStack) Pop() int {
    if (len(this.stack) == 0 ){
        return -1
    }

    pop := this.stack[len(this.stack)-1]
    this.stack = this.stack[:len(this.stack)-1]
    return pop
}


func (this *CustomStack) Increment(k int, val int)  {

    n := min(k, len(this.stack))

    for i := 0; i < n; i++ {
        this.stack[i] = this.stack[i] + val
    }

    return
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}


/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */
复杂度分析

令 n 为数组长度。

时间复杂度：$O(n)$
空间复杂度：$O(n)$
@iambigchen
iambigchen commented 6 hours ago
思路
用increments来存所有的increment操作，increment[i]表示前i个值都加increment[i]值

在pop的时候，只需要把栈顶值取出，加increment[i]。在更新维护increment[i-1]，将increment[i-1] 变成 increment[i] + increment[i-1]。然后重置increment[i]为0即可

关键点
代码
语言支持：JavaScript
JavaScript Code:

var CustomStack = function(maxSize) {
    this.maxSize = maxSize
    this.list = []
    this.increments = Array(maxSize).fill(0)
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if (this.list.length < this.maxSize) {
        this.list.push(x)
    }
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    if (this.list.length === 0) return -1
    let i = this.list.length - 1
    this.increments[i-1] += this.increments[i]
    let res = this.list.pop() + this.increments[i]
    this.increments[i] = 0
    return res
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    let i = Math.min(k, this.list.length) -1
    if (i >= 0) {
        this.increments[i] += val
    }
};
复杂度分析

令 n 为数组长度。

时间复杂度：$O(1)$
空间复杂度：$O(1)$
@wzbwzt
wzbwzt commented 4 hours ago
/*
思路:
前缀和思路：维护一个increDiff固定容量的数组，记录每次incre 操作的差值
push时 increDiff: append(0)
increment(k,v)时 increDiff[k-1]+=v (k =min(k,cnt))
pop时 out=list[cnt-1]+incretment[cnt-1]
increment[cnt-2]+=increment[cnt-1]
re切割list,increment

时间复杂度：全部都是 O(1)
空间复杂度为 O(cnt)
*/

type CustomStack struct {
	list      []int
	cnt       int
	maxsize   int
	increDiff []int
}

func Constructor(maxSize int) CustomStack {
	return CustomStack{list: make([]int, 0, maxSize), cnt: 0, maxsize: maxSize, increDiff: make([]int, 0, maxSize)}
}

func (c *CustomStack) Push(x int) {
	if c.cnt == c.maxsize {
		return
	}
	c.list = append(c.list, x)
	c.increDiff = append(c.increDiff, 0)
	c.cnt++
}

func (c *CustomStack) Pop() int {
	if c.cnt == 0 {
		return -1
	}
	out := c.list[c.cnt-1] + c.increDiff[c.cnt-1]

	c.list = c.list[:c.cnt-1]
	if c.cnt >= 2 {
		c.increDiff[c.cnt-2] += c.increDiff[c.cnt-1]
	}
	c.increDiff = c.increDiff[:c.cnt-1]

	c.cnt--
	return out
}

func (c *CustomStack) Increment(k int, val int) {
	if k > c.cnt {
		k = c.cnt
	}
	if k == 0 {
		return
	}
	c.increDiff[k-1] += val
}
@snmyj
snmyj commented 4 hours ago
class CustomStack {
public:
    int maxs=0;
    vector<int> ss;
    CustomStack(int maxSize) {
       maxs=maxSize;
    }
    
    void push(int x) {
      if(ss.size()<maxs) ss.push_back(x);
    }
    
    int pop() {
       if(ss.size()==0) return -1;
       int res=ss.back();
         ss.pop_back();
       return res;
       
    }
    
    void increment(int k, int val) {
       if(ss.size()==0) return;
        for(int i=0;i<k;i++){
            if(i==ss.size()-1){
                ss[i]+=val;
                break;
            }
            ss[i]+=val;
        }
    }
};
@RanDong22
RanDong22 commented 2 hours ago
思路
pop方法对栈的长度为0时，返回-1；
push方法对栈的长度为maxSize时，不进行push；
increment方法对序号小于指定值的元素进行操作，循环时筛选；
代码
class CustomStack {
  private arr: number[] = [];
  private maxSize: number;
  constructor(maxSize: number) {
    this.maxSize = maxSize;
  }

  push(x: number): void {
    if (this.arr.length < this.maxSize) {
      thiincreas.arr.push(x);
    }
  }

  pop(): number {
    if (this.arr.length > 0) {
      return this.arr.pop()!;
    }
    return -1;
  }

  increment(k: number, val: number): void {
    this.arr.forEach((_val, index) => {
      if (index < k) {
        this.arr[index] = val + _val;
      }
    });
  }
}
@YQYCS
YQYCS commented 1 hour ago
代码
class CustomStack:

    def __init__(self, maxSize: int):
        self.size = 0
        self.maxSize = maxSize
        self.CustomStack = []

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.CustomStack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        res = self.CustomStack[-1]
        del self.CustomStack[-1]
        self.size -= 1
        return res
       
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.CustomStack[i] += val
复杂度
push()方法的时间复杂度为 $O(1)，需在列表末尾添加一个元素。
pop()方法的时间复杂度为 $O(1)，需删除列表末尾的一个元素。
increment()方法的时间复杂度为 O(k)，需遍历栈顶的前k个元素进行加法操作。
空间复杂度为 O(maxSize)，需使用一个列表来存储栈的元素。
@freesan44
freesan44 commented 46 minutes ago
思路
代码
class CustomStack {
    
    var maxLen: Int
    var tempArr: [Int]
    
    init(_ maxSize: Int) {
        maxLen = maxSize
        tempArr = Array<Int>()
    }
    
    func push(_ x: Int) {
        if tempArr.count <= maxLen-1{
            tempArr.append(x)
        }
    }
    
    func pop() -> Int {
        if tempArr.count == 0{
            return -1
        }
        else{
            return tempArr.removeLast() 
        }
    }
    
    func increment(_ k: Int, _ val: Int) {
        if tempArr.count <= k{
            self.tempArr = self.tempArr.map{$0 + val}
        }
        else
        {
            for i in self.tempArr.indices.prefix(k){
                self.tempArr[i] += val
            }
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * let obj = CustomStack(maxSize)
 * obj.push(x)
 * let ret_2: Int = obj.pop()
 * obj.increment(k, val)
 */
@Diana21170648
Diana21170648 commented 1 minute ago
思路
栈的实现，增量栈先出后加再入栈
出栈主要边界-1
入栈注意边界maxsize

代码
class CustomStack:
    def __init__(self, maxSize: int):
        self.st=[]
        self.cnt=0
        self.size=maxSize

    def push(self, x: int) -> None:#判断是否满了，满了就不能添加到栈顶
        if self.cnt<self.size:
            self.st.append(x)
            self.cnt+=1

    def pop(self) -> int:#栈为空，则返回-1
        if self.cnt==0:
            return -1
        self.cnt-=1
        return self.st.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(0,min(self.cnt,k)):
            self.st[i]+=val
复杂度分析

时间复杂度：O(min（k,cnt）)，其中 cnt为栈的可操作长度，k为要增量的个数。
空间复杂度：O(1)
