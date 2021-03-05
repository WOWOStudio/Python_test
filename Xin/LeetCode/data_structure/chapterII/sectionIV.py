'''
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。

提示：

1 <=arr.length <= 10^5
-100 <= arr[i] <= 100

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/59gq9c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# 动态规划
class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)

