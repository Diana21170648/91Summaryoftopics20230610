### 思路
从上往下查询
从下往上删除

### 代码
```python
class Node:
    def __init__(self,val=0,right=None,down=None):
        self.val=val
        self.right=right
        self.down=down


class Skiplist:
    def __init__(self):
        left=[Node(-1) for _ in range(16)]
        right=[Node(20001) for _ in range(16)]
        for i in range(15):
            left[i].right=right[i]
            left[i].down=left[i+1]
            right[i].down=right[i+1]
        left[-1].right=right[-1]
        self.root=left[0]
        


    def search(self, target: int) -> bool:
        cur=self.root
        while cur:
            if target<cur.right.val:
                cur=cur.down
            elif target>cur.right.val:
                cur=cur.right
            else:
                return True
        return False



    def add(self, num: int) -> None:
        cur=self.root
        stack=[]
        while cur:
            if cur.right.val>=num:
                stack.append(cur)
                cur=cur.down
            else:
                cur=cur.right
        pre=None
        while stack:
            cur=stack.pop()
            node=Node(num)
            node.right=cur.right
            cur.right=node
            if pre:
                node.down=pre
            pre=node
            if random.randint(0,1):
                break



    def erase(self, num: int) -> bool:
        cur=self.root
        removed=False
        while cur:
            if num<cur.right.val:
                cur=cur.down
            elif num>cur.right.val:
                cur=cur.right
            else:
                cur.right=cur.right.right
                removed=True
                cur=cur.down
        return removed


```
**复杂度分析**
- 时间复杂度：O(logN)，增删查复杂度。
- 空间复杂度：O(N)
