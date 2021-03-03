'''
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0, F(1)= 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5

提示：

0 <= n <= 100

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/50fxu1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 循环求余法
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a+b) % 1000000007
        return a

# 动态规划
class Solution:
    def fib(self, n):
        if n < 0:
            return -1
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            dp = []
            dp.append(0)
            dp.append(1)
            for i in range(2, n+1):
                dp_tmp = (dp[i-1] + dp[i-2])%1000000007
                dp.append(dp_tmp)
            return dp[n]

# 递归
class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

# 回溯
class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        leftFib = self.fib(n-1)
        rightFib = self.fib(n-2)

        return leftFib + rightFib
