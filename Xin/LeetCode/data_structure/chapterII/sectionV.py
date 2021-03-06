'''
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

提示：

0 <= num < 231

Python3



作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/99wd55/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 字符串遍历
class Solution:
    def translateNum(self, num):
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            a, b = (a+b if '10' <= s[i-2:i] <= '25' else a), a
        return a

# 数字求余
class Solution:
    def translateNum(self, num):
        a = b = 1
        y = num % 10
        while num > 9:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= 10*x + y <= 25 else a), a
            y = x
        return a

