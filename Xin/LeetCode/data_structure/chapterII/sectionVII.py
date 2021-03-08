'''
剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



示例1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。


提示：

s.length <= 40000

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5dgr0c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# 动态规划 + 哈希表
class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            tmp = tmp + 1 if tmp < j - i else j - i
            res = max(res, tmp)
        return res

# 动态规划 + 线性遍历
class Solution:
    def lengthOfLongestSubstring(self, s):
        res = tmp = i = 0
        for j in range(len(s)):
            i = j - 1
            while i >= 0 and s[i] != s[j]:
                i -= 1
            tmp = tmp + 1 if tmp < j - i else j - i
            res = max(res, tmp)
        return res

# 双指针 + 哈希表
class Solution:
    def lengthOfLongestSubstring(self, s):
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j
            res = max(res, j - i)
        return res
