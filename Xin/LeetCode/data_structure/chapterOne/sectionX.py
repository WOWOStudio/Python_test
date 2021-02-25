'''
剑指 Offer 59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/58o46i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1-k, n+1-k),range(n)):
            if i > 0 and deque[0] == nums[i-1]:
                deque.popleft()
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])
        return res

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0: return []
        deque = collections.deque()
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = deque[0]

        for i in range(k, len(nums)):
            if deque[0] == nums[i-k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res
