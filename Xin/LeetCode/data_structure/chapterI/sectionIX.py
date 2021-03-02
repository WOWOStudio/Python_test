'''
剑指 Offer 58 - II. 左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


示例 1：

输入: s = "abcdefg", k = 2
输出:"cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出:"umghlrlose"


限制：

1 <= k < s.length <= 10000

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/589fz2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 字符串切片
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return str[n:] + str[:n]

# 列表遍历拼接
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, n+len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)

# 字符串遍历拼接
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, n+len(s)):
            res += s[i % len(s)]
        return res

