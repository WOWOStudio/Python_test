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

