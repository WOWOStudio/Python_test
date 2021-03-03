'''
剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/57hyl5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# 动态规划
class Solution:
    def numWays(self, n: int) -> int:
        if n < 0: return -1
        elif n == 0: return 1
        elif n == 1: return 1
        else:
            dp = []
            dp.append(1)
            dp.append(1)
            for i in range(2,n+1):
                num = (dp[i-1]+dp[i-2])%1000000007
                dp.append(num)
            return dp[n]

# 循环求余法
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, (a+b)%1000000007
        return a
