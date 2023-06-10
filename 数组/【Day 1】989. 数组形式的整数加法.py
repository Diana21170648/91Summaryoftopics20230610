难度
简单

标签
数组

前置知识
数组的遍历

思路
如果你没做出来这道题，不妨先试试 66. 加一，那道题是这道题的简化版，即 K = 1 的特殊形式。

这道题的思路是 从低位到高位计算，注意进位和边界处理。 细节都在代码里。

为了简化判断，我将 carry（进位） 和 K 进行了统一处理，即 carry = carry + K

关键点
处理进位

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        for i in range(len(A) - 1, -1, -1):
            A[i], carry = (carry + A[i] + K % 10) % 10, (carry + A[i] + K % 10) // 10
            K //= 10
        B = []
        # 如果全部加完还有进位，需要特殊处理。 比如 A = [2], K = 998
        carry = carry + K
        while carry:
            B = [(carry) % 10] + B
            carry //= 10
        return B + A
