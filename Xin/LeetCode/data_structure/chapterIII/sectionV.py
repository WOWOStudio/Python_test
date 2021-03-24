'''
剑指 Offer 28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树[1,2,2,3,4,4,3] 是对称的。

  1
 / \
 2  2
/ \ / \
3 4 4 3
但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

  1
 / \
 2  2
 \  \
 3  3



示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false

限制：

0 <= 节点个数 <= 1000

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5d412v/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

class Solution:
    def isSymmetric(self, root):
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)
